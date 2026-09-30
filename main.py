from menu import display_menu
from pattern_game import pattern_game
from calculator import calculator


def main():
    name = input("What is your name : ")
    print("Welcome to Farhaan's Device System :", name)
    interface = "on"
    while interface == "on":
        app = display_menu()
        if app == 1:
            pattern_game()
        elif app == 2:
            calculator()
        elif app == 3:
            print("Bye", name)
            interface = "off"
        else:
            print("Invalid command!!!")


if __name__ == "__main__":
    main()
