import pandas as pd
import re
df=pd.read_csv('../dataset/dataset.csv')

col=['gender','company','school','job','location']
company_list=["腾讯",'百度','美团','京东','网易','DJI 大疆创新 ','Facebook','IBM','ZTE 中兴','亚马逊 (Amazon.com)',
              '阿里巴巴','饿了么','微软','华为','今日头条','优步（Uber）','去哪儿（Qunar）','哔哩哔哩',
              '小米','新浪','搜狐','360','京东商城','唯品会','大众点评','奇虎 360','小米科技','微软亚洲研究院'
              '亚马逊','Google','阿里','Cisco（思科）','微软（Microsoft）','搜狗','携程','支付宝','新浪微博',
              '滴滴出行','科大讯飞','美团网','英特尔 (Intel)','苹果公司 (Apple Inc.)','蘑菇街','豆瓣','阿里巴巴集团',
              '阿里云','魅族科技']
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
data_job=[]
for index,row in df_job.iterrows():
    vet=[]
    if row['company'] in company_list:
        #print(index, row['company'])
        vet.append(row['gender'])
        vet.append(row['company'])
        vet.append(row['school'])
        vet.append(row['job'])
        vet.append(row['location'])
        print(vet)
        data_job.append(vet)
data_job=pd.DataFrame(data_job)

data_job.to_csv('../dataset/dataJob.csv',header=col)
#
# C_list=[]
# N_list=[]
# for name,group in df_job.groupby('company'):
#     if len(group)>30:
#         print(name,len(group))
#
# #     if name in company_list:
# #         print(name,":",len(group))
# #         C_list.append(name)
# #         N_list.append(len(group))
# # print(C_list,len(N_list))

