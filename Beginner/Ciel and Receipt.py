# cook your dish here
t=int(input())
menu=[2048,1024,512,256,128,64,32,16,8,4,2,1]
for i in range(t):
    p=int(input())
    j=0
    ans=0
    while j<12:
        ans+=p//menu[j]
        p=p%menu[j]
        if p==0:
            break
        j+=1
    print(ans)