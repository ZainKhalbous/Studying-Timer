"""Timer with sound"""
#timer
from playsound import playsound as play
import time
import random 

def set_time(n):
    timer=n.split(":")
    seconds=int(timer[0])*3600+int(timer[1])*60+int(timer[2])
    return seconds
def display_time(s):
            
    for i in range(s,-1,-1):
        second=i%60
        minute=(i//60)%60
        hour=(i//3600)%3600
        print(f"{hour:02}:{minute:02}:{second:02}")
        time.sleep(1)
        if i==0:
            return

def break_time(s):
    s=int(s*0.20)
    for i in range(s,0,-1):
        second=i%60
        minute=(i//60)%60
        hour=(i//3600)%3600
        print(f"{hour:02}:{minute:02}:{second:02}")
        time.sleep(1)
    
        
def break_activity():
    activities=["Stretch","Play Chess","Make a Drink", "Breath", "Read a Book","Draw Something"]
    return random.choice(activities)

#sound

def sound():
    
    message="""
    1-Rain 1 hour
    2-Quraan 30 minutes
    3-Nature 3 hours
    4-Quit
    """
    print(message)
    
    choice=int(input("Enter: "))
    
    if choice==1:
        print("Work Time!")
        play("c:\\Users\\zaink\\Downloads\\rain.mp3")

        times_up()
        return
    elif choice==2:
        print("Work Time!")
        play("c:\\Users\\zaink\\Downloads\\quraan.mp3")     

        times_up()
        return
    elif choice==3:
        print("Work Time!")
        play("c:\\Users\\zaink\\Downloads\\nature.mp3")

        times_up()
        return   
    elif choice==4:
        return
    else:
        print("Enter valid number")
    
def times_up():
    play("C:\\Users\\zaink\\Downloads\\timeup.mp3")




"""CODE"""
t=True
while t:
    print("1-setup timer\n2-fixed timer\n3-Quit")
    user=int(input("Enter: "))
    
    if user==1:
        time_user=input("Enter: ")
        print("Work Time!")
        # sound(time_user)
        display_time(set_time(time_user))
        times_up()
        
        break_user=input("Do you want to take a break? Yes No ").lower()
        
        if break_user=="yes":
            print("Break Time!")
            print(f"You can {break_activity()}")
            time.sleep(5)
            break_time(set_time(time_user))
            times_up()
  
    elif user==2:
        
        sound()
        
    elif user==3:
        break
    
    else:
        print("Not valid")


2
    
    
