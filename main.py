import os
import time
def loopequation():
    equation_array = []
    scan = True
    num = "" 
    for x in equation:
        if x.isdigit():
            scan = True
            num += x
        else:
            if scan:
                num = int(num)
                equation_array.append(num)
                num = ""
            scan = False
    num = int(num)
    equation_array.append(num)
    result = 0
    x = 0
    for x in equation_array:
        result += x
    print(result)
    

print("loading..")
time.sleep(1)
print("-" * 50)
boot_time = time.time()
print("Welcome to KOS (Python Edition)")
print("Enter 'help' for options")

while True:
    command = input("KOS> ")
    if command == "help":
        print("Available commands: help, shutdown, echo (text), time, date, info, clear, uptime")
    elif command.startswith("echo "):
        print(command[5:])
    elif command == "time":
        print(time.strftime("%I:%M:%S %p"))
    elif command == "date":
        print(time.strftime("%A, %B %d %Y"))
    elif command == "info":
        print("kOS, version 0.2, author: Khattab")
    elif command == "clear":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    elif command == "uptime":
        seconds = int(time.time() - boot_time)
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours > 0:
            print(f"The OS ran for {hours}h {minutes}m {seconds}s")
        elif minutes > 0:
            print(f"The OS ran for {minutes}m {seconds}s")
        else:
            print(f"The OS ran for {seconds}s")
    elif command.startswith("calc "):
        equation = command[5:]
        loopequation()
    elif command == "shutdown":
        print("Shutting down..")
        time.sleep(1)
        print("-" * 50)
        break
    else:
        print("Command unavailble, `help` for availble options")