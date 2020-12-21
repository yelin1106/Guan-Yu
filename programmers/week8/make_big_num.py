# 큰 수 만들기

def solution(number, k):
  nums=list(number)
  cnt=0
  while k!=cnt:
    for idx,n in enumerate(nums):
      if idx<len(nums)-1 and n<nums[idx+1]:
        cnt+=1
        nums.pop(idx)
        break
    else:
      cnt+=k-cnt
      for _ in range(k-cnt):
        nums.pop()
  print(nums)
  answer = "".join(nums)
  return answer


number="4177252841"
k=4
print(solution(number,k))