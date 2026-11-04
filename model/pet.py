from tools.validation import Validator
from datetime import date

# Pet Class
class Pet:

    # Initialize pet attributes
    def __init__(self, pet_id, pet_name, species, breed, gender, birth_date, weight, microchip_number=None):
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.species = species
        self.breed = breed
        self.gender = gender
        self.birth_date = birth_date
        self.weight = weight
        self.microchip_number = microchip_number

    # --------------------------------------------------
    # Properties (Getters and Setters)
    @property
    def pet_id(self):
        return self.__pet_id

    @pet_id.setter
    def pet_id(self, pet_id):
        Validator.pet_id_validator(pet_id)
        self.__pet_id = pet_id


    @property
    def pet_name(self):
        return self.__pet_name

    @pet_name.setter
    def pet_name(self, pet_name):
        Validator.pet_name_validator(pet_name)
        self.__pet_name = pet_name


    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        Validator.species_validator(species)
        self.__species = species


    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        Validator.breed_validator(breed)
        self.__breed = breed


    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = Validator.gender_validator(gender)


    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        Validator.birth_date_validator(birth_date)
        self.__birth_date = birth_date


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        Validator.weight_validator(weight)
        self.__weight = weight


    @property
    def microchip_number(self):
        return self.__microchip_number

    @microchip_number.setter
    def microchip_number(self, microchip_number):
        Validator.microchip_number_validator(microchip_number)
        self.__microchip_number = microchip_number

    # --------------------------------------------------
    # Return pet information
    def __repr__(self):
        return (f"Pet (pet_id = {self.pet_id} , pet_name = {self.pet_name} ,"
                f"species = {self.species} , breed = {self.breed} ,"
                f"gender = {self.gender} , birth_date = {self.birth_date} ,"
                f"weight = {self.weight} , microchip_number = {self.microchip_number} )")

    # --------------------------------------------------
    # Convert pet information to tuple
    def to_tuple(self):
        return self.pet_id, self.pet_name, self.species, self.breed, self.gender, self.birth_date, self.weight, self.microchip_number

    # --------------------------------------------------
    # Calculate pet age
    def calculate_age(self):
        today = date.today()
        age = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age = age - 1

        return age