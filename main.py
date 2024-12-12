import calendar
import datetime
import re


def createTimeSlots(startTime, endTime, intervalMinutes):
    currentTime = startTime
    slots = {}

    while currentTime <= endTime:
        slots[currentTime.strftime('%I:%M %p')] = ""

        currentTime += datetime.timedelta(minutes=intervalMinutes)

    return slots


startTime = datetime.datetime.strptime("00:00", "%H:%M")
endTime = datetime.datetime.strptime("23:59", "%H:%M")
intervalMinutes = 60

timeSlots = createTimeSlots(startTime, endTime, intervalMinutes)

timeInput = None
description = None

timeInputPattern = r"^([0][1-9]|1[0-2]):([0][0]\s([AP][M])$)"



def addNewEvent(timeSlots, timeInput, description):
        while True:
            timeInput = input("\nEnter the time slot you want to add something to. (e.g., 05:00 PM:): ")
            if re.match(timeInputPattern, timeInput):
                break
            else: 
                print("Invalid time format. Please enter the time again")
        

        if timeInput in timeSlots and timeSlots[timeInput] != "":
            return overwrite(timeInput, description)
        else:
            description = input("Enter the description for the selected time slot: ")
            timeSlots[timeInput] = description
            print(f"Description for {timeInput} updated to: {description}")


def overwrite(timeInput, description):
    overwrite = input(f"Sorry, the time slot {timeInput} is already booked for: {timeSlots[timeInput]} \nWould you like to overwrite the current event? Y/N ")
    if overwrite == str("Y") or overwrite == str("y"):
        description = input("Enter the new event description: ")
        timeSlots[timeInput] = description
    else:
        print("Event not added. Please try a new time block")
        

            


def deleteEvent(slots, timeInput):
    timeInput = input("\nEnter time slot you want to delete. (e.g., 05:00 PM: )")
    if timeInput in slots:
        timeSlots[timeInput] = None
        print(f"Descriptions for time {timeInput} has been deleted!")
    else:
        print(f"Not a valid time slot")




addNewEvent(timeSlots, timeInput, description)

print("Updated time slots: ")

for time, event in timeSlots.items():
    if event:
        print(f"{time}: {event}")
    else:
        print(f"{time}")

addNewEvent(timeSlots, timeInput, description)

print("Updated time slots: ")

for time, event in timeSlots.items():
    if event:
        print(f"{time}: {event}")
    else:
        print(f"{time}")

