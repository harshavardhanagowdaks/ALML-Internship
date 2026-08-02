import pandas as pd
import os
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

current_folder=os.path.dirname(__file__)
csv_file=os.path.join(current_folder,"student.csv")

df=pd.read_csv(csv_file)

print(df)

X=df[["Hours","Attendance","Assignments"]]
y=df["Pass"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

prediction=model.predict(X_test)

accuracy=accuracy_score(y_test,prediction)

print("\nAccuracy:",accuracy)

hours=float(input("\nStudy Hours: "))
attendance=float(input("Attendance: "))
assignments=float(input("Assignments: "))

result=model.predict([[hours,attendance,assignments]])

if result[0]==1:
    print("\nPrediction : PASS")
else:
    print("\nPrediction : FAIL")

model_path=os.path.join(current_folder,"student_model.pkl")

joblib.dump(model,model_path)

print("\nModel Saved Successfully!")