# 쿼드 압축 후 개수 세기

def quad(arr, x, y, size, ans):
  temp=arr[x][y]
  flag=False
  for ar in arr[x:x+size]:
    for a in ar[y:y+size]:
      if temp!=a:
        flag=True
        break
    if flag: break
  else:
    ans.append(temp)
    return
  size=size//2
  quad(arr, x, y, size, ans)
  quad(arr, x, y+size, size, ans)
  quad(arr, x+size, y, size, ans)
  quad(arr, x+size, y+size, size, ans)
  print(ans)

def solution(arr):
  ans=[]
  quad(arr, 0, 0, len(arr), ans)
  answer=[ans.count(0), ans.count(1)]
  return answer

arr=[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))