import os
import time
boot_time = time.time()
print("loading..")
time.sleep(2)
print("-" * 130)
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
        print("\n" * 100)
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
    elif command.startswith("calc"):
        print("This command is still in progress") #TODO: set up "calc" command
    elif command == "shutdown":
        print("Shutting down..")
        time.sleep(2)
        print("-" * 130)
        break
    else:
        print("Command unavailble, 'help' for availble options")
