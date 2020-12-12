#124 나라의 숫자

n=int(input())
dic={1:"1",2:"2",0:"4"}
result=""
while n>0:
  result+=dic[n%3]
  if n%3==0:
    n-=1
  n//=3
  
print(result[-1::-1])