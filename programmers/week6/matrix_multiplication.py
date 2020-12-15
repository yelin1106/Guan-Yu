# 행렬의 곱셈

def solution(arr1, arr2):
  answer = []
  for _ in range(len(arr1)):
    answer.append([0]*len(arr2[0]))
  for i in range(len(arr1)):
    for j in range(len(arr2[0])):
      for k in range(len(arr2[0])):
        print(f'{i} {j} {k}')
        answer[i][j]+=arr1[i][k]*arr2[k][j]
      print(answer)
  return answer


a=[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
b=[[5, 4], [2, 4], [3, 1]]
print(solution(a,b))