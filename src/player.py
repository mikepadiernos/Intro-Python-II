# Write a class to hold player information, e.g. what room they are in
# currently.


def blocked():
    print(f'Thou art blocked!')


class Player:
    def __init__(self, name, room, inventory):
        self.name = name
        self.current_room = room
        self.inventory = inventory

    def movement(self, direction):
        here = self.current_room.movements(direction)
        if here is not None:
            self.current_room = here
            print(f"Thou'st entered the {here.name}, {here.description}")
        else:
            blocked()
