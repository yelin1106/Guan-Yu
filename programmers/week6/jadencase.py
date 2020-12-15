# JadenCase 문자열 만들기

def solution(s):
  word=s.split(" ")
  cap=[]
  for w in word:
    cap.append(w.capitalize())
  answer=" ".join(cap)
  return answer

s="3people        unFollowed me"
print(solution(s))