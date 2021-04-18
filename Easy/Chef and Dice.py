# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    b=n%4
    ans=(11*n) #min 2 sides will be visible for all dice, those will be 6 and 5 for max pips
    if n>=4:
        ans+=4*4 #the top dice of each stack in the 2x2 area will have 3 visible sides, which will be 4
    else:
        ans+=4*n 
    if b==1:
        ans+=5 #the num of dice on top will tell the extra sides visible
    elif b==2 or b==3:
        ans+=3*2
    print(ans)
