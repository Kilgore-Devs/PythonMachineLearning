import numpy
import matplotlib.pyplot as plt

numpy.random.seed(1)  # Set the seed for the numpy random number generator which allows reproducible results.

x = numpy.random.normal(6, 2, 150)  # Gens data from a normal dist with mean 6, SD 2, and 100 elements.
y = numpy.random.normal(250, 80, 150) / x
# ^^^Gens data the same way, but each element is '/' by the corresponding x element.

train_x = x[:80]  # Select the first 80 elements in x/y for training data.
train_y = y[:80]

test_x = x[80:]  # Select the remaining 20 elements in x/y for testing data.
test_y = y[80:]

regmodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 8))  # Gens polynomial model of degree 8 from train data.

regline = numpy.linspace(1, 10, 100)  # Generate 100 evenly-spaced values between 0 and 10.

fig, axs = plt.subplots(3)  # Creates a figure w/3 subplots shown vertically.

colors = x  # Use the the X data to gen colors for each point.
cmap = 'magma'  # Use the 'magma' color map.
hspace: float = .4

# Plots training data on first subplot, with colors derived from 'x' training data.
scatter0 = axs[0].scatter(train_x, train_y, c=colors[:80], cmap=cmap)
axs[0].plot(regline, regmodel(regline), color='red')  # Add regression line to subplot1.
axs[0].set_title('Training Set')  # Set title for first subplot.
axs[0].set_xlabel('Time Spent Shopping', loc="left")  # Label x-axis.
axs[0].set_ylabel('Amount Spent')  # Label  y-axis.
# plt.colorbar(scatter0, ax=axs[0])  # Add colorbar to first subplot.

scatter1 = axs[1].scatter(test_x, test_y, c=colors[80:], cmap=cmap)  # Plots test data, w/colors derived from x data.
axs[1].plot(regline, regmodel(regline), color='red')  # Add regression line to this subplot.
axs[1].set_title('Test Set')  # Set title for this subplot.
axs[1].set_xlabel('Time Spent Shopping', loc="left")  # Label the x-axis.
axs[1].set_ylabel('Amount Spent')  # Label the y-axis.
# plt.colorbar(scatter1, ax=axs[1])  # Add colorbar to second subplot.

scatter2 = axs[2].scatter(x, y, c=colors, cmap=cmap)  # Plots data on this subplot, w/colors derived from the x data.
axs[2].plot(regline, regmodel(regline), color='red')  # Add regression line to this subplot.
axs[2].set_title('Real Data')  # Set title for this subplot.
axs[2].set_xlabel('Time Spent Shopping', loc="left")  # Label the x-axis.
axs[2].set_ylabel('Amount Spent')  # Label the y-axis.
# plt.colorbar(scatter2, ax=axs[2])  # Adds a colorbar to this subplot.

# predicting next event
new_X = numpy.random.normal(6, 2, 1)
predicted_y = regmodel(new_X)
plt.suptitle('My wife at Target')
# Create a new figure just for displaying the prediction text
plt.figure()
plt.text(0.5, 0.5, "Based on the current data:\n On her next trip, My wife will spend spend ${:.2f} "
                   "after being at Target "
                   "for {:.2f} minutes.".format(round(predicted_y[0], 2), round(new_X[0], 2)),
         horizontalalignment='center', verticalalignment='center')
plt.axis('off')  # Turn off axis for a clean window
plt.suptitle('Prediction of next trip to Target')

plt.tight_layout()  # Improve appearance of overall figure layout.
plt.show()  # Display the figures.
