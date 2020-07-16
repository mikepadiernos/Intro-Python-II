from room import Room
from player import Player
import os

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer",
                  """Dim light filters in from the south. 
                  Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness. 
                     Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage",
                   """The narrow passage bends here from west to north. 
                   The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure chamber! 
                     Sadly, it has already been completely emptied by earlier adventurers. 
                     The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

directions = ["n", "s", "e", "w", "quit"]


def game_start():

    os.system('clear')

    name = 'Traveler'
    avatar = Player(name, room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    title = 'Ultima: Quest for the Lost Journals'
    finale = f"Thou art leaving {title}. Til' the next age!"

    print(f'\n{title}\n\nChoose your path!\nWould you like to play?\n')

    cmd = input('To [p]lay or [n]ot to play.\nThat is thy question!\n> ').lower().strip()

    if cmd == 'p':
        name = input('By what name thou shalt be called, Avatar?\n> ')
        if name != '':
            avatar.name = name
    elif cmd == 'n':
        print(finale)
        exit()
    else:
        print(finale)

    while cmd == 'p':
        path = input(f'{avatar.name}, thy move?\n> ').lower().strip()
        if path.lower() in directions:
            avatar.movement(path)
        elif path.lower() == 'q':
            os.system('clear')
            print(finale + '\n')
            exit()


game_start()
