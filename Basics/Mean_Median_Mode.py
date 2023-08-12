import numpy
# mean = average
# median = mid point
# mode = most common value

# age of 10 people
age = [24, 26, 27, 45, 16, 56, 18, 27, 43, 31]

x = numpy.mean(age)
y = numpy.median(age)
from scipy import stats  # import scipy to use mode
z = stats.mode(age)

print(x, y, z)
