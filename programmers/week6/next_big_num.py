# 다음 큰 숫자

# def solution(n):
#   answer = 0
#   binary=list(bin(n)[2:])
#   temp="0"
#   idx=len(binary)
#   for i, b in reversed(list(enumerate(binary))):
#     #print(f'{i} {b}')
#     if b=="1":
#       temp="1"
#     if temp=="1" and b=="0":
#       idx=i
#       break
#   print(f'{idx}')
#   print()
#   cnt=binary[-1:idx:-1].count("1")
#   print(cnt)
#   for i in range(cnt-1):
#     binary[-1-i]="1"
#     print(binary[-1-i])
#   for i in range(len(binary[-1:idx:-1])-cnt+1):
#     print(binary)
#     binary[cnt+i]="0"
#     print(binary)
#   if len(binary)<cnt+1:
#     binary.insert(0,"1")
#   else:
#     binary[cnt-1]="1"
#   print(binary)
#   result="".join(binary)
#   result="0b"+result
#   answer=int(result,2)
#   return answer

def solution(n):
  answer=n
  binary=str(bin(n))
  cnt=binary.count("1")
  while True:
    answer+=1
    #print(binary.count("1"))
    ans_bin=str(bin(answer))
    if ans_bin.count("1")==cnt:
      break

  return answer

n=78
print(solution(n))