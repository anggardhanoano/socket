from pyfiglet import Figlet
import subprocess
import sys
import threading
from client import main_c

result = Figlet(font='slant')
print(result.renderText('Simp Angga'))
counter1 = 1
counter2 = 1
counter3 = 1
while(True):
    print("Choose the task!")
    tasks = ["1. Long Task", "2. Medium Task", "3. Short Task", "4. Check Queue", "5. Check Status Worker"]
    for task in tasks:
        print(task)
    x = input()
    if(x == "1"):
        threading.Thread(target = main_c, args=("1", counter1)).start()
        counter1 += 1
    elif(x == "2"):
        threading.Thread(target = main_c, args=("2", counter2)).start()
        counter2 += 1
    elif(x == "3"):
        threading.Thread(target = main_c, args=("3", counter3)).start()
        counter3 += 1
    elif(x == "4"):
        threading.Thread(target = main_c, args=("4")).start()
    elif(x == "5"):
        threading.Thread(target = main_c, args=("5")).start()
    else:
        print("Command is wrong!")
    