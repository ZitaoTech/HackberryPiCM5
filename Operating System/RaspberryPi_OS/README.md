# Install RaspberryPi OS on HackberryPi_CM5

### RaspberryPi OS has the most support among other OS for different RaspberryPi SBCs, it is recommended to install RaspberryPi OS on HackberryPi_CM5

Just copy and paste the following command into the ```config.txt``` of [all] section:  

```sh
dtoverlay=vc4-kms-v3d
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```

Insert the tf card into the HackberryPi_CM5 boot it on and after a few reboot you can see the image on the display.


# Add battery status icon and fix shifted pixel

Download and unzip the file ```max17048.rar``` into HackberryPi and let say you unzip all the files into a folder called ```hackberrypicm5``` on desktop

Then open a terminal on this folder and 

```sh
make
```
then
```sh
sudo make install
```

Then the battery status driver and none pixel shifted display driver in installed on the device, then we need to delete the ```dtoverlay=vc4-kms-dpi-hyperpixel4sq``` of ```config.txt``` and add ```dtoverlay=hackberrypicm5```. Then insert the tf card back into the device and we should see the battery status of the device on the taskbar and no more shifted pixel at first col
