'''
    @author: Rezab Ud Dawla
'''


import numpy as np
import matplotlib.pyplot as plt
import random
plt.style.use('dark_background')

# loading data
data = np.genfromtxt('data.csv',delimiter = ",")
centers = np.genfromtxt('centers.csv',delimiter = ",")
# k = len(centers)
# breaking data to plot in a graph
# tempx = data[:,0]
# tempy = data[:,1]
# tempcenterx = centers[:,0]
# tempcentery = centers[:,1]
# plt.scatter(tempx,tempy,s = 10,marker = '*',color = 'g')
# plt.scatter(tempcenterx,tempcentery,s = 25,marker = '^',color = 'r')
# plt.title('Initial Datapoints')
# plt.show()
# 2 new 2D list initialization
clusters = [[],[],[],[],[],[]]
temp_clusters = [[],[],[],[],[],[]]
iteration = 0
while True:
    for x in data:
      sub_array = centers - x
      sqr_array = sub_array**2
      sum_array = sqr_array.sum(axis = 1)
      index = sum_array.argmin()
      temp_clusters[index].append(x)
    i = 0
    for temp_sam in temp_clusters:
      x = np.array(temp_sam)
      y = x.mean(axis = 0)
      centers[i] = y
      i = i+1
    iteration = iteration+1
    count = 0
    if iteration>1:
        for i in range(len(data)):
            x = 0
            y = 0
            for j in range(len(temp_clusters)):
                for k in range(len(temp_clusters[j])):
                    if data[i][0] == temp_clusters[j][k][0] and data[i][1]==temp_clusters[j][k][1]:
                        x = j
            for l in range(len(clusters)):
                for m in range(len(clusters[l])):
                    if data[i][0] == clusters[l][m][0] and data[i][1]==clusters[l][m][1]:
                        y = l
            if x != y:
                count = count+1
        if count<10:
            clusters = temp_clusters
            break
    clusters = temp_clusters
    temp_clusters = [[],[],[],[],[],[]]

print(len(clusters))
for samplex in clusters:
    lenx = np.array(samplex)
    axisx = lenx[:,0]
    axisy = lenx[:,1]
    plt.scatter(axisx, axisy,s = 5,label = "Members")

plt.title('K Means Clustering')
tempcenterx = centers[:,0]
tempcentery = centers[:,1]
plt.scatter(tempcenterx, tempcentery,s = 50,color = 'white',label = "centers")
plt.legend()
plt.show()