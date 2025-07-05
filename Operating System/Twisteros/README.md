# Install TwisterOS on HackberryPi_CM5

Twister OS is a Linux-based operating system developed by Pi Labs for the Raspberry Pi series of single-board computers. A version for x86-64-based personal computers was released shortly after the initial Raspberry Pi release. The operating system is based on Raspberry Pi OS Lite and uses the Xfce desktop environment.

```Step1``` Download the TwisterOS from this [page](https://twisteros.com/downloads/)  
```Step2``` Flash the downloaded image into a TF card  
```Step3``` Copy the following content into the config.txt and override  
```Step4``` Insert the TF card into the HackberryPi_CM5 and power it on, you need to manually reboot the device via the main power switch after you see the white LED on top not blinking any more
Then you can see the device booting into TwisterOS

```sh
# For more options and information see
# http://rptl.io/configtxt
# Some settings may impact device functionality. See link above for details

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

# Automatically load overlays for detected cameras
camera_auto_detect=1

# Automatically load overlays for detected DSI displays
display_auto_detect=1

# Automatically load initramfs files, if found
auto_initramfs=1

# Disable overscan compensation for displays
disable_overscan=1

# Prevent the firmware from overriding KMS video settings via cmdline
disable_fw_kms_setup=1

# Run as fast as the firmware and board allows
arm_boost=1

[cm4]
# Enable host mode on the 2711 built-in XHCI USB controller
otg_mode=1

[cm5]
# Enable USB host mode using DWC2 driver
dtoverlay=dwc2,dr_mode=host

[all]
kernel=kernel8.img
dtoverlay=dwc2,dr_mode=host
dtoverlay=vc4-kms-dpi-hyperpixel4sq

```

### Default username and password

```sh
pi  
pi  
```

![480714362bcb7fc65ef39b1c5f9be44](https://github.com/user-attachments/assets/513c5497-0089-49d0-81a0-0161951a9105)
