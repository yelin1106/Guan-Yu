# 큰 수 만들기

#시간초과 코드
# def solution(number, k):
#   nums=list(number)
#   cnt=idx=0
#   while idx<len(nums) and cnt!=k:
#     if idx<len(nums)-1 and nums[idx]<nums[idx+1]:
#       print(nums.pop(idx))
#       cnt+=1
#       if idx!=0 : idx-=1
#     else:
#       idx+=1
#   cnt+=k-cnt
#   for _ in range(k-cnt):
#     nums.pop()
#   print(nums)
#   answer = "".join(nums)
#   return answer

def solution(number, k):
  stack=[number[0]]
  for num in number[1:]:
    while len(stack)>0 and k>0 and stack[-1]<num:
      k-=1
      stack.pop()
    stack.append(num)
  if k>0:
    stack=stack[:-k]
  answer="".join(stack)
  return answer

number="4177252841"
number="11111"
k=2
print(solution(number,k))