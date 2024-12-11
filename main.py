import calendar
import datetime


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
print(timeSlots)

timeInput = None
description = None




def addNewEvent(slots, timeInput, description):
        timeInput = input("\nEnter the time slot you want to add something to. (e.g., 05:00 PM:): ")
        if timeInput in timeSlots and timeSlots[timeInput] is not "":
            print(f"Sorry, the time slot {timeInput} is already booked for: {timeSlots[timeInput]}")
        else:
            description = input("Enter the description for the selected time slot: ")
            timeSlots[timeInput] = description
            print(f"Description for {timeInput} updated to: {description}")
        

            


def deleteEvent(slots, timeInput):
    timeInput = input("\nEnter time slot you want to delete. (e.g., 05:00 PM: )")
    if timeInput in slots:
        slots[timeInput] = None
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

