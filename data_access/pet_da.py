import os
import pickle

class PetDa:
    def __init__(self):
        self.filename = "data_access/data/pet.dat"
        self.pet_list = self.find_all()


    def save(self, pet):
        self.pet_list.append(pet)
        file = open(self.filename, "wb")
        pickle.dump(self.pet_list, file)
        file.close()


    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            pet_list = pickle.load(file)
            file.close()
            return pet_list