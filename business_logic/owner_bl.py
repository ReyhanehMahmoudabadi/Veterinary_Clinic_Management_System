from data_access.owner_da import OwnerDa

class OwnerBL:
    def __init__(self):
        self.owner_da = OwnerDa()

    def save_owner(self, owner):
        all_owners = self.owner_da.find_all()

        for existing_owner in all_owners:
            if existing_owner.owner_id == owner.owner_id:
                raise ValueError(f"Owner ID {owner.owner_id} already exists!")

        self.owner_da.save(owner)
        return "Owner saved successfully."

    def find_all(self):
        return self.owner_da.find_all()