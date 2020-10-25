from pyfiglet import Figlet
import subprocess
import sys
import threading
from client import main_c, main_c2

result = Figlet(font='slant')
print(result.renderText('Worker is Ready'))
counter1 = 1
counter2 = 1
counter3 = 1
while(True):
    print("Choose the task!")
    tasks = ["1. Exchange Rate(1 from_currency to_currency amount)", "2. Get Host(2 domain)", "3. Get Time",
             "4. Check Queue", "5. Check Status Worker"]
    for task in tasks:
        print(task)
    x = input()
    if(x[0] == "1" and len(x) > 1):
        threading.Thread(target=main_c, args=(x, counter1)).start()
        counter1 += 1
    elif(x[0] == "2" and len(x) > 1):
        threading.Thread(target=main_c, args=(x, counter2)).start()
        counter2 += 1
    elif(x == "3"):
        threading.Thread(target=main_c, args=(x, counter3)).start()
        counter3 += 1
    elif(x == "5"):
        threading.Thread(target=main_c2, args=(x,)).start()
    elif(x == "6"):
        threading.Thread(target=main_c2, args=(x,)).start()
    else:
        print("Command is wrong!")
