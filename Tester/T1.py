import numpy as np
import matplotlib.pyplot as plt

def my_function(x):
    y = 1 / x
    y[x < 0.0001] = 1891000 # set the y value to 1,891,000 when x is near 0
    return y

# Generate x values from 0 to 1 (excluding 0)
x = np.linspace(0.0001, 27683, 1000000)

# Call the function to generate y values
y = my_function(x)

# Create a plot of the function
plt.plot(x, y)

# Set the x and y axis labels
plt.xlabel('Otros')
plt.ylabel('Cobre')

# Set the title of the plot
plt.title('FPP')

# Show the plot
plt.show()