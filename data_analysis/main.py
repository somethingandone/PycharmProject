import pandas as pd

df = pd.read_excel('sx.xlsx')
data_pos = df.iloc[:, len(df.columns) - 2]
data_neg = df.iloc[:, len(df.columns) - 1]
data_tr = []
j = 0
for i in data_pos:
    if i > data_neg[j]:
        data_tr.append(1)
    elif i == data_neg[j] and i == 1:
        data_tr.append(0)
    elif i < data_neg[j] or (i == data_neg[j] and i > 1):
        data_tr.append(-1)
    j += 1

df['Tr'] = data_tr
df.to_excel('ssx.xlsx', index=False)
