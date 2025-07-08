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
![image](https://github.com/user-attachments/assets/c53bd59b-1f58-4ec0-a44a-4ccc6b559dde)

```sh
make
```
then
```sh
sudo make install
```
![image](https://github.com/user-attachments/assets/a22a3c8e-0f1a-40fc-9e09-ead5a17a298c)

Then the battery status driver and none pixel shifted display driver in installed on the device, then we need to delete the ```dtoverlay=vc4-kms-dpi-hyperpixel4sq``` of ```config.txt``` and add ```dtoverlay=hackberrypicm5```. Then insert the tf card back into the device and we should see the battery status of the device on the taskbar and no more shifted pixel at first col
![image](https://github.com/user-attachments/assets/ce9b5ee2-7add-4a49-83c2-6bdfcfc658a1)
