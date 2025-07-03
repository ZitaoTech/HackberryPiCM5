# Install RaspberryPi OS on HackberryPi_CM5

# RaspberryPi OS has the most support among other OS for different RaspberryPi SBCs, it is recommended to install RaspberryPi OS on HackberryPi_CM5
# Follow the steps below once you have flashed the image to your SD card
# You may uncomment #dtparam=pciex1 to enable booting from the NVME drive


```Step1``` Download the ```vc4-kms-dpi-hyperpixel4sq.dtbo``` and ```hyperpixel4.dtbo``` files on the Operating Systems page of this repository
```Step2``` Put the two files into the ```/overlay/``` folder of the image disk  
```Step3```  Copy and paste the following lines into the ```/boot/config.txt```
```sh
# For more options and information see
# http://rptl.io/configtxt
# Some settings may impact device functionality. See link above for details

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

# Uncomment to enable NVME drive
#dtparam=pciex1

# Additional overlays and parameters are documented
# /boot/firmware/overlays/README

# Automatically load overlays for detected cameras
camera_auto_detect=1

# Automatically load overlays for detected DSI displays
display_auto_detect=1

# Automatically load initramfs files, if found
auto_initramfs=1

# Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d
max_framebuffers=2

# Don't have the firmware create an initial video= setting in cmdline.txt.
# Use the kernel's default instead.
disable_fw_kms_setup=1

# Run in 64-bit mode
arm_64bit=1

# Disable compensation for displays with overscan
disable_overscan=1

# Run as fast as firmware / board allows
arm_boost=1

[cm4]
# Enable host mode on the 2711 built-in XHCI USB controller.
# This line should be removed if the legacy DWC2 controller is required
# (e.g. for USB device mode) or if USB support is not required.
otg_mode=1

[cm5]
dtoverlay=dwc2,dr_mode=host

[all]
dtoverlay=dwc2,dr_mode=host
dtoverlay=vc4-kms-v3d
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```
