#폰켓몬

def solution(nums):
  answer = 0
  cnt=len(nums)//2
  nums=list(set(nums))
  answer=len(nums) if len(nums)<cnt else cnt
  return answer

nums=[3,1,2,3]
nums=[3,3,3,2,2,4]
nums=[3,3,3,2,2,2]
print(solution(nums))