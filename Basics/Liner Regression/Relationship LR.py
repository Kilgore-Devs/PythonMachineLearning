# If there is no relationship between the x/y-axis values then linear progression cannot predict.
# Relationship aka coefficient of correlation is call 'r'
# 'r' value ranges from -1 to 1. -1/1 = 100% related. 0 = False or no relationship.
from scipy import stats
import matplotlib.pyplot as plt
a = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
b = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(a, b)  # calls linregress fx using the dataset above.
# This results in variabels conatining the slope, intercept and coefficent.
# 'p' for hypothesis test and and std err of the estimated gradient.


def myfx(x):  # fx to calc the y value for a given x.
    return slope * x + intercept


prediction = myfx(10)  # calls myfx to predict the y value

print(prediction)  # prints prediction

predictionplot = list(map(myfx, a))

plt.scatter(a, b)
plt.plot(a, predictionplot)  # visualize the regression line
plt.show()
# the closer to 1 or -1 means a higher relationship
