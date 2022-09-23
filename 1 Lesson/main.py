import numpy as np
import scipy.integrate as integrate


def integrand1(x):
    return 4*np.sin(x)-3

def integrand2(x,y):
    return x**2+y**2

area = integrate.quad(integrand1, 0, 5)
print('Значения 1-ого интеграла:')
print(area)

area = integrate.dblquad(
    integrand2,
    0, 1,
    lambda x: 0, 1
)
print('Значения 2-ого интеграла:')
print(area)