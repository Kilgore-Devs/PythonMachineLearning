"""# Multi Regression is like linear but with more than 1 independent value.
AKA try to predict a value based on more than one variable.
"""
import pandas
from sklearn import linear_model as lm
df = pandas.read_csv("w3data.csv")
X = df[['Weight', 'Volume']]  # list of independent values
y = df["CO2"]
rgr = lm.LinearRegression()  # create linear regression object
rgr.fit(X, y)  # takes independent and dependent values as parameters
# and fills regression object with data that describes the relationship

predictCO2 = rgr.predict([[3300, 1300]])  # predict CO2 emission of a car weighing 3500 and volume of 1900
print(predictCO2)  # prints the prediction
print(rgr.coef_)  # prints the coefficient values of the regression obj
# Coefficient  - factor that describes the relations with an unknown variable
""" This is all from w3 schools. 
Here we ask for the coefficient value of weight against CO2, and for volume against CO2. 
The answer we get tells us what happens if we increase, or decrease, one of the independent values(weight or volume.)
"""