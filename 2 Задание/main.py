import numpy as np
from scipy.integrate import odeint

def f(y, x):
    return x/5

y0 = 1.0
step = 10
x_output = np.linspace(0, 2, step)
y_result = odeint(f, y0, x_output)

y_result = y_result[:, 0]
print("200 шаг:",y_result[-1])

# x_output = np.linspace(0, 2, step // 100 )
# print("2 шаг: ",odeint(f, y0, x_output)[-1])







#odeint()предназначенно для решения систем обыкновенных дифференциальных уравнений (ОДУ)
#первого порядка с начальными условиями в одной точке (задача Коши)
# берем только первый столбец






