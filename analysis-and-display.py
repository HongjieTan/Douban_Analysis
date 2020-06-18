#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
path = '../Douban_Analysis/book_list.xlsx'
sheet1 = '机器学习'
sheet2 = '计算机'
sheet3 = 'linux'
sheet4 = '数据库'
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
df1 = pd.read_excel(path,sheet_name = sheet1)
df2 = pd.read_excel(path,sheet_name = sheet2)
df3 = pd.read_excel(path,sheet_name = sheet3)
df4 = pd.read_excel(path,sheet_name = sheet4)
print("数据总行数".center(44,'='))
print(len(df1)+len(df2)+len(df3)+len(df4))
print((sheet1+"类数据行数").center(44,'|'))
print(len(df1))
print((sheet2+"类数据行数").center(44,'|'))
print(len(df2))
print((sheet3+"类数据行数").center(44,'|'))
print(len(df3))
print((sheet4+"类数据行数").center(44,'|'))
print(len(df4))


# In[38]:


def f(x):
 return x.replace("作者/译者： ","",1)
df1['作者'] = df1['作者'].map(f)
df2['作者'] = df2['作者'].map(f)
df3['作者'] = df3['作者'].map(f)
df4['作者'] = df4['作者'].map(f)
def f(x):
    return x.replace('出版信息：',"",1).split('/')[0]
df1['出版社'] = df1['出版社'].map(f)
df2['出版社'] = df2['出版社'].map(f)
df3['出版社'] = df3['出版社'].map(f)
df4['出版社'] = df4['出版社'].map(f)
print((sheet1+"类丢弃缺失项后的数据行数").center(44,'|'))
df1


# In[89]:


print(评价人数大于500的书籍".center(44,'='))
print((sheet1+"类").center(44,'|'))
print(df1[df1['评价人数']>500][['序号','书名','评分','评价人数']])
print((sheet2+"类").center(44,'|'))
print(df2[df2['评价人数']>500][['序号','书名','评分','评价人数']])
print((sheet3+"类").center(44,'|'))
print(df3[df3['评价人数']>500][['序号','书名','评分','评价人数']])
print((sheet4+"类").center(44,'|'))
print(df4[df4['评价人数']>500][['序号','书名','评分','评价人数']])


# In[106]:


print(评价最好的十本书".center(44,'='))
print((sheet1+"类").center(44,'|'))
print(df1[df1['评价人数']>0].nlargest(10,'评分')[['序号','书名','评分','评价人数']])
print((sheet2+"类").center(44,'|'))
print(df2[df2['评价人数']>0].nlargest(10,'评分')[['序号','书名','评分','评价人数']])
print((sheet3+"类").center(44,'|'))
print(df3[df3['评价人数']>0].nlargest(10,'评分')[['序号','书名','评分','评价人数']])
print((sheet4+"类").center(44,'|'))
print(df4[df4['评价人数']>0].nlargest(10,'评分')[['序号','书名','评分','评价人数']])


# In[19]:


df1.drop('序号', axis=1, inplace=True)
df2.drop('序号', axis=1, inplace=True)
df3.drop('序号', axis=1, inplace=True)
df4.drop('序号', axis=1, inplace=True)
df1['类别'] = sheet1
df2['类别'] = sheet2
df3['类别'] = sheet3
df4['类别'] = sheet4
df = pd.concat([df1,df2,df3,df4])
df = df[df['评价人数']>0]


# In[188]:





# In[169]:


print("按评价人数和评分降序".center(44,'|'))
print(df[df['评价人数']>0].sort_values(by=['评价人数','评分'],ascending=False)[['书名','评分','评价人数','类别']])


# In[170]:


print("按类别分组查看".center(44,'|'),)
print(df.groupby("类别").describe())


# In[20]:


listBins = [0, 10, 30, 60, 100, 200, 500, 100000]
listLabels = ['0_10','11_30','31_60','61_100','101_200','201_500','501<']
df['评价人数'] = pd.cut(df['评价人数'], bins=listBins, labels=listLabels, include_lowest=True)


# In[172]:


print("各类别在各评价人数段的评分".center(44,'|'),)
print(pd.crosstab(df.类别,df.评价人数,df.评分,aggfunc='mean'))


# In[32]:


df_group = pd.crosstab(df.类别,df.评价人数,df.评分,aggfunc='mean')
df_group.plot(kind='bar')
font = fm.FontProperties(fname=r'C:/Windows/Fonts/bahnschrift.ttf')
plt.xlabel('各类别在各评价人数段评分分布',FontProperties='simhei')
plt.xticks(FontProperties='simhei')
plt.legend(prop=font)
plt.show()


# In[ ]:





# In[4]:


listBins = [0, 2, 4, 6, 8, 10]
listLabels = ['1星级','2星级','3星级','4星级','5星级']
df['评分'] = pd.cut(df['评分'], bins=listBins, labels=listLabels, include_lowest=True)


# 

# In[8]:


df_group = pd.crosstab(df.类别,df.评分)
print(df_group)
df_group['5星级'].plot.pie(subplots=True,fontsize=20,counterclock=False,startangle=-270)
plt.xlabel('5星级的评分分布',FontProperties='simhei')
plt.xticks(FontProperties='simhei')
plt.show()
df_group['4星级'].plot.pie(subplots=True,fontsize=20,counterclock=False,startangle=-270)
plt.xlabel('4星级的评分分布',FontProperties='simhei')
plt.xticks(FontProperties='simhei')
plt.show()


# In[17]:


df_group = pd.crosstab(df.评分,df.类别,df.评价人数,aggfunc='sum').sum()
df_group.plot.pie(subplots=True,fontsize=20,counterclock=False,startangle=-270)
plt.xlabel('各类别评价人数分布',FontProperties='simhei')
plt.xticks(FontProperties='simhei')
plt.show()

