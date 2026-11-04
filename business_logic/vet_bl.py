from data_access.vet_da import  VetDa

class VetBL:
    def __init__(self):
        self.vet_da = VetDa()

    def save_vet(self, vet):
        all_vets = self.vet_da.find_all()

        for existing_vet in all_vets:
            if existing_vet.vet_id == vet.vet_id:
                raise ValueError(f"Vet ID {vet.vet_id} already exists!")

        self.vet_da.save(vet)
        return "Vet saved successfully."

    def find_all(self):
        return self.vet_da.find_all()