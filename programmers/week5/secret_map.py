# 비밀지도
# 풀이시간 56분

def solution(n, arr1, arr2):

  #temp_arr = [[0]*n]*n
  temp_arr=[]
  for i in range(n):
    temp_arr.append([" "]*n)
  
  for i,a1,a2 in zip(range(n),arr1,arr2):
    temp1=a1
    temp2=a2
    for j in range(n-1,-1,-1):
      if temp1%2==1 or temp2%2==1:
        temp_arr[i][j]="#"
      temp1//=2
      temp2//=2
  answer=[""]*n
  for i in range(n):
    answer[i]="".join(temp_arr[i])
  return answer


n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]

print(solution(n,arr1,arr2))