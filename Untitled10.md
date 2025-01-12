```python
import pandas as pd
import seaborn as sns

data = pd.read_csv('cust_churn.csv')
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>customer_id</th>
      <th>credit_score</th>
      <th>country</th>
      <th>gender</th>
      <th>age</th>
      <th>tenure</th>
      <th>balance</th>
      <th>products_number</th>
      <th>credit_card</th>
      <th>active_member</th>
      <th>estimated_salary</th>
      <th>churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15634602</td>
      <td>619</td>
      <td>France</td>
      <td>Female</td>
      <td>42</td>
      <td>2</td>
      <td>0.00</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>101348.88</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15647311</td>
      <td>608</td>
      <td>Spain</td>
      <td>Female</td>
      <td>41</td>
      <td>1</td>
      <td>83807.86</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>112542.58</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15619304</td>
      <td>502</td>
      <td>France</td>
      <td>Female</td>
      <td>42</td>
      <td>8</td>
      <td>159660.80</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>113931.57</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15701354</td>
      <td>699</td>
      <td>France</td>
      <td>Female</td>
      <td>39</td>
      <td>1</td>
      <td>0.00</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>93826.63</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15737888</td>
      <td>850</td>
      <td>Spain</td>
      <td>Female</td>
      <td>43</td>
      <td>2</td>
      <td>125510.82</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>79084.10</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#removing unnecessary columns
data.drop(['customer_id','country'],inplace=True,axis=1)
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>credit_score</th>
      <th>gender</th>
      <th>age</th>
      <th>tenure</th>
      <th>balance</th>
      <th>products_number</th>
      <th>credit_card</th>
      <th>active_member</th>
      <th>estimated_salary</th>
      <th>churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>619</td>
      <td>Female</td>
      <td>42</td>
      <td>2</td>
      <td>0.00</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>101348.88</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>608</td>
      <td>Female</td>
      <td>41</td>
      <td>1</td>
      <td>83807.86</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>112542.58</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>502</td>
      <td>Female</td>
      <td>42</td>
      <td>8</td>
      <td>159660.80</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>113931.57</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>699</td>
      <td>Female</td>
      <td>39</td>
      <td>1</td>
      <td>0.00</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>93826.63</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>850</td>
      <td>Female</td>
      <td>43</td>
      <td>2</td>
      <td>125510.82</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>79084.10</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.gender = [1 if value == "Male" else 0 for value in data.gender]
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>credit_score</th>
      <th>gender</th>
      <th>age</th>
      <th>tenure</th>
      <th>balance</th>
      <th>products_number</th>
      <th>credit_card</th>
      <th>active_member</th>
      <th>estimated_salary</th>
      <th>churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>619</td>
      <td>0</td>
      <td>42</td>
      <td>2</td>
      <td>0.00</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>101348.88</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>608</td>
      <td>0</td>
      <td>41</td>
      <td>1</td>
      <td>83807.86</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>112542.58</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>502</td>
      <td>0</td>
      <td>42</td>
      <td>8</td>
      <td>159660.80</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>113931.57</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>699</td>
      <td>0</td>
      <td>39</td>
      <td>1</td>
      <td>0.00</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>93826.63</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>850</td>
      <td>0</td>
      <td>43</td>
      <td>2</td>
      <td>125510.82</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>79084.10</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10000 entries, 0 to 9999
    Data columns (total 10 columns):
     #   Column            Non-Null Count  Dtype  
    ---  ------            --------------  -----  
     0   credit_score      10000 non-null  int64  
     1   gender            10000 non-null  int64  
     2   age               10000 non-null  int64  
     3   tenure            10000 non-null  int64  
     4   balance           10000 non-null  float64
     5   products_number   10000 non-null  int64  
     6   credit_card       10000 non-null  int64  
     7   active_member     10000 non-null  int64  
     8   estimated_salary  10000 non-null  float64
     9   churn             10000 non-null  int64  
    dtypes: float64(2), int64(8)
    memory usage: 781.4 KB
    


```python
data['churn'].value_counts().plot(kind='bar')
```




    <Axes: xlabel='churn'>




    
![png](output_4_1.png)
    



```python
#divide into target variable and predictors

y = data["churn"] # target 
x = data.drop(["churn"], axis=1)
```

Normalize the data


```python
#Normalize the data as units of the features are different

from sklearn.preprocessing import StandardScaler

#create a scaler object
scaler = StandardScaler()

# fit the scaler to the data and transform the data
X_scaled = scaler.fit_transform(x)
```


```python
X_scaled
```




    array([[-0.32622142, -1.09598752,  0.29351742, ...,  0.64609167,
             0.97024255,  0.02188649],
           [-0.44003595, -1.09598752,  0.19816383, ..., -1.54776799,
             0.97024255,  0.21653375],
           [-1.53679418, -1.09598752,  0.29351742, ...,  0.64609167,
            -1.03067011,  0.2406869 ],
           ...,
           [ 0.60498839, -1.09598752, -0.27860412, ..., -1.54776799,
             0.97024255, -1.00864308],
           [ 1.25683526,  0.91241915,  0.29351742, ...,  0.64609167,
            -1.03067011, -0.12523071],
           [ 1.46377078, -1.09598752, -1.04143285, ...,  0.64609167,
            -1.03067011, -1.07636976]])



Splitting the data


```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.30, random_state=22)


```

Train the data


```python
from sklearn.linear_model import LogisticRegression

#create the model

lr = LogisticRegression()

#train the model on training data
lr.fit(X_train, y_train)

#predict the target variable based on the test data
y_pred = lr.predict(X_test)
```


```python
y_pred
```




    array([0, 1, 0, ..., 0, 0, 0], dtype=int64)



Evaluation


```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy: .2f}")
```

    Accuracy:  0.81
    


```python
from sklearn.metrics import classification_report
print(classification_report (y_test, y_pred))
```

                  precision    recall  f1-score   support
    
               0       0.82      0.96      0.89      2394
               1       0.56      0.18      0.27       606
    
        accuracy                           0.81      3000
       macro avg       0.69      0.57      0.58      3000
    weighted avg       0.77      0.81      0.76      3000
    
    


```python
from sklearn.metrics import confusion_matrix


# Generate the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

```

    [[2309   85]
     [ 497  109]]
    


```python
import matplotlib.pyplot as plt

# Plot confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["Non-Churn", "Churn"], yticklabels=["Non-Churn", "Churn"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

```


    
![png](output_18_0.png)
    



```python

```
