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

print(solution(8,4,7))


#혜린언니 코드
# def solution(n,a,b):
#   answer = 0
  
#   def div(n):
#     if n % 2 == 0:
#       n //= 2
#     else:
#       n = n//2 +1
#     return n
  
#   while a != b:
#     a = div(a)
#     b = div(b)
    
#     answer += 1
      
#   return answer


#도연이 코드
# def solution(n, a, b):
#   answer = 0
#   if a > b:
#     a, b = b, a
#   n_round = bin(n)[2:].count('0')
#   start = 0

#   while n > 1:
#     n /= 2
#     if a <= start + n < b:
#       answer = n_round
#       break
#     else:
#       n_round -= 1

#     if a > n+start:
#       start += n
#   return answer