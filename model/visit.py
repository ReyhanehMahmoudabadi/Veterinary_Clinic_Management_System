from tools.validation import Validator


# Visit Class
class Visit:

    # Initialize visit attributes
    def __init__(self,visit_id,visit_date,reason,status,vet_id,pet_id,diagnosis=None,treatment=None):
        self.visit_id = visit_id
        self.visit_date = visit_date
        self.reason = reason
        self.status = status
        self.vet_id = vet_id
        self.pet_id = pet_id
        self.diagnosis = diagnosis
        self.treatment = treatment

    #----------------------------------------------------
    # Properties (Getters and Setters)
    @property
    def visit_id(self):
        return self.__visit_id

    @visit_id.setter
    def visit_id(self,visit_id):
        Validator.visit_id_validator(visit_id)
        self.__visit_id = visit_id


    @property
    def visit_date(self):
        return self.__visit_date

    @visit_date.setter
    def visit_date(self,visit_date):
        Validator.visit_date_validator(visit_date)
        self.__visit_date = visit_date


    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self,reason):
        Validator.reason_validator(reason)
        self.__reason = reason


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self,status):
        Validator.status_validator(status)
        self.__status = status


    @property
    def vet_id(self):
        return self.__vet_id

    @vet_id.setter
    def vet_id(self,vet_id):
        Validator.vet_id_validator(vet_id)
        self.__vet_id = vet_id


    @property
    def pet_id(self):
        return self.__pet_id

    @pet_id.setter
    def pet_id(self,pet_id):
        Validator.pet_id_validator(pet_id)
        self.__pet_id = pet_id


    @property
    def diagnosis(self):
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self,diagnosis):
        if diagnosis is not None:
            Validator.diagnosis_validator(diagnosis)
        self.__diagnosis = diagnosis


    @property
    def treatment(self):
        return self.__treatment

    @treatment.setter
    def treatment(self,treatment):
        if treatment is not None:
            Validator.treatment_validator(treatment)
        self.__treatment = treatment

    #----------------------------------------------------
    # Return visit information
    def __repr__(self):
        return (f"Visit (visit_id = {self.visit_id} ,"
                f" visit_date = {self.visit_date} ,"
                f"reason = {self.reason} ,"
                f"status = {self.status} ,"
                f"vet_id = {self.vet_id} ,"
                f"pet_id = {self.pet_id} ,"
                f"diagnosis = {self.diagnosis} ,"
                f"treatment = {self.treatment})")

    #----------------------------------------------------
    # Convert visit information to tuple
    def to_tuple(self):
        return self.visit_id, self.visit_date, self.reason, self.status, self.vet_id, self.pet_id, self.diagnosis, self.treatment
