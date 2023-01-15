import datetime
import time
import os
import subprocess

from pydub import AudioSegment
from pydub.playback import play

# Ask the user for the countdown time
target_time = input("Enter the countdown time in the format of hh:mm (24 hour time): ")

# Get the current date and time
now = datetime.datetime.now()

# Get the target date and time
target = datetime.datetime.strptime(target_time, '%H:%M')
target = target.replace(year=now.year, month=now.month, day=now.day)

# Check if the target time is in the past
if target < now:
    target += datetime.timedelta(days=1)

# Calculate the remaining time

flag_30 = 0
flag_10 = 0
flag_05 = 0
flag_01 = 0
flag_10s = 0
while True:
    
    # Sets flags so sound only fires once

    
    # Get the current time
    now = datetime.datetime.now()
    # Calculate the remaining time
    remaining_time = target - now
    time_left = remaining_time.total_seconds()
    
    if time_left < 0:
        break
    elif time_left < 10:
        if flag_10s == 0:
            print(">>> 10s remaining <<<")
            play(AudioSegment.from_file("10s.mp3"))
            flag_10s = 1

            
    elif time_left < 60:
        if flag_01 == 0:
            flag_01 = 1
            print(">>> 60s remaining <<<")
            play(AudioSegment.from_file("1.mp3"))

        
    elif time_left < 300:
        if flag_05 == 0:
            flag_05 = 1
            print(">>> 5 mins remaining <<<")
            play(AudioSegment.from_file("5.mp3"))

        
    elif time_left < 600:
        if flag_10 == 0:
            flag_10 = 1
            print(">>> 10 mins remaining <<<")
            play(AudioSegment.from_file("10.mp3"))
        
    elif time_left < 1800:
        if flag_30 == 0:
            flag_30 = 1
            print(">>> 30mins remaining <<<")
            play(AudioSegment.from_file("30.mp3"))              
    
    
    
    remaining_time = datetime.timedelta(seconds=int(remaining_time.total_seconds()))
    print("Remaining Time: {}".format(remaining_time))
    time.sleep(1)



print("Countdown finished!")

while True:
    try:
        # Terminate the VRChat process
        subprocess.run(["taskkill", "/F", "/IM", "VRChat.exe"])
    except:
        print("VRChat is not running or error occured")
        time.sleep(5)