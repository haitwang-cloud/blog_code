import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
N=50
df=pd.read_csv('../dataset/dataBlog2.csv')
list1=[]
for name,group in df.groupby('location'):
    if len(group)>500:
        vet_1=[]
        vet_1.append(name)
        vet_1.append(group['ask_num'].sum())
        vet_1.append(group['follower'].sum())
        vet_1.append(group['following'].sum())
        vet_1.append(group['agree_num'].sum())
        vet_1.append(group['answer_num'].sum())
        # print(name,'ask_num',group['ask_num'].sum())
        # print(name,'follower',group['follower'].sum())
        # print(name,'following',group['following'].sum())
        # print(name,'agree_num',group['agree_num'].sum())
        # print(name,'answer_num',group['answer_num'].sum())
        # print(vet_1)
        list1.append(vet_1)
location_col=['location','ask_num','follower','following','agree_num','answer_num']
df_location=pd.DataFrame(data=list1,columns=location_col)
df_location=df_location.sort_values('follower',ascending=False)
print(df_location)
df_location.to_csv('../dataset/dataBlog2Location.csv',header=location_col,index=False)
print("data preprosessing ok!")

list2=[]
for name,group in df.groupby('school'):
    if len(group)>50:
        vet_2=[]
        vet_2.append(name)
        vet_2.append(group['ask_num'].sum())
        vet_2.append(group['follower'].sum())
        vet_2.append(group['following'].sum())
        vet_2.append(group['agree_num'].sum())
        vet_2.append(group['answer_num'].sum())
        # print(name,'ask_num',group['ask_num'].sum())
        # print(name,'follower',group['follower'].sum())
        # print(name,'following',group['following'].sum())
        # print(name,'agree_num',group['agree_num'].sum())
        # print(name,'answer_num',group['answer_num'].sum())
        # print(vet_1)
        list2.append(vet_2)
school_col=['school','ask_num','follower','following','agree_num','answer_num']
df_school=pd.DataFrame(data=list2,columns=school_col)
df_school=df_school.sort_values('follower',ascending=False)
print(df_school)
df_school.to_csv('../dataset/dataBlog2School.csv',header=school_col,index=False)
print("data preprosessing ok!")

list3=[]
for name,group in df.groupby('trade'):
    if len(group)>100:
        vet_3=[]
        vet_3.append(name)
        vet_3.append(group['ask_num'].sum())
        vet_3.append(group['follower'].sum())
        vet_3.append(group['following'].sum())
        vet_3.append(group['agree_num'].sum())
        vet_3.append(group['answer_num'].sum())
        # print(name,'ask_num',group['ask_num'].sum())
        # print(name,'follower',group['follower'].sum())
        # print(name,'following',group['following'].sum())
        # print(name,'agree_num',group['agree_num'].sum())
        # print(name,'answer_num',group['answer_num'].sum())
        # print(vet_1)
        list3.append(vet_3)
trade_col=['trade','ask_num','follower','following','agree_num','answer_num']
df_trade=pd.DataFrame(data=list3,columns=trade_col)
df_trade=df_trade.sort_values('follower',ascending=False)
print(df_trade)
df_trade.to_csv('../dataset/dataBlog2trade.csv',header=trade_col,index=False)
print("data preprosessing ok!")
