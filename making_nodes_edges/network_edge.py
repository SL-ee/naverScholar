import pandas as pd

network = pd.read_excel("D:/listToNetwork_test.xlsx")

node = pd.read_excel("D:/node.xlsx")

# 선언
source = []
target = []
weight = []

# 저자 번호
node_id = node["id"]
# 저자 이름
node_label = node["label"]

# print(node_id[5])
# print(node_label[5])

# 297개

for i in range(0, network.shape[0]):
# for i in range(0, 1):
    # label.append(network.iloc[i][0])
    for j in range(i + 2, network.shape[1]):
        source.append(node_id[i])
        target.append(node_id[j-1])
        # print(node_id[j-1])
        weight.append(network.iloc[i][j])
        if network.iloc[i][j] > 0 :
            print(node_id[j - 1], node_label[j - 1])
# 297개
# for i in range(1, network.shape[1]):
#     print(network.iloc[0][i])

excel_export = pd.DataFrame(
    {
        'source': source,
        'target': target,
        'weight': weight
    })

excel_export.to_excel("D:/edge.xlsx", header=True, index=False)
