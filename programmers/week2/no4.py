#문자열을 정수로 바꾸기

s="-1234"

answer=0
if s[0]=="+":
  answer=int(s[1:])
elif s[0]=="-":
  answer=int(s[1:])*-1
else:
  answer=int(s)

print(answer)
