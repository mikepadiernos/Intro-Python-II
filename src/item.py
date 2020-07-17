class Item:
    def __init__(self, name, item_type, item_attributes):
        self.name = name
        self.type = item_type
        self.attributes = item_attributes

    def __str__(self):
        if len(self.name) > 0:
            return f'You hold the {self.type} of {self.name}'
        else:
            return f'You hold a {self.type}'
