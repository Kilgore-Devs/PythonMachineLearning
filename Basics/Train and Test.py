# To determine if the model is fit, use Train/Test.
# Train/Test measures the accuract of a model.
# Two sets: Training 80% | Testing 20 %
# Train the model using a training set and test with a testing set.
# Train means create a set and the test the accuracy of the model.
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(1)
# generating random normal distribution data set of 100 points
x = numpy.random.normal(6, 2, 100)  # mean of 6 and SD of 2
y = numpy.random.normal(300, 80, 100) / x  # mean of 300 and SD 80 divide by x

train_x = x[:80]  # training selection of 80%
train_y = y[:80]

test_x = x[80:]  # test selection of 20%
test_y = y[80:]
# creates polynomial regression model using the training data
regmodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

regline = numpy.linspace(0, 10, 100)
plt.scatter(train_x, train_y)  # display the training set with regression line
plt.plot(regline, regmodel(regline))  # plots regression line
plt.show()

plt.scatter(test_x, test_y)  # display test set with regression line
plt.plot(regline, regmodel(regline))  # plots regression line
plt.show()

plt.scatter(x, y)  # display original data set with regression line
plt.plot(regline, regmodel(regline))  # plots regression line
plt.show()
