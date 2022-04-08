from towns import towns
from random import choice, randint
from images_search import get_images_urls
from towns3 import towns

users = {}


class User:
    def __init__(self, user_id):
        self.id = user_id
        self.current_town = choice(towns)
        self.photos = get_images_urls(self.current_town)
        print(self.photos)
        users[self.id] = self

    def get_photo(self):
        if not self.photos:
            return
        return self.photos.pop(randint(0, len(self.photos) - 1))
