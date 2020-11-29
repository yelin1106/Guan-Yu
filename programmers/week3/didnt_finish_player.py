#완주하지 못한 선수

participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]

for name in completion:
  participant.remove(name)

print(participant)
