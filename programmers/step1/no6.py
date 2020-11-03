#평균 구하기
#정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

def solution(arr):
  sum=0.0
  for num in arr:
    sum+=num
  answer = sum/len(arr)
  return answer


a=[1,2,3,4]
print(solution(a))