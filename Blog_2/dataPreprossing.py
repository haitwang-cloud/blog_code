import pandas as pd
import re
df=pd.read_csv('../dataset/dataset.csv')

col=['follower','following','agree_num',
    'ask_num','answer_num','location','trade','school']
df_Blog2=df[col]
print(df_Blog2.shape)
#筛选粉丝人数非空
df_Blog2=df_Blog2[pd.notnull(df_Blog2['follower'])]
print(df_Blog2.shape)
#筛选关注人数非空
df_Blog2=df_Blog2[pd.notnull(df_Blog2['following'])]
print(df_Blog2.shape)
#筛选赞同数非空
df_Blog2=df_Blog2[pd.notnull(df_Blog2['agree_num'])]
print(df_Blog2.shape)
#筛选提问数非空
df_Blog2=df_Blog2[pd.notnull(df_Blog2['ask_num'])]
print(df_Blog2.shape)
#筛选回答数非空
df_Blog2=df_Blog2[pd.notnull(df_Blog2['answer_num'])]
print(df_Blog2.shape)
#筛选位置非空
df_Blog2=df_Blog2[pd.notnull(df_Blog2['location'])]
print(df_Blog2.shape)
#筛选行业非空
df_Blog2=df_Blog2[pd.notnull(df_Blog2['trade'])]
print(df_Blog2.shape)
#筛选学校非空
df_Blog2=df_Blog2[pd.notnull(df_Blog2['school'])]
print(df_Blog2.shape)

df_Blog2.to_csv('../dataset/dataBlog2.csv',header=col,index=False,encoding='utf-8')
print("data preprosessing ok!")