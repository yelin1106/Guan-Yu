#체육복
import copy

n=5
lost=[2, 4]
reserve=[1, 3, 5]

lost1=copy.deepcopy(lost)

for num in lost1:
  if num in reserve :
    reserve.remove(num)
    lost.remove(num)

lost1=copy.deepcopy(lost)

for num in lost1:
  if num-1 in reserve and num+1 not in reserve:
    reserve.remove(num-1)
    lost.remove(num)
  elif num-1 not in reserve and num+1 in reserve:
    reserve.remove(num+1)
    lost.remove(num)

lost1=copy.deepcopy(lost)

for num in lost1:
  if num-1 in reserve:
    reserve.remove(num-1)
    lost.remove(num)
    print(num)
    print(reserve)
  elif num+1 in reserve:
    reserve.remove(num+1)
    lost.remove(num)
print(f'6666666----------{lost}')
print(n-len(lost))