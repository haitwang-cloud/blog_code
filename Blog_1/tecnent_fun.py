import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('../dataset/data.csv')

col=['gender','company','school','job','location']

df_job=df[col]
print(df_job.shape)
#筛选公司非空值
df_job=df_job[pd.notnull(df_job['company'])]
print(df_job.shape)
#筛选学校非空值
df_job=df_job[pd.notnull(df_job['school'])]
print(df_job.shape)
# df_job=df_job[pd.notnull(df_job['job'])]
# print(df_job.shape)
company_list=["腾讯",'阿里','百度','美团','京东','网易',
              '阿里巴巴','饿了么','微软','谷歌','华为',
              '小米','ebay','新浪','苏宁','搜狐','360'
              ,'36氪','AcFun','Alibaba','Amazon','Apple'
              ,'Google','亚马逊','京东商城','UC','滴滴','ctrip']
for name,group in df_job.groupby('company'):
    if name in company_list:
        print(name,":",len(group))

    # print(name)
    # print(group)
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 55, 10]
explode = (0, 0.1, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()