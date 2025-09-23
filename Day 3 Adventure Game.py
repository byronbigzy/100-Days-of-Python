import random

# Player Stats:
health = 100
inventory = []

#Clearing
def Clearing():
    print("Two paths lie before you: one leading LEFT into a dark cave, and one RIGHT toward a mystic river.")
    choice = input("Which path do you choose?\n")
    while True:
        if choice.lower() == "left":
            Dark_Cave()
        elif choice.lower() == "right":
            Mythic_River()
        else:
            choice = input("You haven't chosen a valid path. Try again.\n")

# Dark Cave Path
def Dark_Cave():
    print("You step into the cave. The air is damp, and a deep rumble echoes... a bear sleeps inside.")
    choice = input("Do you try to SNEAK past the bear, or THROW a rock to distract it?\n")
    if choice.lower() == "sneak":
        if random.randint(1,100) <= 50:
            print("You carefully tiptoe past the slumbering beast. In the shadows, you find a rusty sword.")
            inventory.append("Rusty Sword")
            Clearing()
        else:
            print("Your foot snaps a twig! The bear roars awake, forcing you to flee back to the clearing.")
            Clearing()
    if choice.lower() == "throw":
        print("The rock clatters. The bear charges! You barely escape with scratches, back to the clearing.")
        health =- 25
        print(f"You lost some health to the bear, you now have {health}hp remaining.")
        Clearing()

# Mystic River Path
def Mythic_River():
    print("You reach a wide river. The water glimmers with an eerie light.")
    choice = input("Do you SWIM across, or SEARCH the riverbank?\n")

    # Swim Option
    if choice.lower() == "swim":
        if health < 50:
            print("The current is too strong! It drags you downstream. You cough and stagger back to the clearing.")
            Clearing()
        else:
            print("You push against the current and make it across, breathless but alive. An ancient shrine looms ahead.")
            Ancient_Shrine()

    # Search Option
    if choice.lower() == "search":
        print("You search the bank and find a small boat. It is sturdy... but there’s no oar.")
        print("")

# Ancient Shrine
def Ancient_Shrine():
    print("You stand before a moss-covered shrine. A stone pedestal glows with runes.")
    print("Etched words read: 'Only the Brave with Steel, or the Wise with Knowledge, may claim the key.'")
    if "Rusty Sword" in inventory:
        print("You draw the rusty sword. A guardian spirit rises from the pedestal, testing your strength.")
        # Could add a fight sequence here if bored
        print("After a fierce clash, the spirit bows and vanishes. The Lost Key lies before you.")
        Victory()
    else:
        print("The pedestal shifts, revealing a riddle carved into the stone...")
        print("Answer correctly, and the Lost Key shall be yours.")
        choice = input("I have cities, but no houses.\nI have mountains, but no trees.\nI have water, but no fish.\nWhat am I?")
        if "map" == choice.lower():
            print("The shrine hums with approval. The Lost Key emerges in a beam of light.")
            (Victory)
        else:
            print("The runes flare angrily! You are cast out, stumbling back to the clearing.")
            Clearing()

# The Clearing (Return with Key)
def Victory():
    print("You return to the clearing. A tall, locked gate stands waiting.")
    print("With trembling hands, you place the Lost Key into the lock.")
    print("The gate creaks open, sunlight spilling through. You have escaped Eldermist Forest.")
    print("*** You Win! ***")
    
# Game Over Messages
def Game_Over():
    print("Exhausted and wounded, you can go no further. The forest claims you.")
    print("*** Game Over ***")

# Game Start: Introduction 
print('''
 __        __   _                            _     
 \ \      / /__| | ___ ___  _ __ ___   ___  | |    
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |    
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | |    
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_|    

           THE LOST KEY OF ELDERMIST

''')
print("You awaken in a quiet clearing within the enchanted Eldermist Forest.")
print("Legends whisper of a Lost Key that unlocks the only path out.")
Clearing()