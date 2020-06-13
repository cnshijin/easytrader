# -*- coding: utf-8 -*-

import sys
sys.path.append(r"E:\A_Project\easytrader")

import easytrader
import pandas as pd

user = easytrader.use("ht_client")
# 手动登入客户端，自动登入采用明文密码不安全
user.connect()

bill_2017 = user.get_exchangebill_year(2017)
# bill_2020 = user.get_exchangebill_year(2020)

# 将字典转换为 DataFrame
df = pd.DataFrame(bill_2017)

# 去除不需要的行和列

# DataFrame 存储为 Excel 表格
