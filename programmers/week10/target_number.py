# 타겟 넘버

def dfs(numbers, target, num_sum, idx):
  print(f'dfs 호출 {numbers} {target} {num_sum} {idx}')
  answer=0
  if idx==len(numbers):
    if num_sum==target:
      return 1
    return 0
  answer+=dfs(numbers, target, num_sum+numbers[idx], idx+1)
  answer+=dfs(numbers, target, num_sum-numbers[idx], idx+1)
  return answer

def solution(numbers, target):
  answer = dfs(numbers, target, 0, 0)
  return answer

numbers=[1, 1, 1, 1, 1]
target=3
print(solution(numbers, target))