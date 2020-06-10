import sys
sys.path.append(r"E:\A_Project\easytrader")

import easytrader

user = easytrader.use("ht_client")
user.prepare(user='*',
             password='*',
             exe_path = r"D:\htzqzyb2\xiadan.exe",
             comm_password='*')
user.get_exchangebill()