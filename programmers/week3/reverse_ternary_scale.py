#3진법 뒤집기

n=45

ternary=[]
while n>0:
  ternary.append(n%3)
  n//=3
ternary.reverse()

answer=0
for i in range(len(ternary)):
  answer+=3**i*ternary[i]

print(answer)