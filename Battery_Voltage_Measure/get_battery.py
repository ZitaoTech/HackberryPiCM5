#!/usr/bin/env python3
import smbus2, time, collections
from datetime import timedelta

class MAX17048:
    def __init__(self, i2c_bus=13, i2c_address=0x36):
        self.bus = smbus2.SMBus(i2c_bus)
        self.address = i2c_address

    def _read_u16(self, reg):
        b = self.bus.read_i2c_block_data(self.address, reg, 2)
        return (b[0] << 8) | b[1]

    def read_voltage(self):
        # VCELL 0x02–0x03: 78.125 µV/LSB (1.25 mV / 16)
        raw = self._read_u16(0x02)
        uV = raw * 78.125
        return uV / 1_000_000.0

    def read_soc(self):
        # SOC 0x04–0x05: MSB integer %, LSB in 1/256 %
        raw = self._read_u16(0x04)
        return ((raw >> 8) & 0xFF) + ((raw & 0xFF) / 256.0)

    def read_rate(self):
        # CRATE 0x16–0x17: signed, LSB ≈ 0.208 %/h
        raw = self._read_u16(0x16)
        if raw & 0x8000:
            raw = -((~raw & 0xFFFF) + 1)
        return raw * 0.208

    def close(self):
        self.bus.close()

def fmt_eta(hours):
    if hours is None or hours <= 0 or hours > 1e4:
        return "ETA: n/a"
    t = int(hours * 3600)
    h, m = divmod(t // 60, 60)
    return f"ETA: {h}h{m:02d}m"

if __name__ == "__main__":
    g = MAX17048()
    try:
        # Keep last ~120 seconds of (time,soc) for slope-based ETA
        hist = collections.deque(maxlen=120)

        while True:
            try:
                v = g.read_voltage()
                soc = g.read_soc()
                rate = g.read_rate()  # % per hour, signed

                # --- ETA from CRATE ---
                eta_h = None
                if abs(rate) > 0.05:  # ignore tiny noise
                    if rate < 0:
                        eta_h = soc / (-rate)            # to empty
                    else:
                        eta_h = max(0.0, (100.0 - soc) / rate)  # to full

                # --- Fallback: slope-based ETA over recent history ---
                now = time.time()
                hist.append((now, soc))
                if eta_h is None and len(hist) >= 30:  # need ~30s of data
                    t0, s0 = hist[0]
                    t1, s1 = hist[-1]
                    dt_h = max((t1 - t0) / 3600.0, 1e-6)
                    slope = (s1 - s0) / dt_h  # % per hour (signed)
                    if slope < -0.1:
                        eta_h = soc / (-slope)
                    elif slope > 0.1:
                        eta_h = max(0.0, (100.0 - soc) / slope)

                parts = []
                if v is not None:   parts.append(f"{v:4.2f} V")
                if soc is not None: parts.append(f"{soc:6.2f} %")
                if rate is not None:parts.append(f"{rate:+6.2f} %/h")
                parts.append(fmt_eta(eta_h))
                print(" | ".join(parts))

            except OSError as e:
                print(f"I2C error: {e}")

            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        g.close()
