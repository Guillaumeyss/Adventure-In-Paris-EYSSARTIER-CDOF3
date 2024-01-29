import os

inventory = []

def displayPerson(withHat=False) :
    if withHat: print(" _□_")
    print("  O")
    print(" /|\\")
    print(" / \\")


def display_inventory():
    global inventory  
    print("Your current inventory: ", inventory)

def intro():
    os.system('cls')
    global inventory
    print("Hello "+name)
    print("Here is your first choice, do you want to have a knife or a gun ?")
    print ("1 - knife")
    print("2 - gun")
    while(True):
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
          inventory.append("knife")
          print("You chose a knife. It has been added to your inventory.")
          break
        elif choice == "2":
          inventory.append("gun")
          print("You chose a gun. It has been added to your inventory.")
          break
        else:
          print("Invalid choice. Please enter 1 or 2.")
    display_inventory()
    print("I would have chosen the other one but ... it's your choice ! Maybe you are right, maybe...")
    first_scene()
    
def first_scene():
    os.system('cls')
    displayPerson(withHat=True)
    print('"Solve this enigma and I will let you pass, otherwise you will have to give me your inventory !"')
    print('\n"I fly without wings. I cry without eyes.')
    print('Wherever I go, darkness follows me.')
    print('What am I?"\n')
    cpt=2

    while(cpt!=-1):
        choice = input("Enter your answer : ")
        answer=choice.lower()

        if answer == "cloud":
          print('"nice one"')
          break
        elif answer == "clouds":
          print('"Nice one !"')
          break
        elif answer == "use knife" and "knife" in inventory:
           print("You stabbed the riddler and stole his inventory")
           print("In it you found a funny hat")
           inventory.append("funny hat")
           display_inventory()
           break
        elif answer == "use gun" and "gun" in inventory:
           print("You tried to shoot the riddler to get away from this situation")
           print("You don't have any bullets with that gun. Maybe you should have thought about that before pulling a weapon on a stranger...")
           print("The riddler is not impressed and takes away one of your tries")
           print('"...let this be a lesson for you..."')
           cpt=cpt-1
        else:
          print(f'"Hmmm no that is not the good answer {cpt} tries remaining..."')
          cpt=cpt-1
    
    if cpt==-1:
       print('"Hahaha ! You failed the simplest riddle possible, and you think you have a chance in this world ?"')
       print('"A promise is a promise, stand your ground, and give me your inventory you filth !"')
       print("The riddler steals all of your inventory and runs away smiling machiavellically")
       inventory.clear()



def Menu_Screen():
    os.system('cls')
    print(15*"-"+"\t WELCOME TO ADVENTURE IN PARIS \t"+15*"-"+"\n")

def End_Screen(end):
    print(15*"-"+"\t Thank you for playing my game \t"+15*"-"+"\n")
    print('\n\n\nCredit : Guillaume "Beau Gosse" Eyssartier\n\n')
    return True



if __name__ == "__main__":
  end = False
  Menu_Screen()
  while end==False:
    print("Welcome to my Text based Adventure Game")
    print("You will travel in the shadows of Paris !")
    print("During your travel, you will have multiple decisions to take in order to stay alive.")
    print("I hope you will take the good ones...")
    print("But first, let me know what is your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    intro()
    end = End_Screen(end)


