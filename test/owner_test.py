from controller.owner_controller import OwnerController
from data_access.owner_da import OwnerDa
from business_logic.owner_bl import OwnerBL
from model.owner import Owner


# test passed
# owner_1 = Owner("ali","saberi",'0020254589','9925644825',254,"tehran,saadat abad","aliAli@gmail.com")
# print(owner_1)
# print(owner_1.to_tuple())


# test passed
# owner_1=Owner("ali","alipour","0110546587","09125478567",25469,"tehran")
# owner_2=Owner("zahra","mohseni","0120541254","09985425612",25497,"tehran")
# owner_3=Owner("sara","moradi","0445879654","9585263456",255,"isfahan")
# owner_da = OwnerDa()
# owner_da.save(owner_1)
# owner_da.save(owner_2)
# owner_da.save(owner_3)
# print(owner_da.find_all())


# test passed
# owner_1 = Owner("fatima", "mohseni", "0120541254",
#                 "09985425612", 11, "tehran")
# owner_2 = Owner("fatima", "mohseni", "0120541254",
#                 "09985425612", 22, "tehran")
# owner_3 = Owner("sara", "moradi", "0445879654",
#                 "9585263456", 11, "isfahan")
# owner_bl = OwnerBL()
# print(owner_bl.save_owner(owner_1))
# print(owner_bl.save_owner(owner_2))
# print(owner_bl.save_owner(owner_3))


# test passed
# controller = OwnerController()
# success, message = controller.save("ali",  'alizade','2112654699','9256356568',57850000042,'ahvaz')
# print(success)
# print(message)
# success, owner_list = controller.find_all()
# print(success)
# print(owner_list)