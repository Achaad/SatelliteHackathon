from src.track_and_move import Tracker
import serial

def user_commands():
    command = None
    print("\'a\' for antenna azimuth")
    print("\'e\' for antenna elevation")
    print("\'s\' for satellite position\n")
    # TODO: create stop command
    while not command:
        command = input("Please enter a command: ").lower()
        if command != 'e' and command != 'a' and command != 's':
            command = None
            print("Wrong command!\n")

    return command

def public_void_static_main():

    tle_path = None

    # Asks for tle file path
    while not tle_path:
        tle_path = input("Please enter tle absolute path: ")
        try:
            f = open(tle_path).close()
        except Exception as error:
            tle_path = None
            print("No file found!")

    port = None
    while not port:
        port = input("Please enter port number: ")
        if "COM" not in port:
            port = "COM" + port

        try:
            serial.Serial(port, 9600).close()
        except Exception as error:
            port = None
            print("Wrong com port!")

    tracker = Tracker(port, tle_path)
    # tracker.run_program() #TODO: put into thread

    user_command = user_commands()

    # TODO: create while loop
    if user_command == 'a':
        print("here", tracker.get_azimuth())
    elif user_command == 'e':
        print(tracker.get_elevation())
    elif user_command == 's':
        print(tracker.get_signal())



if __name__ == "__main__":
    public_void_static_main()