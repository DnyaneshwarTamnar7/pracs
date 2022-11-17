import pandas as pd

df = pd.read_csv("E:/BE Notes (Studey Material)/BE StudyMaterial/Macine Learning/MLPractical/diabetes.csv")

X = df.drop(['Outcome'],axis=1)
Y=df['Outcome']

from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
X=sc.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=.2,random_state=42)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

y_pred=knn.predict(X_test)

from sklearn.metrics import confusion_matrix
tn,fp,fn,tp=confusion_matrix(y_test,y_pred).ravel()
print("\nTrue Negative : ",tn)
print("\nFalse Positive : ",fp)
print("\nFalse Negative : ",fn)
print("\nTrue Positive : ",tp)

print(confusion_matrix(y_test,y_pred))

Accuracy = (tn+tp)*100/(tp+tn+fp+fn)
print("\nAccuracy {:.2f}".format(Accuracy))

Precision = tp/(tp+fp)
print("\nPrecision {:.2f}".format(Precision))

Recall = tp/(tp+fn) 
print("\nRecall {:.2f}".format(Recall))

err = (fp+fn)/(tp+tn+fn+fp)
print("\nError rate {:.2f}".format(err))