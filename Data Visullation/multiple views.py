import matplotlib.pyplot as p
x=[i for i in range(10)]
y=[j*2 for j in range(10,20)]
z=[i*i for i in range(10,20)]
# todo first graph
p.subplot(3,2,1)
p.plot(x,y)
p.title("graph 01")

# todo second graph
p.subplot(3,2,2)
p.title("graph 02")
p.plot(x,z)


a=[10,20,30,40]
b=[50,60,70,80]
# todo third graph
p.title("graph 03")
p.subplot(3,2,3)
p.plot(a,b)

a=[10,20,30,40]
b=[50,60,70,80]
# todo fourth graph
p.title("graph 04")
p.subplot(3,2,4)
p.plot(a,b)

a1=[7,8,9,10]
b1=[11,12,13,14]
# todo fifth graph
p.title("graph 05")
p.subplot(3,2,5)
p.plot(a1,b1)

a1=[7,8,90,100]
b1=[11,120,13,140]
# todo sixth graph
p.title("graph 06")
p.subplot(3,2,6)
p.plot(a1,b1)
p.show()