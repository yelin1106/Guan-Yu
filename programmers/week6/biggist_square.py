# 가장 큰 정사각형

def solution(board):
  max=0
  for b in board:
    if 1 in b:
      max=1
  for y,temp in enumerate(board):
    if y==len(board)-1:
      break
    for x,num in enumerate(temp):
      if x==len(temp)-1:
        break
      if num==1 and board[y][x+1]==1 and board[y+1][x]==1:
        cnt=1
        # print("사각형의 왼쪽 위!")
        # print(f'현재 위치 {y} {x}')
        # print(f'오른쪽 {y} {x+1} {board[y][x+1]}')
        # print(f'아래 {y+1} {x} {board[y+1][x]}')
        i=x+1
        while i<len(temp):
          if board[y][i]==1:
            cnt+=1
          i+=1
        # print(f'i {i} cnt {cnt} ')
        if y+cnt>len(board):
          cnt=cnt-y
        if cnt>max:
          for i in range(y+1,y+cnt):
            if i==len(board):
              break
            for j in range(x,x+cnt):
              if j==len(board):
                break
              # print(f'현재 위치 {i} {j} 값 {board[i][j]}')
              if board[i][j]==0:
                cnt=i-y
                break
          if cnt>max:
            max=cnt
  answer=max*max

  return answer


#board=[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
#print(board[0][1])#0의 오른쪽
#print(board[1][0])#0의 아래
board=[[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))