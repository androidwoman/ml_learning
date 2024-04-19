import numpy as np

def cost_function( x, y, theta0, theta1 ):
    m = len(x)  # Number of data points
    total_cost = 0.0

    for i in range(m):
        h_theta = theta0 + theta1 * x[i]
        total_cost += (h_theta - y[i])**2

    cost = (1 / (2)) * total_cost

    
    return cost


def gradient(x, y, theta_0, theta_1):
 
 #with for
#  m = len(x)  # Number of data points
#  d_theta_0, d_theta_1 = 0, 0
#  for i in range(m):
#     h_theta = theta_0 + theta_1 * x[i]
#     d_theta_0 += (h_theta - y[i])
#     d_theta_1 += (h_theta - y[i]) * x[i]


    #withot for
    h_theta = theta_0 + theta_1 * x

    d_theta_0 =   np.sum(h_theta - y)
    d_theta_1 =   np.sum((h_theta - y) * x)
   
    return d_theta_0, d_theta_1




def explicit_answer(x, y):
    """Compute the explicit values of theta1 and theta2

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values

    Returns:
    theta_0  (scalar) intercept of line
    theta_1  (scalar) slope of line
    """
    m = len(x)  # Number of data points
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    sum_x_squared = sum(x_i**2 for x_i in x)

    theta_1 = (m * sum_xy - sum_x * sum_y) / (m * sum_x_squared - sum_x**2)
    theta_0 = (sum_y - theta_1 * sum_x) / m

    return theta_0, theta_1
    
    