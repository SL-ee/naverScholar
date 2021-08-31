import pandas as pd

network = pd.read_excel("D:/listToNetwork_test.xlsx")

# 선언
num = list(range(1, len(network.index))
label = []
weight = []

# 열 개수 df1.shape[1] - 1 열은 1부터
# print(network.shape[1] - 1)

# 297개
for i in range(0, network.shape[0]):
    label.append(network.iloc[i][0])

# 297개
# for i in range(1, network.shape[1]):
#     print(network.iloc[0][i])

for i in range(0, network.shape[0]):
    weight.append(network.iloc[i][i+1])

excel_export = pd.DataFrame(
    {
        'id': num,
        'label': label,
        'index': num,
        'weight': weight
    })

excel_export.to_excel("D:/node.xlsx", header=True, index=False)
