from data_access.visit_da import VisitDa
from data_access.vet_da import VetDa
from data_access.pet_da import PetDa


class VisitBL:
    def __init__(self):
        self.visit_da = VisitDa()
        self.vet_da = VetDa()
        self.pet_da = PetDa()

    def save_visit(self, visit):
        all_visits = self.visit_da.find_all()

        for existing_visit in all_visits:
            if existing_visit.visit_id == visit.visit_id:
                raise ValueError(f"Visit ID {visit.visit_id} already exists!")
        all_pets = self.pet_da.find_all()
        pet_exists = False

        for existing_pet in all_pets:
            if existing_pet.pet_id == visit.pet_id:
                pet_exists = True
                break

        if not pet_exists:
            raise ValueError(f"Pet ID {visit.pet_id} does not exist!")

        all_vets = self.vet_da.find_all()
        vet_exists = False

        for existing_vet in all_vets:
            if existing_vet.vet_id == visit.vet_id:
                vet_exists = True
                break

        if not vet_exists:
            raise ValueError(f"Vet ID {visit.vet_id} does not exist!")

        self.visit_da.save(visit)
        return "Visit saved successfully."

    def find_all(self):
        return self.visit_da.find_all()
