# Annie Sauer
# October 24, 2018

import matplotlib.pyplot as plt
import numpy as np

# Create Newton Method function
def newton_method(x0, t, n, f, g):
  # INPUTS
  # x0: initial guess
  # t: tolerance
  # n: maximum number of iterations
  # f: function f(x)
  # g: derivative of f(x)
  # OUTPUTS
  # Estimated x value such that f(x) = 0
  # Tolerance (t)
  # Scatter plot of iteration values
  
  # Initialize vector of iterations and count
  x_iterations = [x0]
  count = 0
  while (f(x0) > t or f(x0) < -t):
    # Update estimate
    x0 = x0 - f(x0)/g(x0)
    # Add one to count
    count = count + 1
    # Add updated estimate to iteration vector
    x_iterations.append(x0)
    # Break loop if maximum number of iterations is reached
    if count >= n:
      print('Maximum Iterations Reached')
      break
  # Print x and t
  print('Estimated zero at x = ', x0)
  print('Tolerance = ', t)
  print('Number of Iterations = ', count)
  return(x_iterations)

# Original function f(x)
def f(x):
  return(3**(x) - np.sin(x) + np.cos(5*x))

# Derivative function g(x)
def g(x):
  return(np.log(3)*3**(x) - np.cos(x) - 5*np.sin(5*x))

# Initial guess
x0 = 1

# Tolerance
t = 0.0001

# Maximum number of iterations
n = 1000

# Call function
x_iterations = newton_method(x0,t,n,f,g)

# Plot
plt.plot(range(len(x_iterations)), x_iterations)
