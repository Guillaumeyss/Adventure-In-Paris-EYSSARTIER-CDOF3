

inventory = []

def displayPerson() :
    print("  O")
    print(" /|\\")
    print(" / \\")


def display_inventory():
    global inventory  
    print("Your current inventory: ", inventory)

def intro():
    global inventory
    print("Hello "+name)
    print("Here is your first choice, do you want to have a knife or a gun ?")
    print ("1 - knife")
    print("2 - gun")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        inventory.append("knife")
        print("You chose a knife. It has been added to your inventory.")
    elif choice == "2":
        inventory.append("gun")
        print("You chose a gun. It has been added to your inventory.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
    display_inventory()
    print("I would have chosen the other one but ... it's your choice ! Maybe you are right, maybe...")
    first_scene()
    
def first_scene():
    displayPerson()




if __name__ == "__main__":
  while True:
    print("Welcome to my Text based Adventure Game")
    print("You will travel in the shadows of Paris !")
    print("During your travel, you will have multiple decisions to take in order to stay alive.")
    print("I hope you will take the good ones...")
    print("But first, let me know what is your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    intro()


