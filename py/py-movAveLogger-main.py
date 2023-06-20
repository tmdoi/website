from microbit import *

temperature_log = []
light_level_log = []
start_time = running_time()

while True:
    while running_time() - start_time < 30000:  # Note: running_time returns milliseconds
        current_temperature = temperature()
        current_light_level = display.read_light_level()
        
        # Keep only the last 10 values for moving average
        if len(temperature_log) >= 10:
            temperature_log.pop(0)
        if len(light_level_log) >= 10:
            light_level_log.pop(0)
        
        # Add new values
        temperature_log.append(current_temperature)
        light_level_log.append(current_light_level)
        
        # Calculate and print moving averages if we have enough data
        if len(temperature_log) >= 10 and len(light_level_log) >= 10:
            temperature_avg = sum(temperature_log) / len(temperature_log)
            light_level_avg = sum(light_level_log) / len(light_level_log)
            
            # Print the moving averages
            print("Time:", running_time() - start_time)
            print("Temperature Avg:", temperature_avg)
            print("Light Level Avg:", light_level_avg)
        
        sleep(100)  # Pause for 0.1 seconds
