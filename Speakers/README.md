# Speakers on HackberryPi_CM5

As we know, it's always been somehow difficult or tricky to add sound for RaspberryPi. Some use gpio to generate pwm to make sound for speakers, some use I2S audio module to generate sound for speakers. But they all have some shortcomings. PWM generated from gpios on raspberryPi have much noise that make the speakers nealy usable, and I2S audio module will occupy the very precious gpio resoureces(usually take 3 gpio pins). And in some operating system there is no driver for these pwm or I2S audio module. Due to the reasons above this is how I solve the sound problem.

## Bluetooth speakers on board

This is how I add sound on HackberryPi_CM5: Integrating a bluetooth speaker on board.  


**Advantages**:  


**No gpio needed**: The SBC communicates with the audio module via bluetooth so there is no gpio needed.  
**Driverless**: As long as your operating system installed have bluetooth driver, you can pair with the speaker and no external driver needed.  
**Good sound quality**: As long as the power source for the bluetooth audio module clear is, the sound quality is good.  
**Cheap cost**: compared with some USB solution, the bluetooth audio module is moch more cheaper.  


The solution is bluetooth audio module + Stereo Speaker amplifier  
![image](https://github.com/user-attachments/assets/fa1b662a-e1b8-4add-a23a-1842e9664163)  
The bluetooth audio module is very easy to source, it's called MH-M18.  
![d8e22f566b35eec8c523338b65ded325](https://github.com/user-attachments/assets/870e180d-ea77-4786-b0f6-767c084fa577)  
The amplifier is a very classic type called PAM8406.  
![image](https://github.com/user-attachments/assets/2b6e1704-28a0-40e7-b78f-e65098a3e902)  

# Speakers

There are two types of speakers used on HackberryPi_CM5. 1507 speaker for Q20 version and 1511 speaker for Q10 and 9900 version. They are both 8Ω speakers and have difference at the dimension. You can find the datasheet about the speakers in this page.

# Layout

Because the speaker used is just pure speaker and it has no sound cavity. I glue the speaker on the PCB and make a hole on the PCB so that the sound from the speaker can spread to the internal case and that a good cavity, from my test, after making a hole on the PCB the sound quality can get much better. The image below shows the outline(green line) of the speaker and the hole(pink line) made for the sound.  
![image](https://github.com/user-attachments/assets/4c991658-1e0e-4ed0-9fd1-6774af63f9e0)

# Pair with the speakers

After you turn on the device, you can hear sound from the speaker. But you need to manually pair with the speaker in different operating system, here are the steps:

### 1. First enable bluetooth on the pi.

### 2. Search device, you can find a device called XWF-M18-M28-M38, pair with it
![image](https://github.com/user-attachments/assets/a884615d-52f5-4f09-9425-45c1b4422a0e)

### 3. After you pair with it successfully, connect it
![image](https://github.com/user-attachments/assets/cdf1a293-7707-4bea-939b-78946b123b34)

### 4. To control the volume, right-click the volume icon in the system tray and select the speakers. You can now use the volume control by (left-)clicking on the speaker icon. 
