# Install Ubuntu on HackberryPi_CM5

### Ubuntu is a Linux distribution derived from Debian and composed mostly of free and open-source software

⚠️⚠️⚠️  
## Note: Ubuntu is currently not supported on the Raspberry Pi CM5. Installing Ubuntu may result in system crashes. There might be kernel patches in the future to fix this. However, you can display the system image using the following method:


```Step1``` Download the Ubuntu image from the pi imager(main folder-> other general-purpose OS-> Ubuntu)  
```Step2``` Copy the following content into the config.txt and override  
```Step3``` Insert the TF card into the HackberryPi_CM5 and power it on, wait a few seconds and you can see it booting  


```sh
[all]
arm_64bit=1
kernel=vmlinuz
cmdline=cmdline.txt
initramfs initrd.img followkernel

# Enable the audio output, I2C and SPI interfaces on the GPIO header. As these
# parameters related to the base device-tree they must appear *before* any
# other dtoverlay= specification
dtparam=audio=on
#dtparam=i2c_arm=off
#dtparam=spi=off

# Comment out the following line if the edges of the desktop appear outside
# the edges of your display
disable_overscan=1

# If you have issues with audio, you may try uncommenting the following line
# which forces the HDMI output into HDMI mode instead of DVI (which doesn't
# support audio output)
#hdmi_drive=2

# Enable the KMS ("full" KMS) graphics overlay, leaving GPU memory as the
# default (the kernel is in control of graphics memory with full KMS)
dtoverlay=vc4-kms-v3d
disable_fw_kms_setup=1

# Autoload overlays for any recognized cameras or displays that are attached
# to the CSI/DSI ports. Please note this is for libcamera support, *not* for
# the legacy camera stack
camera_auto_detect=1
display_auto_detect=1

# Config settings specific to arm64
dtoverlay=dwc2

[pi4]
max_framebuffers=2
arm_boost=1

[pi3+]
# Use a smaller contiguous memory area, specifically on the 3A+ to avoid an
# OOM oops on boot. The 3B+ is also affected by this section, but it shouldn't
# cause any issues on that board
dtoverlay=vc4-kms-v3d,cma-128

[pi02]
# The Zero 2W is another 512MB board which is occasionally affected by the same
# OOM oops on boot.
dtoverlay=vc4-kms-v3d,cma-128

[cm4]
# Enable the USB2 outputs on the IO board (assuming your CM4 is plugged into
# such a board)
dtoverlay=dwc2,dr_mode=host

[all]
dtoverlay=dwc2,dr_mode=host
dtoverlay=vc4-kms-v3d
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```
![image](https://github.com/user-attachments/assets/3ee45c39-7f7b-4a17-9fb0-ba4bc1ffa9c9)
