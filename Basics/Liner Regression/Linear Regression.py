# Regression - trying to find relationship between variables.
# Can be used to predict outcomes of future events.
# Linear regression draws a line though to predict future values.
import matplotlib.pyplot as plt
from scipy import stats
x = [7, 5, 10, 9, 5, 20, 5, 9, 6, 12, 15, 10, 8]
y = [100, 80, 87, 90, 111, 82, 110, 87, 97, 70, 80, 85, 89]

slope, intercept, r, p, std_err = stats.linregress(x, y)  # returns key values of linear regression


def linreg(x):  # uses slope and intercept values to return a new value.
    return slope * x + intercept  # new value reps y


linregmodel = list(map(linreg, x))  # Run each value on x through fx, results in new values for y.
plt.scatter(x, y)
plt.plot(x, linregmodel)  # Draw liniear regression.
plt.show()

