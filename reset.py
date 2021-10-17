from coin_exchanger import *

username, password = login('upbit.txt')
user = pyupbit.Upbit(username, password)

renew(user, user.get_balances())
