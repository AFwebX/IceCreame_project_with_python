import time

print("""██╗ ██████╗███████╗     ██████╗██████╗ ███████╗ █████╗ ███╗   ███╗
██║██╔════╝██╔════╝    ██╔════╝██╔══██╗██╔════╝██╔══██╗████╗ ████║
██║██║     █████╗      ██║     ██████╔╝█████╗  ███████║██╔████╔██║
██║██║     ██╔══╝      ██║     ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║
██║╚██████╗███████╗    ╚██████╗██║  ██║███████╗██║  ██║██║ ╚═╝ ██║
╚═╝ ╚═════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝

██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ 
██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗
██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║
██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║
╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝""")

print("Welcome to the Best Ice Cream Parlor in Town!")

list_of_iceCream_flavors = {
    1:{
        "flavor": "Vanilla",
        "price": 2.50
    },
    
    2:{"flavor": "Chocolate",
        "price": 3.00
    },
    3:{
        "flavor": "Strawberry",
        "price": 2.75
    },
    4:{
        "flavor": "Mint Chip",
        "price": 3.25
    },
    5:{
        "flavor": "Butter Pecan",
        "price": 3.50
    },
    6:{
        "flavor": "Rocky Road",
        "price": 3.75
    },
    7:{
        "flavor": "Pistachio",
        "price": 3.00
    }
}

total_price_of_ice_cream = 0 # global variable to assign the cost of ice cream
def Ice_cream_Order():
    global total_price_of_ice_cream
    print("Here are the available ice cream flavors:")
    for key, value in list_of_iceCream_flavors.items():
        print(f"{key}. {value['flavor']} - ${value['price']:.2f}")

    user_input_ = int(input("Enter the corresponding number to choose your ice cream: "))

    while user_input_ not in list_of_iceCream_flavors:
        print("Invalid input. Please enter a valid number corresponding to the ice cream flavor.\n")
        for key, value in list_of_iceCream_flavors.items():
            print(f"{key}. {value['flavor']} - ${value['price']:.2f}")
        user_input_ = int(input("Enter the corresponding number to choose your ice cream :"))
        if user_input_ in list_of_iceCream_flavors:
            print(f"You have selected {list_of_iceCream_flavors[user_input_]['flavor']} flavor - ${list_of_iceCream_flavors[user_input_]['price']:.2f}\n")
    total_price_of_ice_cream += list_of_iceCream_flavors[user_input_]['price']
    print(f"Your current total is: ${total_price_of_ice_cream:.2f}\n")

    Chocolate_syrup = input("Would you like to add chocolate syrup? (y/n)  -- 0.25$ ").lower()
    while Chocolate_syrup not in ["y", "n"]:
        print("Please enter 'y' for yes or 'n' for no.\n")
        Chocolate_syrup = input("Would you like to add chocolate syrup? (y/n)  -- 0.25$ ").lower()
    if Chocolate_syrup == "y":
        print("Adding chocolate syrup to your ice cream!\n")
        total_price_of_ice_cream += 0.25
    else:
        print("No chocolate syrup will be added to your ice cream.\n")

    Sprinkles = input("Would you like to add sprinkles? (y/n)  -- 0.10$ ").lower()
    while Sprinkles not in ["y", "n"]:
        print("Please enter 'y' for yes or 'n' for no.\n")
        Sprinkles = input("Would you like to add sprinkles? (y/n)  -- 0.10$ ").lower()
    if Sprinkles == "y":
        print("Adding sprinkles to your ice cream!\n")
        total_price_of_ice_cream += 0.10
    else:
        print("No sprinkles will be added to your ice cream.\n")

    Nuts = input("Would you like to add nuts? (y/n)  -- 0.55$ ").lower()
    while Nuts not in ["y", "n"]:
        print("Please enter 'y' for yes or 'n' for no.\n")
        Nuts = input("Would you like to add nuts? (y/n)  -- 0.55$ ").lower()
    if Nuts == "y":
        print("Adding nuts to your ice cream!\n")
        total_price_of_ice_cream += 0.55
    else:
        print("No nuts will be added to your ice cream.\n")


    Finishing_touches = input("Would you like to add a cherry on top for finishing touch? (y/n)  -- 0.15$ ").lower()
    while Finishing_touches not in ["y", "n"]:
        print("Please enter 'y' for yes or 'n' for no.\n")
        Finishing_touches = input("Would you like to add a cherry on top? (y/n)  -- 0.15$ ").lower()
    if Finishing_touches == "y":
        print("Adding a cherry on top of your ice cream.\n")
        total_price_of_ice_cream += 0.15
    else:
        print("No cherry will be added to your ice cream.\n")

    print(f"Your total price for the ice cream is: ${total_price_of_ice_cream:.2f}\n")

    Decision_of_user = input("Would you like to confirm and place your order? (y/n) ").lower()
    while Decision_of_user not in ["y", "n"]:
        print("Please enter 'y' for yes or 'n' for no.")
        Decision_of_user = input("Would you like to confirm and place your order? (y/n) ").lower()
    if Decision_of_user == "y":
        print("Thank you for placing your order!.\n")
    else:
        print("Your Order is cancelled.\"\n")
    if Decision_of_user == "y":
        print("Your ice cream is being prepared in few seconds, Please wait a moment...\n")
        for i in range(5, 0, -1):
            print(f"{i}s")
            time.sleep(1)
        print("""        ▄████████▄
      ▄█▀        ▀█▄
     █▀   ●    ●   ▀█
    █      ▄▄▄      █
    █     ▀▀▀▀▀     █
     █▄            ▄█
       ▀██████████▀
           ▄██▄
          ██████
         ████████
        ██████████
           ██
           ██

      ── ICE CREAM ──""")
        
        print("Your ice cream is ready! Enjoy your treat!\n")
    
    if Decision_of_user  == "n":
        Decision_of_user_2 = input("Do you want to restart your order:(y/n) -- ").lower()
        while Decision_of_user_2 not in ["y", "n"]:
            print("Please enter 'y' for yes or 'n' for no.\n")
            Decision_of_user_2 = input("Do you want to restart your order? (y/n) ").lower()
        if Decision_of_user_2 == "y":
            total_price_of_ice_cream = 0  # Reset total on restart
            Ice_cream_Order()
        else:
            print("Your order is cancelled.\n")

# Call the function to start the program
Ice_cream_Order()
