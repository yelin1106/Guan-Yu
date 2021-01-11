# 스킬트리
# 23분

# 그래프 최단거리 문제?

def solution(skill, skill_trees):
  answer = 0
  for skill_tree in skill_trees:
    valid_flag=True # 스킬트리가 유효하다면 True
    pre=skill_tree.find(skill[0])
    interrupted_flag=False if pre!=-1 else True
    for sk in skill[1:]:
      temp=skill_tree.find(sk)
      if interrupted_flag or temp==-1:
        interrupted_flag=True
        if temp!=-1:
          valid_flag=False
          break
      elif pre>temp:
        valid_flag=False
        break
      pre=temp
    if valid_flag:
      answer+=1

  return answer

skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))