# 카펫

def solution(brown, yellow):
  answer = []
  yellow_y=1
  yellow_x=yellow
  while True:
    if (yellow_x*2)+(yellow_y+2)*2 == brown:
      answer.append(yellow_x+2)
      answer.append(yellow_y+2)
      break
    while True:
      yellow_y+=1
      if yellow%yellow_y==0:
        yellow_x=yellow//yellow_y
        break
  return answer

brown=24
yellow=24
print(solution(brown,yellow))