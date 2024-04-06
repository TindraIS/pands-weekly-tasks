'''
----------------------------------------------------------------------
Name: plottask.py
Description: 
    This program displays two subplots: 
    (1) a histogram of a normal distribution of a 1000 values with a mean of 5 
    and standard deviation of 2.
    (2) a plot of the function h(x)=x3 in the range 0 to 10.
Author: Irina Simoes
Date created: 06/04/2024
Version: 1.0
References:
    * https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
----------------------------------------------------------------------
''' 

import numpy as np

# Generate list of 1000 values with numpy with a mean of 5 and a std of 2
values_list = np.random.normal(5,2.5,1000) 
print(values_list)