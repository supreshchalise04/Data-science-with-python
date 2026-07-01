while True:

    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Age cannot be negative")

        else:
            print("Valid age:", age)
            break

    except ValueError:
        print("Enter numbers only")