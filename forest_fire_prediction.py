# for numerical computing
import numpy as np

# for dataframes
import pandas as pd


# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")



# to split train and test set
from sklearn.model_selection import train_test_split


# Machine Learning Models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
f#rom sklearn.naive_bayes import GaussianNB



from sklearn.metrics import accuracy_score




df=pd.read_csv('Forest_fire.csv')
#df=df.drop('Area',axis=1)

print(df.shape)
print(df.columns)
print(df.head())
print(df.describe())
print(df.corr())
df = df.drop_duplicates()
print( df.shape )
print(df.isnull().sum())
df=df.dropna()
print(df.isnull().sum())



y = df.Fire_Occurence

# Create separate object for input features
X = df.drop('Fire_Occurence', axis=1)




# Split X and y into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2, random_state=0)


# Print number of observations in X_train, X_test, y_train, and y_test
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)




model1= LogisticRegression()
model2=RandomForestClassifier(n_estimators=100)
model3= KNeighborsClassifier(n_neighbors=3)
model4= SVC()
#model5=GaussianNB()
model6=DecisionTreeClassifier()



#training
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
model3.fit(X_train, y_train)
model4.fit(X_train, y_train)
#model5.fit(X_train, y_train)
model6.fit(X_train, y_train)




## Predict Test set results
y_pred1 = model1.predict(X_test)
y_pred2 = model2.predict(X_test)
y_pred3 = model3.predict(X_test)
y_pred4 = model4.predict(X_test)
#y_pred5 = model5.predict(X_test)
y_pred6 = model6.predict(X_test)





acc1 = accuracy_score(y_test, y_pred1) ## get the accuracy on testing data
print("Accurcay of LogisticRegression is {:.2f}%".format(acc1*100))

acc2 = accuracy_score(y_test, y_pred2)  ## get the accuracy on testing data
print("Accurcay of RandomForestClassifier is {:.2f}%".format(acc2*100))

acc3 = accuracy_score(y_test, y_pred3)  ## get the accuracy on testing data
print("Accurcay of KNeighborsClassifier is {:.2f}%".format(acc3*100))

acc4 = accuracy_score(y_test, y_pred4) ## get the accuracy on testing data
print("Accurcay of SVC is {:.2f}%".format(acc4*100))

#acc5= accuracy_score(y_test, y_pred5)  # get the accuracy on testing data
#print("Accurcay of GaussianNB is {:.2f}%".format(acc5*100))

acc6= accuracy_score(y_test, y_pred6) ## get the accuracy on testing data
print("Accurcay of DecisionTreeClassifier is {:.2f}%".format(acc6*100))



#from sklearn.externals import joblib 
import joblib
# Save the model as a pickle in a file 
joblib.dump(model4, 'forest_fire.pkl') 

  
# Load the model from the file 
final_model = joblib.load('forest_fire.pkl')

pred=final_model.predict(X_test)

acc = accuracy_score(y_test, pred) ## get the accuracy on testing data
print("Accurcay of Final Model is {:.2f}%".format(acc*100))

