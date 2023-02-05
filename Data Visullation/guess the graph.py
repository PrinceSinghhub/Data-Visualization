import matplotlib.pyplot as p
import random as r
a=[]
for i in range(5):
    a.append(r.randrange(10,20,1))
b=[]
for j in range(5):
    b.append(r.randint(5,10))
p.plot(a,b)
p.show()