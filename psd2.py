import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = x.copy()

    j = 0
    for i in y:
        if i < -3 or i > 3:
            y[j] = 0
        else:
            y[j] = abs(i)
        
        j += 1
    
    return y

x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

plt.figure(0)
plt.stem(x, f(x))

plt.figure(1)
plt.stem(x, f(x - 1))

plt.figure(2)
plt.stem(x, f(x + 1))

plt.figure(3)
plt.stem(x, (f(x + 1) + f(x) + f(x - 1)) / 3 )

plt.show()