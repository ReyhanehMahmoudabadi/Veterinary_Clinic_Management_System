from controller.pet_controller import PetController
from data_access.pet_da import PetDa
from data_access.owner_da import OwnerDa
from model.pet import Pet
from model.owner import Owner
from datetime import date
from business_logic.pet_bl import PetBL
from business_logic.owner_bl import OwnerBL


# Test passed
# owner_da = OwnerDa()
# owner_1 = Owner("fatima", "mohseni", "0120541254",
#                 "09985425612", 11, "tehran")
# owner_2 = Owner("fatima", "mohseni", "0120541254",
#                 "09985425612", 22, "tehran")
# # owner_da.save(owner_1)
# # owner_da.save(owner_2)
# print(owner_da.find_all())
#

# Test passed
# pet_1 = Pet(
#     'P2001', 'Boby', 'dog', 'German Shepherd',
#     'male', date(2025, 8, 8), 35.5, 22,
#     '252565141259139')
# pet_2 = Pet(
#     'P2002', 'Luna', 'cat', 'Persian',
#     'female', date(2024, 5, 10), 4.5, 999,
#     '252565141259140')
# pet_3 = Pet(
#     'P2001', 'Max', 'dog', 'Labrador',
#     'male', date(2024, 6, 10), 25.5, 22,
#     '252565141259141')
# pet_bl = PetBL()
# print(pet_bl.save_pet(pet_1))
# print(pet_bl.save_pet(pet_2))
# print(pet_bl.save_pet(pet_3))



# test passed
# controller = PetController()
# success, message = controller.save('P2001', 'Boby', 'dog','German Shepherd',
#     'male', date(2025, 8, 8), 35.5, 22,
#     '252565141259139')
# print(success)
# print(message)
# success, pet_list = controller.find_all()
# print(success)
# print(pet_list)