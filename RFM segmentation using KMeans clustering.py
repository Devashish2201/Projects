#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("mc.csv")
data.head()


# In[4]:


data['Frequency'] = data['NumWebPurchases'] + data['NumStorePurchases'] + data['NumCatalogPurchases']

spending_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
data['Monetary'] = data[spending_columns].sum(axis=1)


# In[5]:


#preprocessing for clustering
from sklearn.preprocessing import StandardScaler

# Select RFM features
rfm_features = data[['Recency', 'Frequency', 'Monetary']]

# Handle missing values
rfm_features = rfm_features.fillna(0)

# Scale the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_features)


# In[7]:


#finding optimum number of clusters

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=22)
    kmeans.fit(rfm_scaled)
    wcss.append(kmeans.inertia_)


# In[8]:


# Plot the elbow graph
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


# In[9]:


# choosing 4 as optimal value of clusters
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=22)
data['RFM_Cluster'] = kmeans.fit_predict(rfm_scaled)


# In[10]:


#Analysing the clusters- grouping the customers by their clusters and calculating the avg. R, F, M for each cluster.
#It will help identify 'loyal', 'at-risk', etc.

cluster_analysis = data.groupby('RFM_Cluster')[['Recency', 'Frequency', 'Monetary']].mean()
print(cluster_analysis)



# In[11]:


#Visualizing the clusters

# Using two metrics for visualization
plt.scatter(rfm_scaled[:, 0], rfm_scaled[:, 1], c=kmeans.labels_, cmap='viridis')
plt.title('Customer Segments Based on RFM')
plt.xlabel('Recency (scaled)')
plt.ylabel('Frequency (scaled)')
plt.show()


# In[12]:


plt.scatter(rfm_scaled[:, 1], rfm_scaled[:, 2], c=kmeans.labels_, cmap='viridis')
plt.title('Frequency vs. Monetary')
plt.xlabel('Frequency (scaled)')
plt.ylabel('Monetary (scaled)')
plt.show()


# In[13]:


cluster_labels = {
    0: 'Loyal Customers',
    1: 'Occasional Buyers',
    2: 'At-Risk Customers',
    3: 'Lost Customers'
}
data['RFM_Cluster_Label'] = data['RFM_Cluster'].map(cluster_labels)


# In[16]:


from mpl_toolkits.mplot3d import Axes3D

# 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(rfm_scaled[:, 0], rfm_scaled[:, 1], rfm_scaled[:, 2], c=kmeans.labels_, cmap='viridis')
ax.set_title('RFM Clusters (3D)')
ax.set_xlabel('Recency (scaled)')
ax.set_ylabel('Frequency (scaled)')
ax.set_zlabel('Monetary (scaled)')
plt.show()


# In[19]:


data.to_csv('RFM_segmented_customers.csv', index=False)



# In[ ]:




