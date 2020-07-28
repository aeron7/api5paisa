
from api5paisa import Api5Paisa

api = Api5Paisa()
api.login("email or clientId", "passowrd", "dob in the format ddMMyyyy")
#for easy access create ~/.5paisa.conf and user api.login()
order_response = api.order('SBIN', 17.15, 1)
print(order_response)
print(api.get_order_book())

