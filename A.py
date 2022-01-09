
#ML PART
import numpy as np
import pandas as pd
import pickle
#import matplotlib.pyplot as plt
#import seaborn as sns
df=pd.read_csv("heart.csv")
target=df['target']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df.drop(columns='target'),target,test_size=0.25,random_state=42)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
from sklearn.metrics import classification_report as c
from sklearn.linear_model import LogisticRegression as lr
model=lr()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
#print(c(y_test,y_pred))
pickle.dump(model,open('model.pkl','wb'))
model1=pickle.load(open('model.pkl','rb'))
#print(model1.predict([[1,2,3,4,5,6,7,8,9,10,11,12,13]]))
print("Accuracy of our model is :",(model.score(x_test,y_test))*100,"%")