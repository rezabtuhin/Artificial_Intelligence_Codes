'''
    @author: Rezab Ud Dawla
'''


from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import random

iris = datasets.load_iris()
x = iris.data[:, :2]
y = (iris.target != 0) * 1

x_new = x.tolist()
y_new = y.tolist()

for i in range(len(x_new)):
  x_new[i].append(1)

x_train = []
y_train = []
x_val = []
y_val = []
x_test = []
y_test = []

for i in range(len(x_new)):
  rand = random.uniform(0,1)
  if rand >= 0 and rand <= 0.7:
    x_train.append(x_new[i])
    y_train.append(y_new[i])
  elif rand > 0.7 and rand <= 0.85:
    x_val.append(x_new[i])
    y_val.append(y_new[i])
  else:
    x_test.append(x_new[i])
    y_test.append(y_new[i])

numpy_x_train = np.array(x_train)
numpy_y_train = np.array(y_train)

numpy_x_val = np.array(x_val)
numpy_y_val = np.array(y_val)

def sigmoid(z):
  return 1 / (1 + np.exp(-z))

theta = [0.3,0.4,0.1]
lr = 0.1
train_loss = []
epoc = []

for i in range(1000):
  TJ = 0
  for s in range(len(x_train)):
    z = np.dot(numpy_x_train[s],theta)
    h = sigmoid(z)
    J = (-numpy_y_train[s]*np.log(h)) - ((1-numpy_y_train[s])*np.log(1-h))
    TJ = TJ+J
    dv = numpy_x_train[s]*(h-numpy_y_train[s])
    theta = theta - dv*lr
  TJ = TJ/len(x_train)
  train_loss.append(TJ)
  epoc.append(i)

correct = 0
for i in range(len(x_val)):
  z = np.dot(numpy_x_val[i],theta)
  h = sigmoid(z)
  if h >= 0.5:
    h = 1
  else:
    h = 0
  if h == numpy_y_val[i]:
    correct += 1
val_acc = correct/(len(x_val))*100

print(val_acc)
plt.plot(epoc,train_loss)
plt.show()