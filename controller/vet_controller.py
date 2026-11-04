from business_logic.vet_bl import VetBL
from model.vet import Vet

class VetController:

    def __init__(self):
        self.vet_bl = VetBL()

    def save(self, name, family, national_id, phone,
             specialization, license_number, vet_id, email=None):
        try:
            vet = Vet(
                name, family, national_id, phone,
                specialization, license_number, vet_id, email
            )
            self.vet_bl.save_vet(vet)
            return True, "Vet Saved!"

        except Exception as e:
            return False, f"Save Failed: {e}"


    def find_all(self):
        try:
            vet_list = self.vet_bl.find_all()
            return True, vet_list
        except Exception as e:
            return False, f"Find Failed: {e}"