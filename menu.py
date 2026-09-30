from validation import get_integer


def display_menu():
    print("\n1. Pattern Printing Game")
    print("2. Calculator")
    print("3. Switch off")
    return get_integer("Which app do you want (1/2/3) : ")
