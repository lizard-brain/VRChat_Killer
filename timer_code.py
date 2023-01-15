import datetime
import time

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
while True:
    # Get the current time
    now = datetime.datetime.now()
    # Calculate the remaining time
    remaining_time = target - now
    if remaining_time.total_seconds() < 0:
        break
    print("Remaining Time: {}".format(remaining_time))
    time.sleep(1)

print("Countdown finished!")
