import pandas as pd

eth_df = pd.read_csv("Your Path")
labels = []

for i in range(len(eth_df.index)-3):
    if (eth_df['Close'][i+1]>eth_df['Open'][i+1]) and (eth_df['Close'][i+2]>eth_df['Open'][i+2]) and (eth_df['Close'][i+3]>eth_df['Open'][i+3]):
        profit = int(eth_df['Close'][i+3]) - int (eth_df['Close'][i+1])
        base = int (eth_df['Close'][i+1])
        if (profit/base) > 0.1:
            labels = labels + ['1']
        else:
            labels = labels + ['0']
    elif (eth_df['Close'][i+1]<eth_df['Open'][i+1]) and (eth_df['Close'][i+2]<eth_df['Open'][i+2]) and (eth_df['Close'][i+3]<eth_df['Open'][i+3]):
        loss = int(eth_df['Close'][i+1]) - int (eth_df['Close'][i+3])
        base = int (eth_df['Close'][i+1])
        if (loss/base) > 0.1:
            labels = labels + ['-1']
        else:
            labels = labels + ['0']
    else:
        labels = labels + ['0']

labels = labels + ['0','0','0']
lab = pd.Series(labels)
tag = eth_df['Open Time']
df = pd.concat([tag,lab],axis=1)
df.columns = ['Open Time','label']
df.to_csv("Your Path",index=False)
