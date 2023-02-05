import matplotlib.pyplot as p
x=[i for i in range(10)]
y=[]
for j in x:
    y.append(j*2)
p.bar(x,y)
p.show()