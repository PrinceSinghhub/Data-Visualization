import matplotlib.pyplot as p
x=[i for i in range(10)]
y=[3,6,5,6,9,7,4,1,2,5]
x1=[i+0.2 for i in range(10)]
y1=[6,5,3,9,8,7,4,3,5,2]
p.bar(x,y,width=0.3,color="red",label="codex")
p.bar(x1,y1,width=0.3,color="blue",label="coder")
# todo show our label
p.legend()
p.show()