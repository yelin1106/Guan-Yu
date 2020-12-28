#소수 찾기
import re

def solution(numbers):
  answer = 0

  # 에라토스테네스의체를 사용하여 소수 리스트 생성
  num_len=int("1"+"0"*len(numbers))
  temp_list=[True]*num_len
  end=int(num_len**0.5)+1
  for i in range(2, end):
    if temp_list[i]:
      for j in range(i+i, num_len, i):
        temp_list[j]=False
  prime=[str(i) for i in range(2, num_len) if temp_list[i]]
  print(prime)

  # 정규식을 활용하여 numbers에 있는 숫자가 들어간 소수만 골라냄
  temp=[]
  for i in range(1,len(numbers)+1):
    compile_num="["+numbers+"]{"+str(i)+"}"
    p=re.compile(compile_num)
    for pr in prime:
      if p.match(pr)!=None and len(pr)==i:
        temp.append(pr)
  print(temp)

  # numbers의 수가 여러번 반복되는경우를 제거하기 위한 리스트
  remove_list=[]
  for n in numbers:
    for t in temp:
      if numbers.count(n)<t.count(n):
        remove_list.append(t)
  remove_list=list(set(remove_list))
  for rl in remove_list:
    temp.remove(rl)
  print(temp)
  answer=len(temp)
  return answer

numbers="17"
print(solution(numbers))