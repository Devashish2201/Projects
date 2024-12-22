#!/usr/bin/env python
# coding: utf-8

# In[32]:


#importing dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


# In[33]:


#Data collection and analysis
cd=pd.read_csv("mc.csv")


# In[34]:


# Checking for missing values
cd.fillna(cd.mean(), inplace=True)  # Fill missing values with column means


# In[ ]:


cd.head()


# In[35]:


cd.shape


# In[36]:


#getting more info
cd.info()


# In[37]:


#checking for missing values
cd.isnull().sum()


# In[38]:


#adding cust_age feature
from datetime import datetime
current_year = datetime.now().year
cd['customer_age'] = current_year - cd['Year_Birth']

cd.head()


# In[39]:


# creating an index map of features
column_indices = list(enumerate(cd.columns))

for index, column_name in column_indices:
    print(f"Index: {index}, Column Name : {column_name}")


# In[51]:


X = cd.iloc[:,[29,0]].values
print(X)


# In[52]:


#choosing number of clusters WCSS -> within clusters sum of squares
#finding wscc value for different number of clusters

wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=22)
    kmeans.fit(X)
    
    wcss.append(kmeans.inertia_)


# In[57]:


#plot an elbow graph

sns.set()
plt.plot(range(1,11), wcss)
plt.title('The Elbow point graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


# In[58]:


#Optimum number of clusters is 3
#training the K-means clustering model

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=96)

#returning a label for each data point based on their cluster
Y = kmeans.fit_predict(X)
print(Y)


# In[59]:


#visualizing the clusters
#plotting all the clusters and their centroids

plt.figure(figsize=(10,10))
plt.scatter(X[Y==0,0], X[Y==0,1], s=50, c='green', label='Cluster 1' )
plt.scatter(X[Y==1,0], X[Y==1,1], s=50, c='red', label='Cluster 2' )
plt.scatter(X[Y==2,0], X[Y==2,1], s=50, c='blue', label='Cluster 3' )

#plot the centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s= 100, c='cyan', label='centroids')

plt.title('Customer age groups')
plt.xlabel('age')
plt.ylabel('customers')
plt.show()


# In[ ]:




