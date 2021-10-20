
'''
    @author: Rezab Ud Dawla
'''


def calc_cost(tree):
  cost = 0
  for i in range(len(tree)):
    for j in range(i+1,len(tree)):
      if tree[i]>tree[j]:
        cost = cost+1
  return cost




def goal_test(tree):
	if calc_cost(tree) == 0:
		return True
	else:
		return False


def State_generation(current_state, current_state_cost):
    cur_cpy = list.copy(current_state)
    for i in range(len(current_state)):
        minimum_cost = float('inf')
        for j in range(i+1,len(current_state)):
            current_state[i], current_state[j] = current_state[j], current_state[i]
            c_cost = calc_cost(current_state)
            if minimum_cost > c_cost:
                minimum_state = list.copy(current_state)
                minimum_cost = c_cost
            current_state = cur_cpy
        if minimum_cost < current_state_cost:
            return minimum_state, minimum_cost
        else:
            return cur_cpy, None

tree = [2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
cost = calc_cost(tree)
print(cost)
while goal_test(tree) != True:
  tree,cost = State_generation(tree,cost)
  if cost == None:
    print(tree)
    break
if cost!=None:
    print(tree)