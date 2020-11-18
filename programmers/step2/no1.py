#이상한 문자 만들기

s="___try    hello world strys___"
list=s.split(" ")
resultList=[]
for word in list:
  idx=0
  flag=1
  while idx<len(word):
    i=ord(word[idx])
    if not (i>96 and i<123) and not (i>64 and i<91):
      idx+=1
      continue
    if flag%2==1 and i>96 and i<123:
      word=word[:idx]+word[idx].upper()+word[idx+1:]
    if flag%2==0 and i>64 and i<91:
      word=word[:idx]+word[idx].lower()+word[idx+1:]
    idx+=1
    flag+=1
  resultList.append(word)

print(resultList)
result=" ".join(resultList)
print(result)
