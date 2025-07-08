# Install Kali on HackberryPi_CM5

### Kali Linux is a Linux distribution designed for digital forensics and penetration testing. It is maintained and funded by Offensive Security.

```Step1```Download and install the kali image from pi imager into a tf card```Main Menu-> other specfic purpose os->kali linux```  
```Step2``` Copy the following content into the config.txt and override  
```Step3``` Insert the TF card into the HackberryPi_CM5 and power it on, wait a few seconds and you can see it booting  

Compared with other operating system, it's just needed to delete the vms, because the .... is currently not likely to be supported in kali os.


```sh
# http://rptl.io/configtxt
# Some settings may impact device functionality. See link above for details

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

# Additional overlays and parameters are documented
# /boot/firmware/overlays/README

# Automatically load overlays for detected cameras
camera_auto_detect=1

# Automatically load overlays for detected DSI displays
display_auto_detect=1

# Automatically load initramfs files, if found
auto_initramfs=1

# Enable DRM VC4 V3D driver
#dtoverlay=vc4-kms-v3d
#max_framebuffers=2
# Don't have the firmware create an initial video= setting in cmdline.txt.
# Use the kernel's default instead.
disable_fw_kms_setup=1

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
dtoverlay=vc4-kms-dpi-hyperpixel4sq


```

![image](https://github.com/user-attachments/assets/7e2cc7c9-229a-4705-bc1a-f41f50b99973)

⚠️ **Note:**  

Bluetooth may not be enabled by default in Kali on current version of Kali. You need to enable it manually, here are the steps:

```sh
sudo apt install blueman
```
and then
```sh
sudo systemctl enable bluetooth.service
```
Then you can connect with the speakers and use bluetooth on HackberryPi_CM5 in Kali
