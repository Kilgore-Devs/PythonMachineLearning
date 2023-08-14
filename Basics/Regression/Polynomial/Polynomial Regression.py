"""
If linear regression, or a straight line through data points, polynomial regression may suffice.
Just like linear regression, polynomial regression uses the relationships between x/y variables to
draw a line through the data points.
"""

# Examples of polcie officer pulling over speeding cars. X = the number of the car, Y = speed.
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
x = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [50, 56, 62, 68, 74, 78, 87, 89, 90, 91, 88, 80, 75, 72, 66, 63, 58, 52, 48]

speedmodel = np.poly1d(np.polyfit(x, y, 3))  # make a polynomial model

regressionline = np.linspace(1, 20, 100)  # how the line is made.
# Starts at car 1, ends at car 20(x1, x20)

speed = speedmodel(7) # will try to predict y value for the given x. or here the speed for the 7th car.

print(speed)  # prints predicted speed
print(r2_score(y, speedmodel(x)))  # print the r squared value. 0-1, 1 = 100% related
plt.scatter(x, y)  # created scatter plot of x and y values
plt.plot(regressionline, speedmodel(regressionline))  # Draw the polynomial regression.
plt.show()  # displays the plots
"""
Examples of a bad fit is if the r2 score is very low or looking at the scatter plot, 
the dots are sporadic and or far from regression line.
"""