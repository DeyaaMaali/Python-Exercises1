# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:43:02 2019

@author: OJO3
"""

import pandas as pd
import numpy as np
# =============================================================================
# data = [100, 120, 140, 180, 200, 210, 214]
# s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# =============================================================================
# =============================================================================
# print("head :",s.head())
# print("mean :",s.mean()) 
# print("std :",s.std())
# print( s.agg(['sum','max']))
# s.plot()
# =============================================================================

# =============================================================================
# s = pd.Series([100, 120, 140, 180, 200, 210, 214]) 
# print(s) 
# s2=s.apply( lambda x: x if x > 180 else x*10 ) 
# print (s2)
# =============================================================================


# =============================================================================
# dates = pd.date_range('20190101', periods=8)
# df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))
# print(df.head())
# print(df['P'])
# print(df[0:1])
# print(df[['P','Q']])
# print(df.iloc[1:3, :])
# 
# df.to_excel('PandaTest.xlsx', sheet_name = 'testing', index = True)
# df.to_csv('myDataFrame.csv', sep='\t')
# =============================================================================


# =============================================================================

# Q1

# =============================================================================

# =============================================================================

# data = [2,4,6,8,10]

# s = pd.Series(data)

# print(s)

# =============================================================================





# =============================================================================

# Q2

# =============================================================================

# =============================================================================

# d1={"A":1,"B":2,"C":3,"D":3,"E":4}

# s = pd.Series(d1)

# print(s)

# 

# =============================================================================



# =============================================================================

# Q3

# =============================================================================



# =============================================================================
# =============================================================================
# 
# Data=[20,10,150,110,100,50]
# 
# s=pd.Series(Data)
# 
# print(s.describe())
# 
# s.plot(kind="bar", color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
# =============================================================================






# =============================================================================

# Q4

# =============================================================================

# =============================================================================

# Data = {'d1':[100,200,5,400,700,100,200,50,400,700],'d2':[140,0,300,400,200,140,0,700,400,200]  }

# s = pd.DataFrame(Data)

# print(s.describe())

# s.plot()

# =============================================================================





# =============================================================================

# Q5

# =============================================================================

# =============================================================================

# data={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

# s=pd.DataFrame(data)

# print(s)

# =============================================================================



# =============================================================================

# Q6

# =============================================================================

# =============================================================================

# names = ['Bob','Jessica','Mary','John','Mel']

# births = [968, 155, 77, 578, 973]

# s=pd.Series(births,index=names)

# print(s)

# s.plot.pie(y='births', figsize=(5, 5))

# =============================================================================



# =============================================================================

# Q7

# =============================================================================



# =============================================================================

# d = [1,2,3,4,5,6,7,8,9]

# df= pd.DataFrame(d, columns = ['Number'])

# df.to_csv('myDataFrame.csv', sep='\t')

# df= pd.read_csv('myDataFrame.csv',sep='\t',index_col=0)

# print(df)

# 

# =============================================================================



# =============================================================================

# Q8

# =============================================================================

# =============================================================================
# dates =pd.date_range('20000101', periods=4)
# 
# df= pd.DataFrame(np.random.randn(4, 2), index=dates, columns=["A","B"])
# 
# print(df)
# 
# print(df.head(2))
# 
# print(df[['A']])
# 
# print(df[0:1]) 
# 
# print(df['20000102':'20000104'])
# 
# print(df.loc['20000102':'20000104', ["A"]])
# 
# print(df.iloc[:,1:2])
# 
# print(df[df>0])
# 
# print(df[df.B>0])
# 
# df["A"]=[100,200,300,100]
# 
# print(df)
# 
# print(df[df['A'].isin([200,300])])
# =============================================================================













