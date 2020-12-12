# 올바른 괄호

def solution(s):
  answer = True
  brackets=[]
  for b in s:
    if b=="(":
      brackets.append(b)
    else:
      if not brackets: #리스트가 비어있다면 (is empty)
        answer=False
        break
      brackets.pop()
  else:
    if brackets:
      answer=False

  return answer

s="(())()"
print(solution(s))