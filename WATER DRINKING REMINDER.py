import time
import win11toast

def water_drinking_reminder():
    for i in range (5):
        print(f"Reminder {i+1}")
        win11toast.toast("PLEASE DRINK WATER💧!!!!!!")
        time.sleep(18000)


water_drinking_reminder()
