from data_access.pet_da import  PetDa
from data_access.owner_da import OwnerDa


class PetBL:
    def __init__(self):
        self.pet_da = PetDa()
        self.owner_da = OwnerDa()

    def save_pet(self, pet):
        all_pets = self.pet_da.find_all()

        for existing_pet in all_pets:
            if existing_pet.pet_id == pet.pet_id:
                raise ValueError(f"Pet ID {pet.pet_id} already exists!")


        all_owners = self.owner_da.find_all()
        owner_exists = False
        for existing_owner in all_owners:
            if existing_owner.owner_id == pet.owner_id:
                owner_exists = True
                break

        if not owner_exists:
            raise ValueError(f"Owner ID {pet.owner_id} does not exist!")

        self.pet_da.save(pet)
        return "Pet saved successfully."

    def find_all(self):
        return self.pet_da.find_all()



