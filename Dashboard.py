command = ""
started=False
while command != "quit":
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started=True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started=False
            print("Car stopped")
    elif command == "help":
        print('''
Start -  to start the car
Stop - to stop the car
Quit - to exit
    ''')
    elif command == "quit":
        break
    else:
        print("I don't understand!")