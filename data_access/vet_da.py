import os
import pickle

class VetDa:
    def __init__(self):
        self.filename= "data_access/data/vet.dat"
        self.vet_list = self.find_all()


    def save(self, vet):
        self.vet_list.append(vet)
        file = open(self.filename, "wb")
        pickle.dump(self.vet_list, file)
        file.close()


    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            vet_list = pickle.load(file)
            file.close()
            return vet_list
