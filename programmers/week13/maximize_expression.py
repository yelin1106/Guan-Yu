# 수식 최대화

def dfs(operation, check, combi, temp):
  if len(temp)==len(operation):
    combi.append(temp)
    return
  for i in range(len(operation)):
    if check[i]: continue
    check[i]=True
    dfs(operation, check, combi, temp+operation[i])
    check[i]=False
  return

def solution(expression):
  nums=[]
  operation=[]
  temp=''
  for e in expression:
    if ord(e) in range(48, 58):
      temp+=e
    else:
      nums.append(int(temp))
      temp=''
      nums.append(e)
      operation.append(e)
  nums.append(int(temp))
  operation=list(set(operation))

  check=[False]*len(operation)
  combi=[]
  dfs(operation, check, combi, "")

  answer = 0
  for com in combi:
    stack=nums[:]
    for c in com:
      temp=[]
      idx=0
      while idx<len(stack):
        if stack[idx]==c:
          if c=="+":
            result=temp.pop()+stack[idx+1]
          elif c=="*":
            result=temp.pop()*stack[idx+1]
          else:
            result=temp.pop()-stack[idx+1]
          temp.append(result)
          idx+=2
        else:
          temp.append(stack[idx])
          idx+=1
      stack=temp[:]
    answer=abs(stack[0]) if abs(stack[0])>answer else answer
  return answer


expression="100-200*300-500+20"
print(solution(expression))