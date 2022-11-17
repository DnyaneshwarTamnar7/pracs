import pandas as pd
import numpy as np

df=pd.read_csv("E:/BE Notes (Studey Material)/BE StudyMaterial/Macine Learning/MLPractical/emails.csv")

X = df.drop(['Email No.', 'Prediction'], axis=1)
Y = df['Prediction']

from sklearn.preprocessing import MinMaxScaler

sc=MinMaxScaler()

X=sc.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=.2,random_state=20)


from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

y_pred=knn.predict(X_test)

from sklearn.metrics import mean_squared_error,mean_absolute_error,accuracy_score
print("Accuracy {:.2f}".format(accuracy_score(y_test, y_pred)))


from sklearn.svm import SVC
svc=SVC(kernel="rbf",random_state=1)
svc.fit(X_train,y_train)
y_pred=svc.predict(X_test)

print("Accuracy {:.2f}".format(accuracy_score(y_test, y_pred)))