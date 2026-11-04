import os
import pickle

class VisitDa:
    def __init__(self):
        self.filename= "data_access/data/visit.dat"
        self.visit_list = self.find_all()


    def save(self, visit):
        self.visit_list.append(visit)
        file = open(self.filename, "wb")
        pickle.dump(self.visit_list, file)
        file.close()


    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            visit_list = pickle.load(file)
            file.close()
            return visit_list