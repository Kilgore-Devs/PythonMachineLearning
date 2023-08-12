# Describes how spread out values are. Wish someone would have explained it ike that when I was 14.
# Low std = close to mean.
# High std = values spread out over a wider range.
import numpy
age = [55, 22, 33, 44, 18, 62, 40, 25, 29]

x = numpy.std(age)

print(x)

# Variance is another number that shows how spread out values are.
# SD^2 = variance or sqrt of variance is SD.
# to find the variance -  find the mean(avg of set of nums)
# then find the diff from mean
# for each diff, square it
# then find the average of the squared diffs
age = [55, 22, 33, 44, 18, 62, 40, 25, 29]
y = numpy.var(age)
# detail of SD = sqrt of var
z = numpy.sqrt(y)
print(y)
# detail of SD = sqrt of var
print("Standard deviation is equal to the square rooot of variation.\n"
      "In this case, the variance is: " + str(y) + ". So the standard deviation is: " + str(z) + ".")
