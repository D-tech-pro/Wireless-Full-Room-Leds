from PIL import ImageGrab
import socket
import csv
import struct
import datetime
import time
import numpy as n

###############################################################################
############### Please Enter Your Wi-Fi Module's IP Address ###################
###############################################################################

IP_Address = '192.168.1.191'

class MagicHomeApi:
    """Representation of a MagicHome device."""

    def __init__(self, device_ip, device_type, keep_alive=True):
        """"Initialize a device."""
        self.device_ip = device_ip
        self.device_type = device_type
        self.API_PORT = 5577
        self.latest_connection = datetime.datetime.now()
        self.keep_alive = keep_alive
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(3)
        try:
            print("Establishing connection with the device.")
            self.s.connect((self.device_ip, self.API_PORT))
        except socket.error as exc:
            print("Caught exception socket.error : %s" % exc)
            if self.s:
                self.s.close()

    def turn_on(self):
        """Turn a device on."""
        self.send_bytes(0x71, 0x23, 0x0F, 0xA3) if self.device_type < 4 else self.send_bytes(0xCC, 0x23, 0x33)

    def turn_off(self):
        """Turn a device off."""
        self.send_bytes(0x71, 0x24, 0x0F, 0xA4) if self.device_type < 4 else self.send_bytes(0xCC, 0x24, 0x33)

    def get_status(self):
        """Get the current status of a device."""
        if self.device_type == 2:
            self.send_bytes(0x81, 0x8A, 0x8B, 0x96)
            return self.s.recv(15)
        else:
            self.send_bytes(0x81, 0x8A, 0x8B, 0x96)
            return self.s.recv(14)

    def update_device(self, r=0, g=0, b=0, white1=None, white2=None):
        """Updates a device based upon what we're sending to it.

        Values are excepted as integers between 0-255.
        Whites can have a value of None.
        """
        # Update an RGB or an RGB + WW device

        message = [0x31, r, g, b, 0, 0x00, 0x0f]
        self.send_bytes(*(message+[self.calculate_checksum(message)]))

    def check_number_range(self, number):
        """Check if the given number is in the allowed range."""
        if number < 0:
            return 0
        elif number > 255:
            return 255
        else:
            return number

    def send_preset_function(self, preset_number, speed):
        """Send a preset command to a device."""
        # Presets can range from 0x25 (int 37) to 0x38 (int 56)
        if preset_number < 37:
            preset_number = 37
        if preset_number > 56:
            preset_number = 56
        if speed < 0:
            speed = 0
        if speed > 100:
            speed = 100

        if type == 4:
            self.send_bytes(0xBB, preset_number, speed, 0x44)
        else:
            message = [0x61, preset_number, speed, 0x0F]
            self.send_bytes(*(message+[self.calculate_checksum(message)]))

    def calculate_checksum(self, bytes):
        """Calculate the checksum from an array of bytes."""
        return sum(bytes) & 0xFF

    def send_bytes(self, *bytes):
        """Send commands to the device.

        If the device hasn't been communicated to in 5 minutes, reestablish the
        connection.
        """
        check_connection_time = (datetime.datetime.now() -
                                 self.latest_connection).total_seconds()
        try:
            if check_connection_time >= 290:
                print("Connection timed out, reestablishing.")
                self.s.connect((self.device_ip, self.API_PORT))
            message_length = len(bytes)
            self.s.send(struct.pack("B"*message_length, *bytes))
            # Close the connection unless requested not to
            if self.keep_alive is False:
                self.s.close
        except socket.error as exc:
            print("Caught exception socket.error : %s" % exc)
            if self.s:
                self.s.close()
    

weights = [1.2, 0.9, 0.8]

while(True):


    screen = ImageGrab.grab().resize([160,90])
    sBox = screen.resize([1, 1],ImageGrab.Image.BOX)
    colors = sBox.load()[0,0]
    
    send = []

    for i in range(3):
        send.append(colors[i] * weights[i])
        send[i] = int(min(send[i],255))

    controller1 = MagicHomeApi(IP_Address, 0)


    cR = int(send[0])
    cG = int(send[1])
    cB = int(send[2])

    controller1.update_device(cR, cG, cB)

    time.sleep(.2)

    
