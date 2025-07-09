# Multiboot on HackberryPi_CM5

⚠️⚠️⚠️
## Note: There are some missing device tree files for RaspberryPi CM5 for the current PINNOS, but I have managed to make multiboot work on the zero version of HackberryPi, so technically just wait for PINN to update the kernel for CM5 and it should work

```Step1``` Download the PINN OS from the pi imager(main folder-> Misc utility images-> [PINN](https://github.com/procount/pinn/tree/master))  
```Step2``` Copy the following content into the config.txt and override  
```Step3``` Insert the TF card into the HackberryPi_CM5 and power it on  

```sh
gpu_mem=16
start_file=start.elf
fixup_file=fixup.dat

disable_overscan=1
initramfs pinn.rfs

dtoverlay=dwc2,dr_mode=host

dtoverlay=pimhyp4:checkonly
overscan_left=0
overscan_right=0 
overscan_top=0
overscan_bottom=0
framebuffer_width=720
enable_dpi_lcd=1
display_default_lcd=1
dpi_group=2
dpi_mode=87
dpi_output_format=0x5f026
dpi_timings=720 0 20 20 40 720 0 15 15 15 0 0 0 60 0 36720000 4

[HDMI1]
hdmi_force_hotplug=1

[pi4]
start_file=start4.elf
fixup_file=fixup4.dat
max_framebuffers=2

[pi5]
kernel=kernel8.img
overlay_prefix=overlays6/
dtoverlay=vc4-kms-v3d
max_framebuffers=2

```

I currently just make it work on the zero version, but the methode should be the same for CM5 version  
![image](https://github.com/user-attachments/assets/40c76bed-a878-4fef-a04c-9f6985bbfede)


So currently the best way to make multiboot is to save one image on the tf card and another on the SSD, and use 
```sh
sudo rpi-eeprom-config --edit
```
to modify  ```BOOT_ORDER=0xf41``` to boot with ```tf card``` first and ```BOOT_ORDER=0xf416``` to boot with ```ssd``` first
![image](https://github.com/user-attachments/assets/0074b639-3ff6-4599-8049-61ce8fa60fcc)
