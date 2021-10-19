import matplotlib.pyplot as plt
from random import randint as rand
import random


random.seed(1234)

def make_points():
    x_list = [rand(0,100) + rand(-10,10) for _ in range(100)]
    y_list = [rand(0,100) + rand(-10,10) for _ in range(100)]

    for _ in range(100):
    	x_list.append(rand(-100,0) + rand(-10,10))
    	y_list.append(rand(-100,0) + rand(-10,10))

    return x_list, y_list

def getCluster(x_list, y_list, c1, c2):
    cluster1 = []
    cluster2 = []

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        if Dist(x,y,c1[0],c1[1]) < Dist(x,y,c2[0],c2[1]):
            cluster1.append([x,y])
        else:
            cluster2.append([x,y])

    return cluster1, cluster2

def show(x_list, y_list, c1, c2):
    cluster1, cluster2 = getCluster(x_list, y_list, c1, c2)

    plt.scatter([i[0] for i in cluster1], [i[1] for i in cluster1], c=['g'])
    plt.scatter([i[0] for i in cluster2], [i[1] for i in cluster2], c=['b'])

    plt.plot([c1[0], c2[0]],[c1[1],c2[0]], 'ro')

    plt.show()

def Dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

def avgPos(l):
    x_sum = 0
    y_sum = 0
    for i in range(len(l)):
        x_sum += l[i][0]
        y_sum += l[i][1]

    return [x_sum//len(l), y_sum//len(l)]

def calcNewPos(c1, c2, x_list, y_list):
    cluster1, cluster2 = getCluster(x_list, y_list, c1, c2)

    return [avgPos(cluster1), avgPos(cluster2)]


x_list, y_list = make_points()

c1 = [rand(-100, 0),rand(-100,100)]
c2 = [rand(0, 100),rand(-100,100)]

show(x_list, y_list, c1, c2)

for i in range(5):
    c1,c2 = calcNewPos(c1,c2,x_list,y_list)
    show(x_list, y_list, c1, c2)