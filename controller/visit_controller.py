from business_logic.visit_bl import VisitBL
from model.visit import Visit


class VisitController:

    def __init__(self):
        self.visit_bl = VisitBL()

    def save(self, visit_id, visit_date, reason, status,
             vet_id, pet_id, diagnosis=None, treatment=None):
        try:
            visit = Visit(
                visit_id, visit_date, reason, status,
                vet_id, pet_id, diagnosis, treatment
            )
            self.visit_bl.save_visit(visit)
            return True, "Visit Saved!"

        except Exception as e:
            return False, f"Save Failed: {e}"


    def find_all(self):
        try:
            visit_list = self.visit_bl.find_all()
            return True, visit_list
        except Exception as e:
            return False, f"Find Failed: {e}"