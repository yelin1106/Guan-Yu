#다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
  answer = 0 #초
  dic={} #트럭의 인덱스가 키, [무게, 거리] 값
  i=0 #트럭 인덱스
  finish=0 #다리를 지난 트럭의 수
  while True:
    if finish==len(truck_weights):
      print("트럭이 모두 다리를 건넜습니다 {finish}")
      break
    answer+=1
    print(f'{answer} 초')
    sum=0
    for v,_ in dic.values():
      sum+=v
    print(f'트럭 무게의 합 {sum}')
    if i<len(truck_weights) and sum+truck_weights[i]<=weight:
      dic[i]=[truck_weights[i],0]
      i+=1
    dic_keys=list(dic.keys())
    print(f'dic의 key들 {dic_keys}')
    for k in dic_keys:
      print(f'{i} {dic}')
      dic[k][1]+=1
      if dic[k][1]==bridge_length:
        print(f"빠지는 트럭 {dic[k][0]}")
        dic.pop(k)
        finish+=1
  answer+=1
  print(f'while이 끝난 뒤 second {answer}')
  print(dic)
  return answer

bridge_length=2
weight=10
truck_weights=[7,4,5,6]

print(solution(bridge_length, weight, truck_weights))