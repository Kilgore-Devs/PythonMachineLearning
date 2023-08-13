import numpy as np
import matplotlib.pyplot as plt
# crete random set of number, low=1, high=10, size=200000(different values)
x = np.random.uniform(1, 50, 200000)

plt.hist(x, 100)  # 100 is how many bars on histogram
plt.show()

# normal data distribution aka Gaussian data distro aka bell curve - concentrated around a certain value.
# Here, the mean is 10 and most stays within +-1 from mean
y = np.random.normal(10.0, 1.0, 200000)
plt.hist(y, 200)
plt.show()

# Using scatter plots with random datasets.
# Numbers are concetrated around (10, 20) and spread out more on y axis.
a = np.random.normal(10, 2, 5000)
b = np.random.normal(20, 4, 5000)

plt.scatter(a, b)
plt.show()

D