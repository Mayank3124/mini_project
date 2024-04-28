start = int(input("Enter the starting point: "))
end = int(input("Enter the end point: "))
update = int(input("Enter the update value: "))

choice = input("Enter your choice for forward or reverse printing: ")
choice2 = input("Enter your choice for row or column printing: ")

if choice == "forward":
    if choice2 == "row":
        for i in range(start, end, update):
            print(i, end=', ')
    elif choice2 == "column":
        for i in range(start, end, update):
            print(i)
    else:
        print("Invalid choice for the second option. Please enter a valid choice.")
elif choice == "reverse":
    if choice2 == "row":
        for i in range(end, start - 1, -update):
            print(i, end=', ')
    elif choice2 == "column":
        for i in range(end, start - 1, -update):
            print(i)
    else:
        print("Invalid choice for the second option. Please enter a valid choice.")
else:
    print("Both choices are invalid.")
