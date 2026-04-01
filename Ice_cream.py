
print("Welcome to the Best Ice Cream Parlor in Town!")
print("""
    🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦
    🍦                  🍦
    🍦   ICE CREAM      🍦
    🍦   PARADISE       🍦
    🍦                  🍦
    🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦
""")

def Making_ice_creame(func):
    def wrapper():
        func()
        print("We will try to match the taste that you like!")
    return wrapper

@Making_ice_creame
def ice_cream():
    print("We will make your ice cream with the best ingredients and toppings!")
    
ice_cream()


list_of_iceCream_flavors = {
1: "Vanilla",
2: "Chocolate",
3: "Strawberry",
4: "Mint Chocolate Chip",
5: "Cookie Dough"
}


print("Here are the available ice cream flavors:")
for key, value in list_of_iceCream_flavors.items():
    print(f"{key}: {value}")

user_input = int(input("Please enter the number corresponding to your desired flavor: "))
while user_input not in list_of_iceCream_flavors:
    print("Sorry, we have only the following flavors available.")
    for key, value in list_of_iceCream_flavors.items():
        print(f"{key}: {value}")
    user_input = int(input("Please enter the number corresponding to your desired flavor: "))
print(f"You have selected {list_of_iceCream_flavors[user_input]} flavor.")


Chocolate_syrup = input("Would you like to add chocolate syrup? (y/n) ").lower()
while Chocolate_syrup not in ["y", "n"]:
    print("Please enter 'y' for yes or 'n' for no.")
    Chocolate_syrup = input("Would you like to add chocolate syrup? (y/n) ").lower()

if Chocolate_syrup == "y":
    print("Adding chocolate syrup to your ice cream!")
else:
    print("No chocolate syrup will be added to your ice cream.")

Sprinkles = input("Would you like to add sprinkles? (y/n) ").lower()
while Sprinkles not in ["y", "n"]:
    print("Please enter 'y' for yes or 'n' for no.")
    Sprinkles = input("Would you like to add sprinkles? (y/n) ").lower()

if Sprinkles == "y":
    print("Adding sprinkles to your ice cream!")
else:
    print("No sprinkles will be added to your ice cream.")
print("Your ice cream is being prepared. Please wait a moment...")

print("scan this qr and pay you total amount for the ice creame")