# N개의 최소공배수

def solution(arr):
  answer = 1
  cm=[]
  for a in arr:
    temp=[]
    divnum=2
    while divnum<=a:
      if a%divnum==0:
        temp.append(divnum)
        a//=divnum
      else :
        divnum+=1
    cm.append(temp)
  for idx in range(len(cm)):
    for i in range(len(cm[idx])):
      print(f'첫번째 for {idx} {i}')
      if cm[idx]:
        num=cm[idx][0]
        answer*=num
        for j in range(len(cm[idx:])):
          print(cm[idx+j])
          if num in cm[idx+j]:
            cm[idx+j].remove(num)

  return answer

arr=[2,6,8,14]
print(solution(arr))