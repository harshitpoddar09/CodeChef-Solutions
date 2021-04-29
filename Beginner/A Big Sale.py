# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    loss=0
    for j in range(n):
        p,qty,x=map(int,input().split())
        pnew=p+((x/100)*p)
        pfinal=pnew-((x/100)*pnew)
        loss+=(p-pfinal)*qty
    print(loss)