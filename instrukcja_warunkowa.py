"""
Instrukcję warunkową wykorzystujemy, gdy chcemy wykonać kod, ale tylko pod jakimś warunkiem
"""
def main():
    print("What is your age?")
    age = int(input())
    if age >= 21:
        print("You can drink alcohol and have a gun")
    elif age >= 18:
        print("You can drink alcohol")
    else:
        print("You can\'t drink alcohol and can\'t have a gun")


if __name__ == "__main__":
    main()