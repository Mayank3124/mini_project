inventory = {}

while True:
    action = input("What would you like to do? (add, remove, display, quit): ")

    if action == 'add':
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
    
    elif action == 'remove':
        item = input("Enter the name of the item you want to remove: ")
        quantity = int(input("Enter the quantity you want to remove: "))
        if item in inventory and inventory[item] >= quantity:
            inventory[item] -= quantity
        elif item in inventory and inventory[item] < quantity:
            print(f"There are only {inventory[item]} left of {item} in inventory.")
        else:
            print("There is no such item in inventory.")
    
    elif action == 'display':
        print("Inventory:")
        for key, value in inventory.items():
            print(f"{key}: {value}")
    
    elif action == 'quit':
        break
    
    else:
        print("Invalid entry. Please try again.")
    elif action =='quit':
        break
    else:
        print("invalid entry please try again. ")
