# Wireless Full Room Leds

Guys, I am making this to make things easier on how to do the full room responsive LED things that I have done for your PC. 

## Hardware:

Although I have listed the links I have used out for you, this does not mean taht you have to buy these exact ones. 
  
- [RBG LED Strips](https://www.amazon.com/dp/B086VYGP6D/ref=cm_sw_r_cp_apa_i_m0.9Eb2KF3128) - How ever many feet you want but this is what I used. They are honestly all the same cheap LEDs. 
- [Wi-Fi module](https://www.amazon.com/dp/B07116SX41/ref=cm_sw_r_cp_apa_i_B7.9Eb5CHZ7J4) - Wi-Fi module that connects to the Magic-home API
- Optional: [Corner Clips for LED Strips](https://www.amazon.com/dp/B011BD2B5Q/ref=cm_sw_r_cp_apa_i_40.9EbR5T6AGH) - For cutting the strips at corners and putting strips together with their clips. 

Prerequisites:
- Python version: [3.8.3](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)

## Python Dependencies

PC:

- Install Numpy: 
`python -m pip install numpy`

- Install Pillow:
`python -m pip install pillow`

Mac:

- Install Numpy: 
`python3 -m pip install numpy`

- Install Pillow:
`python3 -m pip install pillow`

Remember While Script is running it will override all other platforms while running. 

Test Video for colors (not mine
): [Link](https://www.youtube.com/watch?v=PMtNRXu3z54)

## Script Modifications

To make this work with your Wi-Fi Lights, there is one change to the script you have to make, You have to change the IP_Address Variable to your string lights.

`IP_Address = '192.168.1.191'`

Then save the file, run and test. 

#### Bonus Shortcut Tutorial

- Create a Text File called LEDs.bat
- Populate this text file with

PC: `python "/path/to/WirelessFullRoomLEDsbyD.py"`

Mac: `python3 "/path/to/WirelessFullRoomLEDsbyD.py"`
- Double click to run

#### To run on start up:
- Find your "LEDs.bat"
- Drop this file into `C:\Users\{Username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
- Reboot

Credits:
- [@adamkempenich/magichome-python script](https://github.com/adamkempenich/magichome-python) for interfacing with the wi-fi module
- [alsa9709's Responsive LED Project](https://www.instructables.com/id/Responsive-LED-Backlight-With-Arduino-and-Python/) for caputing the screen down to a color
