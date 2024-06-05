import math
from pylab import *
x = np.arange(0, math.pi*2, 0.05)
plot(x, sin(x))
plot(x, cos(x), 'r-')
plot(x, -sin(x), 'g--')
show()