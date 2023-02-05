import matplotlib.pyplot as p
percent = [70,20,15,5]
name=["python","java","c++","c"]
# todo using explode
explode=[0.1,0,0,0]
p.pie(percent,labels=name,shadow=True,explode=explode)
p.show()
