import re
from datetime import date

class Validator:

    # Validate first name
    @staticmethod
    def name_validator(name):
        if not isinstance(name, str):
            raise ValueError("Invalid Name!")
        name = name.strip()
        if not re.match(r"^[a-zA-Z]{2,30}$", name):
            raise ValueError("Invalid Name!")

# --------------------------------------------------------------------------------------------
    # Validate family name
    @staticmethod
    def family_validator(family):
        if not isinstance(family, str):
            raise ValueError("Invalid Family!")
        family = family.strip()
        if not re.match(r"^[a-zA-Z]{2,50}$", family):
            raise ValueError("Invalid Family!")

# --------------------------------------------------------------------------------------------
    # Validate national ID (10 digits)
    @staticmethod
    def national_id_validator(national_id):
        if not isinstance(national_id, str):
            raise ValueError("Invalid National Id!")
        national_id = national_id.strip()
        if not re.match(r"^[0-9]{10}$", national_id):
            raise ValueError("Invalid National Id!")

# --------------------------------------------------------------------------------------------
    # Validate phone number
    @staticmethod
    def phone_validator(phone):
        if not isinstance(phone, str):
            raise ValueError("Invalid Phone Number!")
        phone = phone.strip()

        if not re.match(r"^0?9[0-9]{9}$", phone):
            raise ValueError("Invalid Phone Number!")

# --------------------------------------------------------------------------------------------
    # Validate email address
    @staticmethod
    def email_validator(email):
        if email is None:
            return

        if not isinstance(email, str):
            raise ValueError("Invalid Email Address!")

        email = email.strip()

        if email == "":
            return

        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise ValueError("Invalid Email Address!")

# --------------------------------------------------------------------------------------------
    # Validate owner ID
    @staticmethod
    def owner_id_validator(owner_id):
        if not isinstance(owner_id, int) or not owner_id > 0:
            raise ValueError("Invalid Owner Id!")

# --------------------------------------------------------------------------------------------
    # Validate address
    @staticmethod
    def address_validator(address):
        if not isinstance(address, str):
            raise ValueError("Invalid Address!")

        address = address.strip()

        if not re.match(r"^[a-zA-Z0-9آ-ی\s،,./#\-]+$", address):
            raise ValueError("Invalid Address!")

# --------------------------------------------------------------------------------------------
    # Validate vet ID
    @staticmethod
    def vet_id_validator(vet_id):
        if not isinstance(vet_id, int) or not vet_id > 0:
            raise ValueError("Invalid Vet Id!")

# --------------------------------------------------------------------------------------------
    # Validate specialization
    @staticmethod
    def specialization_validator(specialization):
        if not isinstance(specialization, str):
            raise ValueError("Invalid Specialization!")

        specialization = specialization.strip()

        if not re.match(r"^[a-zA-Z ]{2,100}$", specialization):
            raise ValueError("Invalid Specialization!")

# --------------------------------------------------------------------------------------------
    # Validate veterinary license number
    @staticmethod
    def license_number_validator(license_number):
        if not isinstance(license_number, str):
            raise ValueError("Invalid License Number!")
        license_number = license_number.strip()
        if not re.match(r"^[0-9]{4,20}$", license_number):
            raise ValueError("Invalid License Number!")

# --------------------------------------------------------------------------------------------
    # Validate pet ID
    @staticmethod
    def pet_id_validator(pet_id):

        if not isinstance(pet_id, str):
            raise ValueError("Invalid Pet Id!")
        pet_id = pet_id.strip()
        if not re.match(r"^[a-zA-Z0-9]{10}$", pet_id):
            raise ValueError("Invalid Pet Id!")
# --------------------------------------------------------------------------------------------
    # Validate pet name
    @staticmethod
    def pet_name_validator(pet_name):
        if not isinstance(pet_name, str):
            raise ValueError("Invalid Pet Name!")
        pet_name = pet_name.strip()
        if not re.match(r"^[a-zA-Z]{1,30}$", pet_name):
            raise ValueError("Invalid Pet Name!")
# --------------------------------------------------------------------------------------------
    #Validate species
    @staticmethod
    def species_validator(species):
        if not isinstance(species, str):
            raise ValueError("Invalid Species!")
        species = species.strip()
        if not re.match(r"^[a-zA-Z ]{1,50}$", species):
            raise ValueError("Invalid Species!")
# --------------------------------------------------------------------------------------------
    #Validate breed
    @staticmethod
    def breed_validator(breed):
        if not isinstance(breed, str):
            raise ValueError("Invalid Breed!")
        breed = breed.strip()
        if not re.match(r"^[a-zA-Z ]{1,50}$", breed):
            raise ValueError("Invalid Breed!")
# --------------------------------------------------------------------------------------------
    #Validate gender
    @staticmethod
    def gender_validator(gender):
        if not isinstance(gender, str):
            raise ValueError("Invalid Gender!")
        gender = gender.strip()
        if gender.lower() not in ["male", "female", "unknown"]:
            raise ValueError("Invalid Gender!")
# --------------------------------------------------------------------------------------------
    #Validate birth date
    @staticmethod
    def birth_date_validator(birth_date):
        if not isinstance(birth_date, date):
            raise ValueError("Invalid Birth Date!")
        if birth_date > date.today():
            raise ValueError("Invalid Birth Date!")
# --------------------------------------------------------------------------------------------
    #Validate weight
    @staticmethod
    def weight_validator(weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Invalid Weight!")
        if weight <= 0:
            raise ValueError("Invalid Weight!")
# --------------------------------------------------------------------------------------------
    #Validate microchip number
    @staticmethod
    def microchip_number_validator(microchip_number):
        if microchip_number is None:
            return

        if not isinstance(microchip_number, str):
            raise ValueError("Invalid Microchip Number!")

        microchip_number = microchip_number.strip()
        if not re.match(r"^[0-9]{15}$", microchip_number):
            raise ValueError("Invalid Microchip Number!")