def start_game():
    # Initial Prompt
    print('You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears')
    print('To your left, a narrow tunnel leads deeper into darkness. To your right, a wider passage seems to have some light.')
    print('Which way do you go')
    choice1 = input("Type 'left' to go into the tunnel or 'right' to go toward the light: ").lower()
    
    # first decisions left or right path
    if choice1 == 'left':
        tunnel_path()
    elif choice1 == 'right':
        light_path()
    else:
        # invalid
        print('Invalid choice. Try again.')
        start_game()
    
def tunnel_path():
    # The player chooses the tunnel path and faces the river
    print("You brave the dark tunnel, and the sound of rushing water grows louder. You reach an underground river.")
    print("Do you swim across or follow the river downstream?")
    choice2 = input("Type 'swim' to cross the river or 'follow' to follow the river: ").lower()

    # Second decision point: Swim or follow the river
    if choice2 == 'swim':
        swim_path()
    elif choice2 == 'follow':
        follow_path()
    else:
        # Invalid input case
        print('Invalid choice. Try again')
        tunnel_path()

def swim_path():
    # The player chooses to swim across the river
    print("You decide to swim across the river, but midway, you encounter a whirlpool.")
    print("Do you try to swim harder or let the whirlpool take you?")
    choice3 = input("Type 'fight' to swim harder or 'whirlpool' to let it take you: ").lower()

    # Third decision point: fight the whirlpool or let it take you
    if choice3 == 'fight':
        ending1()
    elif choice3 == 'whirlpool':
        ending2()
    else:
        # Invalid input case
        print("Invalid choice. Try again.")
        swim_path()

def follow_path():
    # The player chooses to follow the river downstream
    print("You follow the river downstream and find a hidden path leading out of the cave.")
    print("Do you continue along the river or explore the new path?")
    choice3 = input("Type 'continue' to follow the river or 'explore' to take the new path: ").lower()

    # Third decision point: continue following the river or explore the new path
    if choice3 == 'continue':
        ending3()
    elif choice3 == 'explore':
        ending4()
    else:
        # Invalid input case
        print("Invalid choice. Try again.")
        follow_path()

def light_path():
    # The player chooses the path toward the light
    print("You walk toward the light and find a strange glowing crystal in the middle of a large chamber.")
    print("Do you touch the crystal or ignore it and explore the chamber further?")
    choice2 = input("Type 'touch' to touch the crystal or 'explore' to explore further: ").lower()

    # Second decision point: touch the crystal or explore the chamber
    if choice2 == 'touch':
        crystal_path()
    elif choice2 == 'explore':
        chamber_path()
    else:
        # Invalid input case
        print("Invalid choice. Try again.")
        light_path()

def crystal_path():
    # The player chooses to touch the crystal
    print("You touch the crystal and a door opens, revealing an ancient library.")
    print("Do you enter the library or retreat?")
    choice3 = input("Type 'enter' to explore the library or 'retreat' to go back: ").lower()

    # Third decision point: enter the library or retreat
    if choice3 == 'enter':
        ending5()
    elif choice3 == 'retreat':
        ending6()
    else:
        # Invalid input case
        print("Invalid choice. Try again.")
        crystal_path()

def chamber_path():
    # The player chooses to explore the chamber
    print("You explore the chamber and discover a hidden treasure chest.")
    print("Do you open the chest or leave it alone?")
    choice3 = input("Type 'open' to open the chest or 'leave' to leave it: ").lower()

    # Third decision point: open the chest or leave it
    if choice3 == 'open':
        ending7()
    elif choice3 == 'leave':
        ending8()
    else:
        # Invalid input case
        print("Invalid choice. Try again.")
        chamber_path()

# Various endings based on the player's choices
def ending1():
    print("You fight against the whirlpool but tire out quickly. You drown in the cold, dark water. The end.")
    play_again()

def ending2():
    print("You let the whirlpool take you, and it carries you safely to a hidden cave. You find a way out. The end.")
    play_again()

def ending3():
    print("You continue along the river and find an opening that leads outside. You escape the cave. The end.")
    play_again()

def ending4():
    print("You explore the new path but it leads deeper into the cave. You're lost forever. The end.")
    play_again()

def ending5():
    print("You enter the ancient library and discover forgotten knowledge. Your mind expands beyond the known world. The end.")
    play_again()

def ending6():
    print("You retreat from the crystal, but the door shuts forever, trapping you inside. The end.")
    play_again()

def ending7():
    print("You open the treasure chest and are cursed by its contents. You fade into darkness. The end.")
    play_again()

def ending8():
    print("You leave the treasure chest alone, but as you turn to leave, the floor collapses beneath you. The end.")
    play_again()

# Asks the player if they want to play again
def play_again():
    choice = input("Would you like to play again? (yes/no): ").lower()
    if choice == 'yes':
        start_game()
    elif choice == 'no':
        print("Thanks for playing!")
    else:
        # Handles invalid input for replay choice
        print("Invalid input. Please type 'yes' or 'no'.")
        play_again()

# Start the game
start_game()


    
