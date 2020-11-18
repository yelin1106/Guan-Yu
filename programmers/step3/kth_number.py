#k번째 수

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
result=[]

for i in range(len(commands)):
  tempList=array[commands[i][0]-1:commands[i][1]]
  tempList.sort()
  result.append(tempList[commands[i][2]-1])

print(result)