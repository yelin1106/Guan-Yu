# H-Index

def solution(citations):
  answer = 0
  citations.sort()
  print(citations)
  for idx,c in reversed(list(enumerate(citations))):
    print(f'{idx} {c}')
    if idx+1<=citations[len(citations)-idx-1] and c>=idx+1:
      answer=idx+1
      break
  return answer


citations=[3, 0, 6, 1, 5]
citations=[6, 6, 6, 6, 6]
print(solution(citations))