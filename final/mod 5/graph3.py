import math
from pylab import *
x = np.arange(0, math.pi*2, 0.05)
plot(x, sin(x),label='sin')
plot(x, cos(x), 'r-',label='cos')
plot(x, -sin(x), 'g--',label='-sin')
grid(True)
title('waves')
xlabel('x')
ylabel('sin cos -sin')
legend(loc='upper right')
show()