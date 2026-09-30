from validation import get_integer


def pattern_game():
    while True:
        print("\n1. Left Triangle")
        print("2. Right Triangle")
        print("3. Pyramid")
        print("4. Exit")
        pattern = get_integer("Which pattern do you want (1/2/3/4) : ")
        if pattern in (1, 2, 3):
            n = get_integer("What value do you want for n : ")
            if n <= 0:
                print("Please enter a positive value.")
                continue
            for i in range(1, n + 1):
                if pattern == 1:
                    print("*" * i)
                elif pattern == 2:
                    print(" " * (n - i) + "*" * i)
                else:
                    print(" " * (n - i) + "*" * (2 * i - 1))
        elif pattern == 4:
            print("Exiting Pattern Printing Game...")
            break
        else:
            print("Invalid command!!!")
