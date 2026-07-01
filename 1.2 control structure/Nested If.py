age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")


if age >= 18:

    if citizen.lower() == "yes":
        print("You can vote")

    else:
        print("Not a citizen")

else:
    print("Too young")