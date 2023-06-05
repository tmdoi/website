from microbit import *
import time

temperature_readings = []
sum = 0

def average_temperature():
    return sum / len(temperature_readings) if temperature_readings else "N/A"

while True:
    time.sleep(1)  # wait for 1 second

    current_temperature = temperature()
    
    if len(temperature_readings) == 5:
        # remove the oldest reading if we already have 5 readings
        removed_temperature = temperature_readings.pop(0)
        sum -= removed_temperature

    temperature_readings.append(current_temperature)
    sum += current_temperature

    if button_a.is_pressed():
        display.scroll(average_temperature())
