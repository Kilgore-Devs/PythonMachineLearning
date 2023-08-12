# Gives a number that describes the value that a given percent of the values are lower than.
# weight of people. What is ith 90 percentile
import numpy as np
weight = [190, 140, 165, 163, 155, 299, 220, 250, 230, 222, 199, 233, 214, 210, 200]
x = np.percentile(weight, 90)  # finds the 90 percetile.
# Meaning that 90% of people are less than the output.
y = np.percentile(weight, 50)  # 50% weighs more than y.
print(x)
print(y)
