list=[1,-1,1,-1,1]
curr_pos=0
position=0
for i in list:
    position+=i
    if position==0:
        curr_pos+=1
print(curr_pos)