#두 개 뽑아서 더하기

numbers=[2,1,3,4,1]
result=[]
for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    result.append(numbers[i]+numbers[j])

answer=set(result)

print(answer)