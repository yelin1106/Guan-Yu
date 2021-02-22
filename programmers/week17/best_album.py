# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
  answer = []
  gen_cnt={}
  gen_dic={}
  for i,gen in enumerate(genres):
    if gen in gen_cnt:
      gen_cnt[gen]+=plays[i]
      gen_dic[gen].append([i,plays[i]])
    else:
      gen_cnt[gen]=plays[i]
      gen_dic[gen]=[[i,plays[i]]]
  gen_cnt=sorted(gen_cnt.items(), key=lambda x: x[1], reverse=True)

  for gen, _ in gen_cnt:
    gen_dic[gen]=sorted(gen_dic[gen], key=lambda x: (-x[1], x[0]))

  for gen,_ in gen_cnt:
    end=2 if len(gen_dic[gen])>1 else 1
    for i in range(0,end):
      answer.append(gen_dic[gen][i][0])
  return answer

genres=['classic', 'pop', 'classic', 'classic', 'pop']
plays=[500, 600, 150, 800, 2500]
print(solution(genres, plays))