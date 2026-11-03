from model.person import Person
from tools.validation import Validator

# Owner Class
class Owner(Person):

    # Initialize owner attributes
    def __init__(self, name, family, national_id, phone, owner_id, address, email=None):
        super().__init__(name, family, national_id, phone, email)
        self.owner_id = owner_id
        self.address = address

    # --------------------------------------
    # Properties (Getters and Setters)
    @property
    def owner_id(self):
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        Validator.owner_id_validator(owner_id)
        self.__owner_id = owner_id


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        Validator.address_validator(address)
        self.__address = address

    # --------------------------------------
    # Return owner information
    def __repr__(self):
        person_info = super().__repr__()
        return f"{person_info} | Owner ( owner_id = {self.owner_id} )"

    # --------------------------------------
    # Convert owner information to tuple
    def to_tuple(self):
        return super().to_tuple() + (self.owner_id, self.address)
