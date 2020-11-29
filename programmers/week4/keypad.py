#키패드 누르기

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"
result="LRLLLRLLRRL"

keypad={
  1:(0,0), 2:(0,1), 3:(0,2),
  4:(1,0), 5:(1,1), 6:(1,2),
  7:(2,0), 8:(2,1), 9:(2,2),
  "*":(3,0), 0:(3,1), "#":(3,2)
}
result_list=[]
lHand="*"
rHand="#"

for key in numbers:
  if key in (1,4,7):
    result_list.append("L")
    lHand=key
  elif key in (3,6,9):
    result_list.append("R")
    rHand=key
  else:
    temp_l=abs(keypad[key][0]-keypad[lHand][0])+abs(keypad[key][1]-keypad[lHand][1])
    temp_r=abs(keypad[key][0]-keypad[rHand][0])+abs(keypad[key][1]-keypad[rHand][1])

    if temp_l==temp_r:
      if hand=="left":
        result_list.append("L")
        lHand=key
      else :
        result_list.append("R")
        rHand=key
    else:
      if temp_l<temp_r:
        result_list.append("L")
        lHand=key
      else:
        result_list.append("R")
        rHand=key

print("".join(result_list))
