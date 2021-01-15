# 멀쩡한 사각형


def solution(w,h):
  answer = w*h
  w1, h1=w, h
  while w1!=h1:
    if w1>h1:
      w1-=h1
    else:
      h1-=w1
  answer-=w+h-w1
  return answer

w=8
h=12
print(solution(w,h))