from towns import towns
from random import choice, randint

users = {}


class User:
    def __init__(self, user_id):
        self.id = user_id
        self.current_town = choice(towns.keys())
        self.photos = towns[self.current_town].copy()
        users[self.id] = self

    def get_photo(self):
        if not self.photos:
            return
        return self.photos.pop(randint(0, len(self.photos) - 1))
