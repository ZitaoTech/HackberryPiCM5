# Install Arch Linux ARM on HackberryPi_CM5

Arch Linux is a Linux distribution that focuses on maximum flexibility. **This guide assumes you want to install Arch Linux into the internal SSD.** We'll achieve our goal by using a Raspberry Pi OS SD card as a live-CD-like environment.

## Step 1. Install Raspberry Pi OS on the SD card.

Follow instructions from [here](https://github.com/ZitaoTech/HackberryPiCM5/tree/main/Operating%20System/RaspberryPi_OS) to install Raspberry Pi OS (or Raspberry Pi OS since we won't need GUI to install our Arch Linux ARM instance) on the SD card. It'll be simpler to use the Pi Imager to setup WiFi connections and enable SSH. Don't forget to add these lines to your `config.txt`.

```
dtoverlay=vc4-kms-v3d
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```

## Step 2. Boot from the SD card.

Insert the SD card and boot Raspberry Pi OS. SSH into it for later use. You can find its IP address directly on the screen.

## Step 3. Upgrade your Raspberry Pi OS and install all the tools we need.

```
sudo apt update
sudo apt upgrade
reboot
```

Wait for the device to reboot. Reconnect to it and install `libarchive-tools` and `arch-install-scripts`.

```
sudo apt install libarchive-tools arch-install-scripts
```

## Step 4. Obtain the latest Arch Linux ARM aarch64 tarball

```
wget http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-aarch64-latest.tar.gz
```

## Step 5. Partitioning

**WARNING: All your data on the SSD will be destroyed in this step.**

Use `fdisk` to partition your internal SSD. You can follow the instructions for partitioning the SD card from [Arch Linux ARM official wiki for Raspberry Pi 4](https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4) to partition your SSD, just don't forget you're partitioning your SSD, not the SD card. **Change device paths accordingly, otherwise you may need to start over from Step 1.**

## Step 6. Preparing and mounting your SSD partitions

From now on, this guide assumes you're operating with the `root` user. It'll be easier, just remember not to destroy anything of the Raspberry Pi OS instance.

```
mkfs.vfat -F 32 /dev/nvme0n1p1
mkfs.ext4 /dev/nvme0n1p2
```

Now we mount our partitions.

```
cd /mnt
mkdir root
mount /dev/nvme0n1p2 root
mkdir root/boot
mount /dev/nvme0n1p1 root/boot
```

*Note: During CM5 booting process, it'll first check `/boot/firmware`, then `/boot`. We use `/boot` instead of `/boot/firmware` because Arch Linux ARM maintains its packages in such way.*

## Step 7. Release the tarball

```
mv <path-to-your-tarball> ./
bsdtar -xpf ArchLinuxARM-rpi-aarch64-latest.tar.gz -C root
```

## Step 8. `arch-chroot` into Arch Linux ARM

```
arch-chroot root
```

Now you're in a chroot environment of our newly installed Arch Linux ARM instance. It won't boot without proper configurations though.

## Step 9. Configurations

Initialize the keyring

```
pacman-key --init
pacman-key --populate archlinuxarm
```

Upgrade your Arch Linux ARM packages.

```
pacman -Syu
```

Install must-have utilities.

```
pacman -S sudo vim fakeroot
```

Change the `root` password.

```
passwd
```

Install the `linux-rpi` kernel, replacing the old kernel.

```
pacman -S linux-rpi
```

Edit `/etc/fstab`.

```
# Static information about the filesystems.
# See fstab(5) for details.

# <file system> <dir> <type> <options> <dump> <pass>
# <pass> is the order of loading parition
# main partition
/dev/nvme0n1p2  /      ext4   defaults    0      1
# boot partition
/dev/nvme0n1p1  /boot  vfat   defaults    0      2
```

Edit `/boot/cmdline.txt`. You can find the PARTUUID of your `root` partition by executing `ls /dev/disk/by-partuuid -al`.

```
root=PARTUUID=<Remember to change this!> rootfstype=ext4 rw rootwait console=serial0,115200 console=tty1 fsck.repair=yes
```

## Step 10. Firmware

The firmwares included in the Arch Linux ARM tarball is not the latest. Your CM5 won't be able to connect to WiFi correctly using their firmwares. We need to package the original Raspberry Pi OS firmwares as a pacman package and replace what were included in the Arch Linux ARM tarball.

Create another SSH session to your CM5 and copy all the firmwares to the Arch Linux ARM chroot.

```
sudo su
cd
mkdir firmware
cd firmware
cp -r /etc/alternatives ./
cp -r /usr/lib/firmware ./
rm firmware/regulatory.db firmware/regulatory.db.p7s
tar -cvf firmware.tar ./
mkdir /mnt/root/home/alarm/linux-firmware-rpi
cp firmware.tar /mnt/root/home/alarm/linux-firmware-rpi/firmware.tar
```

In the first SSH session (which is now a chroot environment of your Arch Linux ARM instance) and switch to the default `alarm` user and obtain ownerships of the `linux-firmware-rpi` folder and its contents.

```
su alarm
cd
su
chown -R alarm:alarm ./linux-firmware-rpi
exit
cd linux-firmware-rpi
```

Create a `PKGBUILD` in the `linux-firmware-rpi` directory

```
pkgname=linux-firmware-cm5
pkgver=20250724
pkgrel=1
pkgdesc="Custom firmware for CM5, provides linux-firmware"
arch=('aarch64')
provides=('linux-firmware' 'firmware-raspberrypi')
conflicts=('linux-firmware' 'linux-firmware-amdgpu' 'linux-firmware-atheros' 'linux-firmware-broadcom' 'linux-firmware-cirrus' 'linux-firmware-intel' 'linux-firmware-mediatek' 'linux-firmware-nvidia' 'linux-firmware-other' 'linux-firmware-radeon' 'linux-firmware-realtek' 'firmware-raspberrypi')
license=('custom')
source=("firmware.tar")
sha256sums=('SKIP')

options=('!strip')

package() {
    cd "$srcdir"
    tar -xvf firmware.tar

    install -dm755 "$pkgdir/etc/alternatives"
    cp -r alternatives/* "$pkgdir/etc/alternatives/"

    install -dm755 "$pkgdir/usr/lib/firmware"
    cp -r firmware/* "$pkgdir/usr/lib/firmware/"
}
```

Make and install the pacman package, replacing old firmware packages.

```
makepkg
su
pacman -U linux-firmware-cm5-20250724-1-aarch64.pkg.tar.xz
exit
```

## Step 11. Migrate `config.txt`

Using the second SSH session which is not chrooted into Arch Linux ARM to migrate config.txt from Raspberry Pi OS.

```
sudo su
cp /boot/firmware/config.txt /mnt/root/boot/config.txt
```

## Step 12. Clean up and reboot

Exit from the chroot environment and sync your disks. Then `umount` all your SSD partitions and shutdown the device.

```
sync
umount /mnt/root/boot
umount /mnt/root
shutdown now
```

Take out the SD card and boot. You'll get a clean Arch Linux ARM system.

## Final step

Save your SD card that contains the Raspberry Pi OS somewhere safe. It can be used as a live-CD-like thing to fix your Arch Linux ARM whenever it breaks.

Configure your Arch Linux ARM. Here are some useful links.
- [Network](https://wiki.archlinux.org/title/Network_configuration)
- [Locale](https://wiki.archlinux.org/title/Locale)
- [Timezone](https://wiki.archlinux.org/title/System_time)
- [Desktop environments](https://wiki.archlinux.org/title/Desktop_environment)
- [Display managers](https://wiki.archlinux.org/title/Display_manager)
- [AUR](https://wiki.archlinux.org/title/Arch_User_Repository)