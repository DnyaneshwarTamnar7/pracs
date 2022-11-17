import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:/BE Notes (Studey Material)/BE StudyMaterial/Macine Learning/MLPractical/sales_data_sample.csv")

x=df.iloc[:,[1,4]].values

wcss_list = []

from sklearn.cluster import KMeans
for i in range(1,11):
    kmeans= KMeans(n_clusters=i,init="k-means++", random_state=42)
    kmeans.fit(x)
    wcss_list.append(kmeans. inertia_)
    
plt.plot(range(1,11),wcss_list)
plt.title("Elbow Method Graph")
plt.xlabel("Number of clusters")
plt.ylabel("wcss_list")
plt.show()

kmeans=KMeans(n_clusters=3,init="k-means++",random_state=42)
y_pred=kmeans.fit_predict(x)

plt.scatter(x[y_pred==0,0],x[y_pred==0,1],c='blue',label='Cluster1')
plt.scatter(x[y_pred==1,0],x[y_pred==1,1],c='green',label='Cluster2')
plt.scatter(x[y_pred==2,0],x[y_pred==2,1],c='red',label='cluster3')
plt.title("K-Means Clustering")
plt.xlabel("Quantity Ordered")
plt.ylabel("Sales")
#plt.legend()
plt.show()