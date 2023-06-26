import serial
import time

# Change the following line to your serial port name
ser = serial.Serial('/dev/tty.usbmodem11302', 115200) # micro:bit v2's default baud rate is 115200

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print(line)
        time.sleep(0.1)
