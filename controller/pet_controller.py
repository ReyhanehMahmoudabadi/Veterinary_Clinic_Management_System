from business_logic.pet_bl import PetBL
from model.pet import Pet


class PetController:

    def __init__(self):
        self.pet_bl = PetBL()

    def save(self, pet_id, pet_name, species, breed, gender,
             birth_date, weight, owner_id, microchip_number=None):
        try:
            pet = Pet(
                pet_id, pet_name, species, breed, gender,
                birth_date, weight, owner_id, microchip_number
            )
            self.pet_bl.save_pet(pet)
            return True, "Pet Saved!"

        except Exception as e:
            return False, f"Save Failed: {e}"


    def find_all(self):
        try:
            pet_list = self.pet_bl.find_all()
            return True, pet_list
        except Exception as e:
            return False, f"Find Failed: {e}"