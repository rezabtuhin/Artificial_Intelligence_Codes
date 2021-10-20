'''
    @author: Rezab Ud Dawla
'''


from numpy import genfromtxt
import random
import math
import numpy as np



data_path = 'G:\Study\AI Lab\Dataset\iris.csv'
my_data = genfromtxt(data_path, delimiter=',')
data = my_data.tolist()

random.shuffle(data)
Train_set = []
Val_set = []
Test_set = []

for sample in data:
  R = random.uniform(0, 1)
  if R >= 0 and R <= 0.7:
    Train_set.append(sample)
  elif R > .7 and R < 0.85:
    Val_set.append(sample)
  else:
    Test_set.append(sample)

Distance = []
count = []
check = 0
k=15
for i in Val_set:
  valset1 = i
  for j in Train_set:
    trainset1 = j
    distance = 0
    for k in range(len(trainset1)-1):
      distance+= (valset1[k] - trainset1[k])**2
    Distance.append(math.sqrt(distance))
  avg = np.array(Distance)
  avg_new = avg.argsort()[:]
  Distance.clear()
  zero=0
  one=0
  two=0
  for l in range(k):
    if Train_set[avg_new[l]][len(data[0])-1] == 1:
      one+=1
    elif Train_set[avg_new[l]][len(data[0])-1] == 2:
      two+=1
    else:
      zero+=1
  if one>zero and one>two:
    count.append(1)
  elif two>zero and two>one:
    count.append(2)
  else:
    count.append(0)

for p in range(len(count)):
  if Val_set[p][len(Val_set[1])-1] == count[p]:
    check+=1;

accuracy = check / len(Val_set) * 100
print("Accuracy = ", accuracy)
