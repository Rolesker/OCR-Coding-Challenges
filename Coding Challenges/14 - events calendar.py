import json
import time

"""
structure of events: dictionary uses dates as keys. inputs are an array of size
3, arr[0] is the start time, arr[1] is the end time, arr[2] is the title 
"""
running=True
calendar={}
calendar_file=open("14-calendar.txt","rb")
calendar=json.load(calendar_file)
calendar_file.close()


def add_event():
    datestr=input("Enter the date of the event in the format dd/mm/yyyy ")
    concat=""
    for i in datestr.split("/")[::-1]:
        concat+=i
    key=int(concat)
    eventnum=0
    if key not in calendar.keys():     
        calendar[key]=[]
    else:
        eventnum=len(calendar[key])
    title=input("Enter the title/detail for this event ")
    start_time=input("Enter the start time in 24 hour format (hh:mm) ")
    end_time=input("Enter the end time in 24 hour format (hh:mm) ")
    calendar[key].append([start_time,end_time,title])
    print()
    print("Event created:")
    print(calendar[key][eventnum][2]+", from "+calendar[key][eventnum][0]+" - "+calendar[key][eventnum][1])
    save_changes()
    
def remove_event():
    pass

def display_events():
    print()
    sorted_calendar=dict(sorted(calendar.items()))
    for i in sorted_calendar.keys():
        keystr=str(i)
        date=keystr[6:8]+"/"+keystr[4:6]+"/"+keystr[0:4]
        print(date+":")
        for j in sorted_calendar[i]:
            print(j[2]+", from "+j[0]+" - "+j[1])
        print()
    

def save_changes():
    calendar_file=open("14-calendar.txt","w")
    calendar=json.dump(globals()["calendar"],calendar_file)
    calendar_file.close()

def clear_calendar():
    calendar={}
    save_changes()

while running:
    print("-----------MAIN-MENU-----------")
    print("Select an option below")
    print("1) Add event")
    print("2) Remove event")
    print("3) Display events")
    print("4) Clear calendar")
    print("5) Exit and save changes")
    choice=0
    while not 1<=choice<=5:
        choice=int(input())
    print()
    if choice==1:
        add_event()
    elif choice==2:
        pass
    elif choice==3:
        display_events()
    elif choice==4:
        choice=input("Press Y if you are really sure. ")
        if choice=="Y":
            clear_calendar()
    elif choice==5:
        save_changes()
        print("Bye!")
        time.sleep(1)
        running=False
    print()
