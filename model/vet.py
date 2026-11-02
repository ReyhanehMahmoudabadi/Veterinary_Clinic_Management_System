from model.person import Person
from tools.validation import Validator


class Vet(Person):

    # Initialize vet details and inherited person attributes
    def __init__(self, name, family, national_id, phone, specialization, license_number, vet_id, email=None):
        super().__init__(name, family, national_id, phone, email)
        self.vet_id = vet_id
        self.specialization = specialization
        self.license_number = license_number

    # --------------------------------------------------
    # Get and validate vet ID
    @property
    def vet_id(self):
        return self.__vet_id

    @vet_id.setter
    def vet_id(self, vet_id):
        Validator.vet_id_validator(vet_id)
        self.__vet_id = vet_id

    # --------------------------------------------------
    # Get and validate specialization
    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, specialization):
        Validator.specialization_validator(specialization)
        self.__specialization = specialization

    # --------------------------------------------------
    # Get and validate license number
    @property
    def license_number(self):
        return self.__license_number

    @license_number.setter
    def license_number(self, license_number):
        Validator.license_number_validator(license_number)
        self.__license_number = license_number

    # --------------------------------------------------
    # Return vet information as a formatted string
    def __repr__(self):
        person_info = super().__repr__()
        return (f"{person_info} | Vet ( vet_id = {self.vet_id} ,"
                f" specialization = {self.specialization} ,"
                f" license_number = {self.license_number} )")

    # --------------------------------------------------
    # Convert vet information to a tuple
    def to_tuple(self):
        return super().to_tuple() + (self.vet_id, self.specialization, self.license_number)