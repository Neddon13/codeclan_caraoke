class Room:

    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.play_list = []
        self.check_in = []

    def add_guest_to_check_in(self, guest):
        self.check_in.append(guest)

    def add_song_to_play_list(self, song):
        self.play_list.append(song)

    def remove_song_by_title(self, title):
        [self.play_list.remove(song) 
        for song in self.play_list
        if song.title == song.title]

