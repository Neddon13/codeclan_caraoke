class Room:

    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.play_list = []
        self.check_in = []

    def check_in_guest(self, guest):
        self.check_in.append(guest)

    def check_guest_has_enough_cash(self, guest):
        if guest.cash >= self.room1.price:
            return "Have fun!"
        else:
            return "Not enough cash!"
