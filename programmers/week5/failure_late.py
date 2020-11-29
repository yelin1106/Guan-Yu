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

#도연이거 훔치기
# def solution(N, stages):
#     answer = []
#     passed_cnt = len(stages)
#     stage_dict = {}
#     for i in range(1,N+1):
#         stages_cnt = stages.count(i)
#         # 스테이지에 멈춰있는 사람의 수가 0일 때 연산을 하지 않도록 따로 빼주어서 런타임 에러를 해결함
#         if stages_cnt == 0:
#             stage_dict[i] = 0
#         else:
#             stage_dict[i] = stages_cnt/passed_cnt
#         passed_cnt -= stages_cnt
#     # print(stage_dict)
#     sorted_dict = sorted(stage_dict.items(), reverse=True, key=lambda x: x[1])
#     # print(sorted_dict)
#     answer = [stage for stage, _ in sorted_dict]
#     return answer