# NVME Slot on HackberryPi_CM5

There is an NVME Slot on board which is only compatible with 2242 ssd or hailo 8 AI accelerator card.
![image](https://github.com/user-attachments/assets/70425743-f175-4eb6-a6be-5a03c525eecf)
There are many types of ssd that are not compatible with RaspberryPi, it is recommended to buy the ssd directly from shop of elecrow:


## Use SSD with HackberryPi_CM5

### Enable PCIe
First enable PCIe Interface, note: PCIE interface is enabled on the PI5B by default.
If the PCIE interface is not enabled, you add the following content in "/boot/firmware/config.txt" by typing ```sudo nano /boot/firmware/config.txt``` in a terminal:
```sh
dtparam=pciex1
```
at [all] section

The default mode of PCIe is gen2. If you need to enable PCIe Gen3, you need to add the following content at /boot/firmware/config.txt:
```sh
dtparam=pciex1_gen=3
```
at [all] section

Now the ```config.txt``` file will look like this:  
![image](https://github.com/user-attachments/assets/4eaf41f2-989e-48ca-8308-74255f591d27)

Now make a ```sudo reboot``` and type ```lsblk``` The SSD should be recognized by the Pi:
![image](https://github.com/user-attachments/assets/da639e70-392c-4627-a9c4-45de4356bc23)

### Partition
```sh
sudo fdisk /dev/nvme0n1
```
Execute n to add the partition, and then just type enter enter enter until a new partition is created, and then execute w to save and exit.
![3e1775b2937b64a7e02af512a7da948c](https://github.com/user-attachments/assets/efba3dd9-927c-44ab-b508-64ea986d3372)

### Format
```sh
sudo mkfs.ext4 /dev/nvme0n1p1
```
Wait for a few moments, when done has appeared, it means that the formatting has been carried out.
![1a0374a7-da44-4201-9268-f5ef6763b0c1](https://github.com/user-attachments/assets/59d68cfb-bc9b-4627-8ab2-7d934cb8fa68)

### Mount
Create Mount Directory(Use any name)
```sh
sudo mkdir ssd
```
Mount the device
```sh
sudo mount /dev/nvme0n1p1 ./ssd
```
Checking disk status
```sh
df -h
```
![image](https://github.com/user-attachments/assets/05d913d4-3291-43b4-b47a-c9829f42b60f)

## Read/Write Test
Enter the directory where the disk is mounted:
```sh
cd ssd
```
Write test
```sh
sudo dd if=/dev/zero of=./test_write count=2000 bs=1024k
```
Read Test
```sh
sudo dd if=./test_write of=/dev/null count=2000 bs=1024k
```
Note: Different cards and environments make different test results. As the Raspberry Pi is more vulnerable to being affected, if you want to test the exact performance, you can use a PC to test.
![image](https://github.com/user-attachments/assets/6898ba8f-9f83-42ca-b039-fdb53ec3016c)

## Auto-Mounting
If the testing is sound and you don't need it as a system disk and only use an extended disk, you can set up an automatic mounting.
```sh
sudo nano /etc/fstab
```
#Add the following content at the end:
```sh
/dev/nvme0n1p1  /home/pi/ssd  ext4  defaults  0  0
```
#/dev/nvme0n1p1 is the device name, /home/pi/ssd is the directory to be mounted, ext4 is the file system type, defaults are using the default mounting setting  
Make the modification take effect (make sure the test is sound before rebooting, otherwise it will lead to failure to mount or boot; if it cannot boot, you can remove the content added in /etc/fstab)
```sh
sudo mount -a
```
You should see an external disk on the desktop after reboot

## Booting from NVMe SSD
Open Menu->Accessories->SD card Copier.  
![image](https://github.com/user-attachments/assets/7ccde86f-81f4-400d-90f2-17856608acf7)  
Copy the image from SD card to SSD:  
![image](https://github.com/user-attachments/assets/c34ebdf6-002e-4a6a-beb8-bac9ac4a08d4)  
Wait a few moment until the copying is finished.  
![image](https://github.com/user-attachments/assets/01d3ec06-4dac-4cd3-84e6-d3568cfc96b1)  


Then
```sh
sudo rpi-eeprom-config --edit
```
Modify BOOT_ORDER=0xf41 as BOOT_ORDER=0xf416  
![image](https://github.com/user-attachments/assets/d105ebac-e58d-4332-8f2d-8bdc8c2243dd)


Remove the tf card and reboot the HackberryPi then the system should be rebooted from the SSD, it's about 10 seconds faster than booting from tf card(RaspberryPi OS)


