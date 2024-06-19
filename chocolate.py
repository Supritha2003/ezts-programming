list=[7,10,30]
n=len(list)
chocolate_a=0
curr_pick=0
for chocolate in list:
    while(chocolate>0):
        if curr_pick==0:
            chocolate_a+=1
    chocolate-=1
    curr_pick=(curr_pick+1)%3
print(chocolate_a)
