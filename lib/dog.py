class Dog:
    approved_breeds = ["Pug", "Labrador", "Bulldog"]

    def __init__(self, name=None, breed=None):
        self.name = name
        self.breed = breed
        if not name or not isinstance(name, str) or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        elif not breed or not isinstance(breed, str) or breed not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
        else:
            self.name = name
            self.breed = breed
