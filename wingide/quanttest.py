# -*- coding: utf-8 -*-

import sys
sys.path.append(r"E:\A_Project\easytrader")

import easytrader
import pandas as pd

user = easytrader.use("ht_client")

# 手动登入客户端，自动登入采用明文密码不安全
user.connect()
user.refresh()

bill_2019 = user.get_exchangebill_year(2019)

# 将字典转换为 DataFrame
df = pd.DataFrame(bill_2019)

# 去除不需要的行和列

# DataFrame 存储为 Excel 表格
wrxl = pd.ExcelWriter("交易清单 2019.xlsx")
df.to_excel(wrxl, '2019 年', index=False)
wrxl.save()
