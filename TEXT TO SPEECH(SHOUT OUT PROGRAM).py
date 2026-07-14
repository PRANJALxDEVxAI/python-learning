import pyttsx3
import time

people = [
    "Rahul",
    "Priya",
    "Aman",
    "Sneha",
    "Vikram",
    "Ananya",
    "Rohit",
    "Kavya",
    "Arjun",
    "Divya",
    "Karan",
    "Isha",
    "Siddharth",
    "Meera",
    "Aditya",
    "Pooja",
    "Nikhil",
    "Riya",
    "Varun",
    "Simran",
    "Harsh",
    "Neha",
    "Yash",
    "Tanya",
    "Abhishek",
    "Shreya",
    "Manish",
    "Kritika",
    "Rajat",
    "Anjali"
]
for person in people:
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    message = f"Shout out to {person}!"
    print(message)
    engine.say(message)
    engine.runAndWait()
    engine.stop()
    del engine
    time.sleep(1)