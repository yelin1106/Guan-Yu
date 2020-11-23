#예산
#풀이시간 11분

#Greedy?

d=[1,3,2,5,4]	
budget=9

d.sort()

cnt=0
for num in d:
  if budget>=num:
    budget-=num
    cnt+=1
  else:
    break
  
print(cnt)
