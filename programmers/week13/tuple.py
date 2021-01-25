# 튜플

def solution(s):
  s=s.split("}")
  s=[i.strip(",") for i in s if len(i)>0]
  s=[i.strip("{") for i in s if len(i)>0]
  s=[i.split(",") for i in s if len(i)>0]
  cnt={}
  for string in s:
    for i in string:
      if i in cnt.keys():
        cnt[i]+=1
      else:
        cnt[i]=1
  answer = []
  for k,v in sorted(cnt.items(), key=lambda item: item[1], reverse=True):
    answer.append(int(k))
  return answer

s="{{2},{2,3,1},{2,1,3,4},{2,1}}"
s="{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))