from model.person import Person
from tools.validation import Validator


class Owner(Person):

    # Initialize owner details and inherited person attributes
    def __init__(self, name, family, national_id, phone, owner_id, address, email=None):
        super().__init__(name, family, national_id, phone, email)
        self.owner_id = owner_id
        self.address = address

    # Get and validate owner ID
    @property
    def owner_id(self):
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        Validator.owner_id_validator(owner_id)
        self.__owner_id = owner_id

    # --------------------------------------
    # Get and validate owner address
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        Validator.address_validator(address)
        self.__address = address

    # --------------------------------------
    # Return owner information as a formatted string
    def __repr__(self):
        return (f"Owner (name = {self.name}, "
                f"family = {self.family}, "
                f"national_id = {self.national_id}, "
                f"phone = {self.phone}, "
                f"email = {self.email}, "
                f"owner_id = {self.owner_id}, "
                f"address = {self.address})")
    # --------------------------------------
    # Convert owner information to a tuple
    def to_tuple(self):
        return super().to_tuple() + (self.owner_id, self.address)