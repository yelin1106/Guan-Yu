#시저 암호

s="a B z"
n=4
tempList=list(s)
answer=""
for c in tempList:
  i=ord(c)
  if not (i>96 and i<123) and not (i>64 and i<91):
    answer+=c
    continue
  if i>96 and i<123:
    i=(i-97+n)%26
    answer+=chr(97+i)
  if i>64 and i<91:
    i=(i-65+n)%26
    answer+=chr(65+i)

print(answer)