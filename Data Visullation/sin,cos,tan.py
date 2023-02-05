import matplotlib.pyplot as p
from numpy import *
# todo sinx
a=arange(0,10,0.1)
b=sin(a)
p.subplot(2,2,1)
p.title("sinx")
p.plot(a,b)
# todo cosx
a1=arange(-5,5,0.01)
b1=cos(a1)
p.subplot(2,2,2)
p.title("cosx")
p.plot(a1,b1)
# todo taxx
a2=arange(0,10)
b2=sin(a2)
b3=cos(a2)
b4=b2/b3
p.subplot(2,2,3)
p.title("tanx")
p.plot(a2,b4)
# todo cotx
a2=arange(1,10,0.1)
b2=1/tan(a2)
p.subplot(2,2,4)
p.title("cotx")
p.plot(a2,b2)
p.show()

