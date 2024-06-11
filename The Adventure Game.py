#Tast 1: Code Correction
#Check to see which place the user would like to explore
place = input("Choose a place: forest or cave? ")

if place == "forest":
    #Check to see what action the user would like to take in the forest
    action = input("climb a tree or cross a river? ")
    #Display the results of the users action in the forest
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == input("cross a river"):
        print("You found a boat!")
    else:
        pass
elif place == "cave":
#Task 2: Setting the Scene
    #Check to see what action the user would like to take in the cave
    action = input("light a torch or proceed in the dark? ")
    #Display the results of the users action in the cave
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == input("proceed in the dark"):
        print("You got lost in the cave!")
    else:
        pass
else:
    pass

#Task 3: Default Path
#pass statements inserted into else statements to fill invalid choices