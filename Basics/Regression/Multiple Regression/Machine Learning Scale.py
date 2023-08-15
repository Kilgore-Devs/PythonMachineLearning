# Should scale values if they are difficult to compare, ir: Altitude to time, and weight to distance.
# Standardization can accomplish this.
# Standardization formula: z = (x - u) / s

# z = new value | x = original value | u = mean | s = standard deviation
# sklearn will do this for you
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
# kept getting numerous errors.
# predicted CO2 is off by 10 according to w3schools material.
# Didn't change any of the data
