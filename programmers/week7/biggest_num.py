#가장 큰 수

def solution(numbers):
  numbers.sort()
  print(numbers)
  if numbers[-1]!=0:
    str_list=list(map(str,numbers))
    str_list = sorted(str_list, key=lambda x: x[-1], reverse=True)
    print(str_list)
    max_len=max(list(map(len,str_list)))
    for i in range(max_len, -1, -1):
      str_list=sorted(str_list, key=lambda x: x[i] if len(x)>i else x[0], reverse=True)
    print(str_list)
    answer="".join(str_list)
  else:
    answer="0"
  return answer

numbers=[34, 30, 3, 5, 9]
#numbers=[12, 121]
#numbers=[21, 212]	
#numbers=[40, 403]
#numbers=[3, 30, 34, 5, 9, 4, 40, 42]
numbers=[0,0]
print(solution(numbers))