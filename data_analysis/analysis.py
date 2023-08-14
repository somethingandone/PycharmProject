import pandas as pd

pos = 'Positive'
neg = 'Negative'
change = 'change'
mean_pos = 'mean pos'
mean_neg = 'mean neg'
to_pos = 'ToPos'
to_neg = 'ToNeg'
size_to_pos = 344
size_to_neg = 157
df = pd.read_csv('md.csv')
count = 0
for i in range(len(df)):

    if df[change][i] == to_pos:

        if df[mean_pos][i] == df[pos][i] and df[mean_neg][i] == df[neg][i]*-1:
            count += 1
print(count)
print(float(count/size_to_pos))

