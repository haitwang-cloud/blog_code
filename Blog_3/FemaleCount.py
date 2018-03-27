import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
sns.set_style('whitegrid',{'font.sans-serif':['simhei','Arial']})


df=pd.read_csv('../dataset/dataBlog3_female.csv')
# print(df.info())
#筛选地区
city_list=[]
city_count=[]
for name,group in df.groupby('location'):
    if len(group)>100:
        # print(name,len(group))
        city_list.append(name)
        city_count.append(len(group))
city_dict={
    'city':city_list,
    'count':city_count
}
city_df=pd.DataFrame(city_dict)
city_df=city_df.sort_values('count',ascending=False)[:10]
print(city_df)
# f,ax=plt.subplots(figsize=(40,30))
# sns.barplot(x='city',y='count',data=city_df)
# ax.set_title('女性分布Top10城市',fontsize=30)
# ax.tick_params(axis='x',labelsize=40)
# ax.tick_params(axis='y',labelsize=40)
# plt.show()
#筛选行业
trade_list=[]
trade_count=[]
for name,group in df.groupby('trade'):
    if len(group)>100:
        # print(name,len(group))
        trade_list.append(name)
        trade_count.append(len(group))
trade_dict={
    'trade':trade_list,
    'count':trade_count
}
trade_df=pd.DataFrame(trade_dict)
trade_df=trade_df.sort_values('count',ascending=False)[:10]
print(trade_df)
#筛选学校
school_list=[]
school_count=[]
for name,group in df.groupby('school'):
    if len(group)>100:
        # print(name,len(group))
        school_list.append(name)
        school_count.append(len(group))
school_dict={
    'school':school_list,
    'count':school_count
}
school_df=pd.DataFrame(school_dict)
school_df=school_df.sort_values('count',ascending=False)[:10]
print(school_df)
#筛选公司
company_list=[]
company_count=[]
for name,group in df.groupby('company'):
    if len(group)>10:
        # print(name,len(group))
        company_list.append(name)
        company_count.append(len(group))
company_dict={
    'company':company_list,
    'count':company_count
}
company_df=pd.DataFrame(company_dict)
company_df=company_df.sort_values('count',ascending=False)[:10]
print(company_df)

