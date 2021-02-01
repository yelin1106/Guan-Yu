# 가장 긴 팰린드롬

def palin(string):
  return string == string[::-1]

def solution(s):
  answer=1
  for i in range(len(s)):
    for j in range(i+1,len(s)+1):
      if palin(s[i:j]):
      # print(f'{i} {j}')
      # print(s[i:j])
      # print(s[j-1:i-1 if i>0 else None :-1])
        if answer < len(s[i:j]):
          answer = len(s[i:j])
  return answer

print(solution("abcdcba"))