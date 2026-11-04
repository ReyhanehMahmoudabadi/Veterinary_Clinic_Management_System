from data_access.vet_da import VetDa
from model.vet import Vet
from business_logic.vet_bl import VetBL
from controller.vet_controller import VetController


# test passed
# vet_1=Vet("ali","alipour","0550255265","09195263654","lkkk gg","454565656",5542)
# print(vet_1)
# print(vet_1.to_tuple())


# test passed
# vet_1 = Vet("ziba","rad","2112541657","9665362145","dermatology",'55444447',2255)
# vet_2=Vet('ali','alipour','2545693651','09125636545','dermatology','5544367',2258887)
# print(vet_1)
# print(vet_2)
#
# vet_da = VetDa()
# # vet_da.save(vet_1)
# # vet_da.save(vet_2)
# print(vet_da.find_all())


# test passed
# vet_1 = Vet("ali", "alipour", "2545693651",
#             "09125636545", "dermatology", "5544367", 2258887)
# vet_2 = Vet("ziba", "rad", "2112541657",
#             "9665362145", "dermatology", "55444447", 2258888)
# vet_3 = Vet("sara", "moradi", "0445879654",
#             "9585263456", "surgery", "5544368", 2258887)
# vet_bl = VetBL()
# print(vet_bl.save_vet(vet_1))
# print(vet_bl.save_vet(vet_2))
# print(vet_bl.save_vet(vet_3))



#test passed
# controller = VetController()
# success, message = controller.save("ali", "alipour", "2545693651",
#             "09125636545", "dermatology", "5544367", 2258887)
# print(success)
# print(message)
# success, vet_list = controller.find_all()