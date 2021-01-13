# 점프와 순간이동

def solution(n):
  ans = 0
  remain=0
  while n!=0:
    n, remain=divmod(n,2)
    ans+=remain
  return ans

# 다른 풀이
# def solution(n):
#   return bin(n).count('1')


n=5
print(solution(n))