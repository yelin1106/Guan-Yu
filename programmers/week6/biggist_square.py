# 가장 큰 정사각형

def solution(board):
  answer=0
  if len(board)==1 or len(board[0])==1:
    return 1
  for i in range(len(board)):
    if i==0: continue
    for j in range(len(board[i])):
      if j==0: continue
      if board[i][j]!=0:
        board[i][j]=min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1
        if board[i][j]>answer:
          answer=board[i][j]
  answer*=answer
  return answer


board=[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))