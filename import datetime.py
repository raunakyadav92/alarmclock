import datetime
import time
from playsound import playsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("⏰ Time to Wake Up!")
            playsound("alarm.mp3")  # Replace with your alarm sound file
            break
        time.sleep(1)

# Example Usage
alarm_time = input("Enter alarm time (HH:MM:SS): ")
set_alarm(alarm_time)
