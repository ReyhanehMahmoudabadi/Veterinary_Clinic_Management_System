import re


class Validator:

    # Validate first name
    @staticmethod
    def name_validator(name):
        if not isinstance(name, str) or not re.match(r"^[a-zA-Z]{2,30}$", name):
            raise ValueError("Invalid Name!")

    # --------------------------------------------------------------------------------------------
    # Validate family name
    @staticmethod
    def family_validator(family):
        if not isinstance(family, str) or not re.match(r"^[a-zA-Z]{2,50}$", family):
            raise ValueError("Invalid Family!")

    # --------------------------------------------------------------------------------------------
    # Validate national ID (10 digits)
    @staticmethod
    def national_id_validator(national_id):
        if not isinstance(national_id, str) or not re.match(r"^[0-9]{10}$", national_id):
            raise ValueError("Invalid National Id!")

    # --------------------------------------------------------------------------------------------
    # Validate phone number
    @staticmethod
    def phone_validator(phone):
        if not isinstance(phone, str) or not re.match(r"^0?9[0-9]{9}$", phone):
            raise ValueError("Invalid Phone Number!")

    # --------------------------------------------------------------------------------------------
    # Validate email address
    @staticmethod
    def email_validator(email):
        if email is None:
            return

        if not isinstance(email, str):
            raise ValueError("Invalid Email Address!")

        if email.strip() == "":
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
        if not isinstance(address, str) or not re.match(r"^[a-zA-Z0-9آ-ی\s،,./#\-]+$",
                                                        address) or address.strip() == "":
            raise ValueError("Invalid Address!")
