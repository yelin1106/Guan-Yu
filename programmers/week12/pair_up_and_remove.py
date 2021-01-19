# 짝지어 제거하기
# 스택활용

def solution(s):
  stack=[s[0]]
  idx=1
  while idx<len(s):
    if stack and stack[-1]==s[idx]:
      stack.pop()
    else:
      stack.append(s[idx])
    idx+=1
  answer=0 if stack else 1
  
  return answer


s="baabaa"
s="cdcd"
print(solution(s))