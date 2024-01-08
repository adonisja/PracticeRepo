print("This function uses a 24hr clock")
current_time = int(input("Enter the current time: (hrs)"))
waiting_time = int(input("How many hours before your alarm rings? (hrs)"))
hours = current_time + waiting_time
if hours > 24:
    time = hours % 24   
else:
    time = hours
twelveHourClock = time % 12  
print(f"Current time = {current_time}")
print(f"Your alarm will ring at {time}:00", end = "")
print(f" or {twelveHourClock} {'AM' if time <= 12 else 'PM'}")