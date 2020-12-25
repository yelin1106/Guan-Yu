# 조이스틱

def solution(name):
  alpha={"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10,"L":11, "M":12, "N":13, "O":12, "P":11, "Q":10, "R":9, "S":8, "T":7, "U":6, "V":5, "W":4, "X":3, "Y":2, "Z":1}
  cnt_list=[]
  for n in name:
    cnt_list.append(alpha[n])
  print(cnt_list)
  answer=sum(cnt_list)

  #여기부터 구글 참고
  idx=0
  left=right=1
  while True:
    cnt_list[idx]=0
    if sum(cnt_list)==0: break
    while cnt_list[idx-left]==0:
      left+=1
    while cnt_list[idx+right]==0:
      right+=1
    answer+=left if left<right else right
    idx+= -left if left<right else right

  return answer


name="JAZ" #11
name="JEROEN" #56
name="JAN" #23
name="AAA" #0
name="ABAAAAABAB" #8
name="ABABAAAAAB" #8
name="BBBAAAB"#9
name="ABABAAAAABA"#11
print(solution(name))