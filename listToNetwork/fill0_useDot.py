import pandas as pd

df = pd.read_excel('D:/paperslist_test.xlsx', "DB 피벗")

df_1 = df.fillna(0)
df_2 = df_1.set_index("저자")
df_3 = df_2.dot(df_2.T)

df_3.to_excel("D:/listToNetwork_test.xlsx")
