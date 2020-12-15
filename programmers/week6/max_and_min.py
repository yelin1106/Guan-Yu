# 최댓값과 최솟값

def solution(s):
  answer = ''
  s_list=list(map(int,s.split()))
  print(s_list)
  max_num=str(max(s_list))
  min_num=str(min(s_list))
  answer=min_num+" "+max_num

  return answer

  
s="-1 -2 -3 -4"
print(solution(s))