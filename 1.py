import pandas as pd
import numpy as np 
import matplotlib as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


employers = ['ahmed','sara','younes','achraf','ayoub','mohamed','wissam','taha','khaled','hamza']
grades_logic = [44,11,60,99,54,20,47,81,32,59]
grades_open = [77,41,57,91,23,38,59,26,37,41]
grades_help = [91,77,11,22,33,21,23,63,52,41]
beahvior = ['good','bad','average','excellent','average','bad','average','excellent','average','average']
absence = [2,3,0,1,2,4,1,0,3,2]
issues = [1,0,0,0,1,1,0,0,1,0]

df = pd.DataFrame(
    {
        'employers':employers,
        'grades_logic' :grades_logic,
        'grades_open' :grades_open,
        'grades_help':grades_help,
        'beahvior':beahvior,
        'absence':absence,
        'issues' : issues
    }
)
# df.to_csv('employers_data.csv' , index=False)


le = LabelEncoder()
df['beahvior_Numeric'] = le.fit_transform(df['beahvior'])
x = df[['grades_logic','grades_open','grades_help','absence','issues']]
y = df['beahvior_Numeric']

X_train , X_test , Y_train , Y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)

new_employers = {
        'grades_logic' :60,
        'grades_open' :50,
        'grades_help':60,
        'absence':3,
        'issues' : 3
}

new_employers = pd.DataFrame([new_employers])

new_employers_predetc = model.predict(new_employers)

convert = le.inverse_transform(new_employers_predetc)

print(f'the beahvior of the new student is : {convert[0]}')