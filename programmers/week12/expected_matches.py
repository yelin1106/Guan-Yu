# 예상 대진표

def solution(n,a,b):
  answer = 0
  nums=[i for i in range(1,n+1)]
  while True:
    answer+=1
    temp=nums[:]
    nums=[]
    idx=0
    while idx<len(temp):
      if temp[idx] in (a,b) and temp[idx+1] in (a,b):
        return answer
      if temp[idx] in (a,b):
        nums.append(temp[idx])
      else:
        nums.append(temp[idx+1])
      idx+=2

  return answer


print(solution(8,4,7))