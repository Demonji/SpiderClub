#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import  string

with open('speed.txt','r') as f:
    x=np.arange(1,515,5)
    y=[]
    average=0
    count=0
    for line in f:
        average+=string.atof(line.split('\n')[0])
        count+=1
        if count%5==0:
            y.append(average/5)
            average=0


plt.xlabel('Authors in top five hundred ')
plt.ylabel('Words wirten everyday')
plt.plot(x,y)
plt.show()
