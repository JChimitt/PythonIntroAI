from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

df = pd.read_csv('IRIS.csv')
print(df.head())

# look at raw data in scatter plot to determine approximate k value
scatterX = df.drop(['sepal_length', 'sepal_width', 'species'], axis=1).values
plt.scatter(df['petal_length'], df['petal_width'])
plt.xlabel('petal_length')
plt.ylabel('petal_width')

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['petal_length', 'petal_width']])
print(y_predicted)
df['cluster']=y_predicted
print(df.head())
print("Cluster Centeres: ", km.cluster_centers_)

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.petal_length,df1['petal_width'],color='green')
plt.scatter(df2.petal_length,df2['petal_width'],color='red')
plt.scatter(df3.petal_length,df3['petal_width'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.legend()

# problem with bottom two clusters - black data points mixing with green 
# Need to scale features
scaler = MinMaxScaler()
scaler.fit(df[['petal_width']])  # Scales 0 to 1
df['petal_width'] = scaler.transform(df[['petal_width']])

scaler.fit(df[['petal_length']])
df['petal_length'] = scaler.transform(df[['petal_length']])
df.head()

plt.scatter(df.petal_length,df['petal_width'])

# Scale Age as well.
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['petal_length','petal_width']])
y_predicted

df['cluster']=y_predicted
df.head()

print("Centroids after scaling: ",km.cluster_centers_)

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.petal_length,df1['petal_width'],color='green')
plt.scatter(df2.petal_length,df2['petal_width'],color='red')
plt.scatter(df3.petal_length,df3['petal_width'],color='black')
plt.scatter(km.cluster_centers_[:,0],
            km.cluster_centers_[:,1],
            color='purple',marker='*',
            label='centroid')
plt.legend()

# Plot elbow plot
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['petal_length','petal_width']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)
