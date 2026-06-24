import time
def tame():
    time_hours = int(time.strftime("%H"))
    time_minutes = int(time.strftime("%M"))
    time_seconds = int(time.strftime("%S"))
    return time_hours , time_minutes , time_seconds

def main():
    timing = tame()
    print("Current Time: " , timing[0] , ":" , timing[1] , ":" , timing[2])
    Hours = int(time.strftime("%H"))
    if (Hours > 12):
        print("Good Afternoon")
    elif (Hours <=12):
        print("Good Morning")
    elif (Hours >=5):
        print("Good Evening")
    elif (Hours >=9):
        print("Good Night")
    else:
        print("Good Day")
main()