# 이진 변환 반복하기

def solution(s):
  cnt, zero=0,0
  while s!="1":
    cnt+=1
    zero+=s.count("0")
    s=s.replace("0","")
    s=str(bin(len(s)))[2:]
  answer=[cnt,zero]
  return answer

s="110010101001"
s="01110"
s="1111111"
print(solution(s))