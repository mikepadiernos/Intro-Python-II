# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


def blocked():
    print(f'Thou art blocked!')


class Player(Room):
    def __init__(self, name, room):
        self.name = name
        self.current_room = room

    def movement(self, direction):
        here = self.current_room.movements(direction)
        if here is not None:
            self.current_room = here
            print(f"Thou'st entered the {here.name}, {here.description}")
        else:
            blocked()
