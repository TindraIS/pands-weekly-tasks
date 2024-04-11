'''
----------------------------------------------------------------------
Name: plottask.py
Description: 
    This program displays: 
    (1) a histogram of a normal distribution of a 1000 values with a mean of 5 
    and standard deviation of 2.
    (2) a plot of the function h(x)=x3 in the h_function 0 to 10 on the one set of axes.
Author: Irina Simoes
Date created: 06/04/2024
Version: 1.0
References:
    * https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
    * https://www.geeksforgeeks.org/python-h_function-function/
    * https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf
    * https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html
    * https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots
    * https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions
    * https://matplotlib.org/stable/users/explain/colors/colors.html#sphx-glr-users-explain-colors-colors-py
    * https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers

----------------------------------------------------------------------
''' 

import numpy as np
import matplotlib.pyplot as plt

# Generate list of 1000 values with numpy with a mean of 5 and a std of 2
# As Ian had already showed us in one of the lectures the random module and the different distributions,
# I went straight to the official documentation
normal_values_list = np.random.normal(5,2,1000) 
#print(normal_values_list)

# Get the function h_function values
h_function_list = []
for number in range(0,11): # Set the range ending in 11 in order to get 10 valies
    value = number ** 3
    h_function_list.append(value)

# Following matplotlib sample code referenced above, create a figure and only one axis of the subplot
fig, ax1 = plt.subplots()

# Create the histogram with the distribution of the normal values
color = '#01153E'
ax1.set_xlabel('Values in Common',fontsize=8)                           # Set x-label which will be shared for both normal_values_list and h_function_list    
ax1.set_ylabel('Normal Distribution Values', color=color, fontsize=8)   # Set y-label normal_values_list    
ax1.hist(normal_values_list, 
         bins=10, 
         edgecolor='white', 
         alpha=0.9,
         label='Normal Distribution List', 
         color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Instantiate the second axes for the h(x) function which shares the same x-axis 
ax2 = ax1.twinx()  

# Create the plot with the h(x) function
color = 'tomato'
ax2.set_ylabel('$h(x)$ Values', color=color, fontsize=8)                # Set label only for the other y axis, as the x-label has been handled in ax1
ax2.plot(h_function_list, 
         color=color, 
         alpha=0.7,
         linestyle='--', 
         marker='H', 
         label='$h(x) = x^3$ Function')
ax2.tick_params(axis='y', labelcolor=color)

# Customize the plot
plt.title('Normal Distribution and $h(x) = x^3$ Function\n')
fig.tight_layout() # Otherwise the right y-label is slightly clipped

# Show the plot
plt.show()