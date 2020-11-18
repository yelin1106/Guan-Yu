#약수의 합

n=12

answer=0
for i in range(1, n+1):
  if n%i==0:
    answer+=i

print(answer)

#12의 경우 1-12, 2-6, 3-4 등의 짝이 있는 것을 활용할 수 있다 