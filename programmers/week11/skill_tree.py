# 스킬트리
# 23분

def solution(skill, skill_trees):
  answer = 0
  for skill_tree in skill_trees:
    pre=skill_tree.find(skill[0])
    interrupted_flag=False if pre!=-1 else True
    for sk in skill[1:]:
      temp=skill_tree.find(sk)
      if interrupted_flag or temp==-1:
        interrupted_flag=True
        if temp!=-1:
          break
      elif pre>temp:
        break
      pre=temp
    else:
      answer+=1

  return answer

skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))

#큐 문제로 볼 수 있을 것 같음