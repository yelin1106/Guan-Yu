#실패율
#풀이시간 28분

def solution(N, stages):
  player=[]
  failuer=[]
  failuer_rate=[]
  for i in range(N):
    player.append(0)
    failuer.append(0)
    failuer_rate.append(0)
  for stage in stages:
    stage-=1
    if stage<N:
      failuer[stage]+=1
    else:
      stage=N-1
    for j in range(stage+1):
      player[j]+=1
  for i in range(N):
    if player[i]!=0:
      failuer_rate[i]=failuer[i]/player[i]
  answer=[]
  for i in range(N):
    idx=failuer_rate.index(max(failuer_rate))
    answer.append(idx+1)
    failuer_rate[idx]=-1
  return answer


N=4
stages=[4,4,4,4,4]
result=[3,4,2,1,5]
print(solution(N, stages))