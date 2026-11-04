from tools.validation import Validator

# Person Class
class Person:

    # Initialize person attributes
    def __init__(self, name, family, national_id, phone, email=None):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.phone = phone
        self.email = email

    # -------------------------------------
    # Properties (Getters and Setters)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        Validator.name_validator(name)
        self.__name = name


    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family):
        Validator.family_validator(family)
        self.__family = family


    @property
    def national_id(self):
        return self.__national_id

    @national_id.setter
    def national_id(self, national_id):
        Validator.national_id_validator(national_id)
        self.__national_id = national_id

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        Validator.phone_validator(phone)
        self.__phone = phone


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = Validator.email_validator(email)


    # -------------------------------------
    # Return person information
    def __repr__(self):
        return (f"Person ( name = {self.name} ,"
                f" family = {self.family} ,"
                f" national_id = {self.national_id} ,"
                f" phone = {self.phone} ,"
                f" email = {self.email})")

    # -------------------------------------
    # Convert person information to tuple
    def to_tuple(self):
        return self.name, self.family, self.national_id, self.phone, self.email