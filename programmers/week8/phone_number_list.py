# 전화번호 목록

def solution(phone_book):
  for phone in phone_book:
    for p in phone_book:
      if phone==p: continue
      if p.find(phone)==0:
        return False
  return True


phone_book=["119", "97674223", "1195524421"]
print(solution(phone_book))