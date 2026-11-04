import os
import pickle

class OwnerDa:
    def __init__(self):
        self.filename = "data_access/data/owner.dat"
        self.owner_list = self.find_all()


    def save(self, owner):
        self.owner_list.append(owner)
        file = open(self.filename, "wb")
        pickle.dump(self.owner_list, file)
        file.close()


    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            owner_list = pickle.load(file)
            file.close()
            return owner_list