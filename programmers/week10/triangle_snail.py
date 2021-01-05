# 삼각 달팽이

# 처음 풀이
# def solution(n):
#   answer = []
#   tri=[]
#   for i in range(1,n+1):
#     tri.append([0]*i)
#   print(tri)
#   i,j=-1,0
#   temp=1
#   while temp<=sum(range(1,n+1)):
#     i+=1
#     while i<len(tri) and tri[i][j]==0: 
#       tri[i][j]=temp
#       i+=1
#       temp+=1
#     i-=1
#     j+=1
#     while j<len(tri[i]) and tri[i][j]==0:
#       tri[i][j]=temp
#       j+=1
#       temp+=1
#     i-=1
#     j-=2
#     while tri[i][j]==0:
#       tri[i][j]=temp
#       i-=1
#       j-=1
#       temp+=1
#     i+=1
#     j+=1
#     print(f'{i} {j}')
#     print(tri)
#   for t in tri:
#     for ans in t:
#       answer.append(ans)
#   return answer

# 풀이2 - 구글 검색
# def solution(n):
#   answer=[]
#   tri=[[0]*i for i in range(1,n+1)]
#   x,y=-1,0
#   num=1
#   for i in range(n):
#     for j in range(i,n):
#       if i%3==0: #down
#         x+=1
#       if i%3==1: #right
#         y+=1
#       if i%3==2: #up
#         x-=1
#         y-=1
#       tri[x][y]=num
#       num+=1
#   for tr in tri:
#     for t in tr:
#       answer.append(t)
#   return answer


# 풀이3 - 도연이 코드 훔침
def solution(n):
  answer=[]
  tri=[[0]*i for i in range(1,n+1)]
  direction={"down":[1,0], "right":[0,1], "up":[-1,-1]}
  x,y=-1,0
  num=1
  for i in range(n):
    for j in range(i,n):
      if i%3==0:
        dire="down"
      if i%3==1:
        dire="right"
      if i%3==2:
        dire="up"
      x+=direction[dire][0]
      y+=direction[dire][1]
      tri[x][y]=num
      num+=1
  for tr in tri:
    for t in tr:
      answer.append(t)
  return answer

n=6
print(solution(n))