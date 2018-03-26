import pandas as pd
df=pd.read_csv('../dataset/data.csv')

col=['gender','follower','ask_num','answer_num',
'location','trade','school','company']
df_Blog3=df[col]
print(df_Blog3.shape)
#筛选性别非空
df_Blog3=df_Blog3[pd.notnull(df_Blog3['follower'])]
print(df_Blog3.shape)
#筛选粉丝人数非空
df_Blog3=df_Blog3[pd.notnull(df_Blog3['follower'])]
print(df_Blog3.shape)
#筛选提问数非空
df_Blog3=df_Blog3[pd.notnull(df_Blog3['ask_num'])]
print(df_Blog3.shape)
#筛选回答数非空
df_Blog3=df_Blog3[pd.notnull(df_Blog3['answer_num'])]
print(df_Blog3.shape)
#筛选位置非空
df_Blog3=df_Blog3[pd.notnull(df_Blog3['location'])]
print(df_Blog3.shape)
#筛选行业非空
df_Blog3=df_Blog3[pd.notnull(df_Blog3['trade'])]
print(df_Blog3.shape)
#筛选学校非空
df_Blog3=df_Blog3[pd.notnull(df_Blog3['school'])]
print(df_Blog3.shape)
#筛选公司非空
df_Blog3=df_Blog3[pd.notnull(df_Blog3['company'])]
print(df_Blog3.shape)
df_Blog3.to_csv('../dataset/dataBlog3.csv',header=col,index=False)
print("data preprosessing ok!")
# #筛选男性用户
# df_Blog3_male=df_Blog3[df_Blog3['gender']==1]
# print(df_Blog3_male[:5])
# df_Blog3_male.to_csv('../dataset/dataBlog3_male.csv',header=col,index=False)
# #筛选女性用户
# df_Blog3_female=df_Blog3[df_Blog3['gender']==0]
# print(df_Blog3_female[:5])
# df_Blog3_female.to_csv('../dataset/dataBlog3_female.csv',header=col,index=False)