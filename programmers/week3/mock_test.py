#모의고사

answers=[1,2,3,4,5]
a=[1, 2, 3, 4, 5]
b=[2, 1, 2, 3, 2, 4, 2, 5]
c=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
count=[0,0,0]
for i in range(len(answers)):
  if a[i%len(a)] == answers[i]:
    count[0]+=1
  if b[i%len(b)] == answers[i]:
    count[1]+=1
  if c[i%len(c)] == answers[i]:
    count[2]+=1

result=[]
max_num=max(count)
for i in range(3):
  if count[i]==max_num:
    result.append(i+1)
print(result)