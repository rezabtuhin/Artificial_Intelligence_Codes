'''
    @author: Rezab Ud Dawla
'''


from numpy import genfromtxt
import random
import numpy as np
import math

data_path = 'G:\Study\AI Lab\Dataset\diabetes.csv'
database = genfromtxt(data_path, delimiter=',')
data = database.tolist()

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
k = 1
for i in Val_set:
  valset1 = i
  for j in Train_set:
    trainset1 = j
    distance = 0
    for k in range(len(trainset1)-1):
      distance+=(valset1[k] - trainset1[k])**2
    Distance.append(math.sqrt(distance))
  avg = np.array(Distance)
  new_avg = avg.argsort()[:]
  Distance.clear()
  add = 0
  avarage=0
  error=0
  for l in range(k):
    add+=Train_set[new_avg[l]][len(Val_set[0]) - 1]
  avarage= add / k
  error = error+((valset1[10] - avarage)**2)

ac_error=error/len(Val_set)
print("Average: ",avarage)
print("Mean Error: ",ac_error)
