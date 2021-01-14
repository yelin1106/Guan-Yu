# 영어 끝말잇기

def solution(n, words):
  answer = [0,0]
  pre=words[0]
  for idx, word in enumerate(words):
    if idx==0 : continue
    if pre[-1]!=word[0] or words.index(word)!=idx:
      answer[0]=idx%n+1
      answer[1]=idx//n+1
      break
    pre=word

  return answer


n=3
words=['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
print(solution(n,words))