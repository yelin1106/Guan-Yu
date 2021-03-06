# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
  words.append(begin)
  if target not in words:
    return 0
  target_idx=words.index(target)
  length=len(words)
  w_len=len(begin)
  visited=[0]*length

  queue=[[begin, -1]]
  while queue:
    cur=queue.pop(0)
    for i in range(length-1):
      if not visited[i]:
        dif=0
        for j in range(w_len):
          if dif>1: break
          if cur[0][j]!=words[i][j]:
            dif+=1
        if dif==1:
          queue.append([words[i],i])
          visited[i]=visited[cur[1]]+1

  answer=visited[target_idx]
  return answer

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))