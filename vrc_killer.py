import time
import datetime
import subprocess
import os

# Get the target time from the user in 24-hour format (HH:MM)
target_time = input("Enter the target time in 24-hour format (HH:MM): ")

# Convert the target time to a datetime object
target_time = datetime.datetime.strptime(target_time, "%H:%M")

# Get the current time
current_time = datetime.datetime.now()

# Calculate the time difference between the target time and the current time
time_diff = target_time - current_time

# Get the total number of seconds in the time difference
total_seconds = int(time_diff.total_seconds())

# Loop until the target time is reached
while total_seconds > 0:
    # Output the remaining time in hours and minutes
    print(f"Time remaining: {int(total_seconds / 3600)} hours, {int((total_seconds % 3600) / 60)} minutes")
    
    # Check if 30 minutes, 10 minutes, 5 minutes, 1 minute, or 10 seconds remaining
    if total_seconds == 1800:
        os.system("afplay 30.wav")
    elif total_seconds == 600:
        os.system("afplay 10.wav")
    elif total_seconds == 300:
        os.system("afplay 5.wav")
    elif total_seconds == 60:
        os.system("afplay 1.wav")
    elif total_seconds == 10:
        os.system("afplay 10s.wav")
    
    # Sleep for 1 second
    time.sleep(1)
    
    # Update the current time
    current_time = datetime.datetime.now()
    
    # Update the time difference
    time_diff = target_time - current_time
    
    # Update the total number of seconds
    total_seconds = int(time_diff.total_seconds())

# Terminate the VRChat process
#subprocess.run(["pkill", "-f", "VRChat"])
subprocess.run(["taskkill", "/F", "/IM", "VRChat.exe"])
#os.system("pkill VRChat")
