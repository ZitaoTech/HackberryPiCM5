# Install different operating system on HackberryPi_CM5

There are many different OS that you can install on HackberryPi_CM5. They are basically those OS that support RaspberryPi5 Serie. 
But note that RaspberryPi5 or BCM2712 is relativly a new chip. Some OS may have not enough support for Pi5 like Kali.  

### On this page, there are many folders that will tell you how to install the driver for this screen on these operating systems.

### If you want to try other OS that is not mentioned in this page. You can try the normal way listed below:

```Step1``` Download the ```vc4-kms-dpi-hyperpixel4sq.dtbo``` and ```hyperpixel4.dtbo``` file in this page  
```Step2``` Put the two files into the ```/overlay/``` folder of the image disk  
```Step3```  Copy and paste the following lines into the ```/boot/config.txt```  
```sh
dtoverlay=vc4-kms-v3d
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```
In this way, you have installed the screen driver on this operating system and invoked it.  
Unless this operating system does not support the Pi 5, it should generally be able to display the image on this screen.

### Also note that the default hardware I2C and SPI gpios are used for the display. So remember to disable them in the OS

# Fix shifted pixel at first col

You might see there is shifted pixel at the first col of the display like this:
![image](https://github.com/user-attachments/assets/87f9b68f-430e-497b-a978-2f8b670889f9)

Here is the solution to fix that:

```Step1``` Download the ```hackberrypi.dtbo``` file in this page   
```Step2``` Put the file into the ```/overlay``` folder of the image disk   
```Step3``` Delete ```dtoverlay=vc4-kms-dpi-hyperpixel4sq``` and paste the following into the ```/boot/config.txt```  
```sh
dtoverlay=hackberrypi
```
