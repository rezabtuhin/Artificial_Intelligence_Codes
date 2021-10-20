'''
    @author: Rezab Ud Dawla
'''


import random

state = [2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
temp = 1000
time = 0


def curTemp(temp,time):
  return temp-0.95*time


def calc_cost(state):
  cost = 0
  for i in range(len(state)):
    for j in range(i+1, len(state)):
      if state[i]>state[j]:
        cost = cost+1
  return cost

cost = calc_cost(state)

while True:
  mytemp = curTemp(temp,time)
  if mytemp<=0:
    break

  r1 = random.randint(0,len(state)-1)
  r2 = random.randint(0, len(state)-1)
  new_state = list.copy(state)
  new_state[r1],new_state[r2] = new_state[r2],new_state[r1]
  v = calc_cost(new_state)
  if v<cost:
    state = new_state
    cost = v
  else:
    energy = v - cost
    prob = pow(2.71828, (energy/mytemp))
    rand_def = random.random()
    if rand_def < prob:
      state = new_state
      cost = v
    else:
      continue
  time = time+1


print(state)
