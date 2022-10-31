import numpy as np
import matplotlib.pyplot as plt

# This script represent the Runge-Kutta method for the equation y'=ln(y)
# With initial value y(1)=2 : 1<=x<=2

# Define here your initial vals
y = 2
x = 1
h = 0.2

# This is where the calculated values are store
y_vals = []

x_vals = []


# Define your function here
def func(x=0, y=0):
    return np.log(y)


# 'x' and 'y' are the initial values (x1,y1)
# jump is the h
def calculate_yns(y, jump, x, up_limit):
    x += jump
    if x > up_limit:
        return

    k1 = func(y=y)
    k2 = func(y=y + (0.5 * h * k1))
    k3 = func(y=y + (0.5 * jump * k2))
    k4 = func(y=y + (h * k3))
    yn = y + (0.5 / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
    x_vals.append(x)
    y_vals.append(yn)

    # Recursive call to calculate the next point using the previous one
    calculate_yns(yn, jump, x, up_limit)


calculate_yns(y, h, x, 2)

plt.plot(x_vals,y_vals)
plt.show()
print(y_vals)
