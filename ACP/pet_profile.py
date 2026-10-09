class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    def display_profile(self):
        print("Pet Name:", self.name)
        print("Animal Type:", self.animal_type)
        print("Age:", self.age)
pet1 = Pet("Buddy", "Dog", 3)
pet1.display_profile()