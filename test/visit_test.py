from controller.visit_controller import VisitController
from data_access.visit_da import VisitDa
from data_access.pet_da import PetDa
from data_access.vet_da import VetDa
from model.visit import Visit
from model.vet import Vet
from datetime import datetime
from business_logic.visit_bl import VisitBL
from business_logic.vet_bl import VetBL
from controller.vet_controller import VetController


# test passed
# visit_da = VisitDa()
# print(visit_da.find_all())
#
#
# # test passed
# pet_da = PetDa()
# print(pet_da.find_all())
#
#
# # test passed
# vet_da = VetDa()
# print(vet_da.find_all())
#
#
# # test passed
# visit_bl = VisitBL()
# vet_bl = VetBL()


# test passed
# vet_1 = Vet(
#     "ali", "alipour", "2545693651",
#     "09125636545", "dermatology", "5544367", 2258887)
# print(vet_bl.save_vet(vet_1))


# test passed
# visit_1 = Visit(
#     'VIS-101', datetime(2026, 12, 10, 10, 30),
#     'Checkup', 'Scheduled', 2258887, 'P2001')
# visit_2 = Visit(
#     'VIS-102', datetime(2026, 12, 11, 11, 30),
#     'Vaccination', 'Scheduled', 9999999, 'P2001')
# visit_3 = Visit(
#     'VIS-103', datetime(2026, 12, 12, 12, 30),
#     'Surgery', 'Scheduled', 2258887, 'P9999')
# visit_4 = Visit(
#     'VIS-101', datetime(2026, 12, 13, 13, 30),
#     'Checkup', 'Scheduled', 2258887, 'P2001')
## print(visit_bl.save_visit(visit_1))
# print(visit_bl.save_visit(visit_2))
# print(visit_bl.save_visit(visit_3))
# print(visit_bl.save_visit(visit_4))



#test passed
# controller = VisitController()
# success, message = controller.save('VIS-112121201', datetime(2026, 12, 10, 10, 30),
#     'Checkup', 'Scheduled', 2258887, 'P2001')
# print(success)
# print(message)
# find_success, visit_list = controller.find_all()
#
# print(find_success)
# print(visit_list)
