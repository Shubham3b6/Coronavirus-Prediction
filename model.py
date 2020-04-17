import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn import tree

data = pd.read_csv('Covid_dataset.csv')


data_x = data.iloc[:,0:-1].values
data_y = data.iloc[:,-1].values
#print(data_y)

X_train,X_test,y_train,y_test = train_test_split(data_x,data_y,test_size=0.3,random_state=0)

reg = tree.DecisionTreeClassifier()
reg.fit(data_x,data_y)

print("Train Score:", reg.score(X_train,y_train))
print("Test Score:", reg.score(X_test,y_test))


pickle.dump(reg, open('covid.pkl','wb'))

model = pickle.load(open('covid.pkl','rb'))
print(model.predict([[17,99.03,	0 ,0 ,1	]]))
