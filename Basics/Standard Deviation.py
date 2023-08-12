# Describes how spread out values are. Wish someone would have explained it ike that when I was 14.
# Low std = close to mean.
# High std = values spread out over a wider range.
import numpy
age = [55, 22, 33, 44, 18, 62, 40, 25, 29]

x = numpy.std(age)

print(x)
