import pandas as pd

ser1 = pd.Series(data=[120, 380, 250, 360], index=['一季度', '二季度', '三季度', '四季度'])
print(ser1)

ser2 = pd.Series({'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})
print(ser2)
