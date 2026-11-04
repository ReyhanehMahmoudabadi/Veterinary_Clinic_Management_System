from business_logic.owner_bl import OwnerBL
from model.owner import Owner


class OwnerController:

    def __init__(self):
        self.owner_bl = OwnerBL()

    def save(self, name, family, national_id, phone, owner_id, address, email=None):
        try:
            print("Name:", repr(name))
            owner = Owner( name, family, national_id, phone,owner_id, address, email)
            self.owner_bl.save_owner(owner)
            return True, "Owner Saved!"

        except Exception as e:
            return False, f"Save Failed : {e}"


    def find_all(self):
        try:
            owner_list = self.owner_bl.find_all()
            return True, owner_list
        except Exception as e:
            return False, f"Find Failed : {e}"