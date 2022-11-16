import numpy as np
from scipy.signal import argrelextrema
x = np.linspace (0, 50, 100)
y = np.sin(x)
#print(y)
print(argrelextrema(y, np.less))