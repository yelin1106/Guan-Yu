# 조이스틱

def solution(name):
  alpha={"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10,"L":11, "M":12, "N":13, "O":12, "P":11, "Q":10, "R":9, "S":8, "T":7, "U":6, "V":5, "W":4, "X":3, "Y":2, "Z":1}
  cnt_list=[]
  for n in name:
    cnt_list.append(alpha[n])
  print(cnt_list)
  
  cnt1=0
  for i in range(1,len(cnt_list)):
    if cnt_list[i]==0:
      cnt1+=1
    else:
      break
  
  cnt2=0
  for i in range(len(cnt_list)-1,0,-1):
    if cnt_list[i]==0:
      cnt2+=1
    else:
      break
  answer=sum(cnt_list)
  answer+= len(cnt_list)-1-cnt1 if cnt1>cnt2 else len(cnt_list)-1-cnt2
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