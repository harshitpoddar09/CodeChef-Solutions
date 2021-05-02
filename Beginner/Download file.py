# cook your dish here
tc=int(input())
for i in range(tc):
    n,k=map(int,input().split())
    ans=0
    for j in range(n):
        t,d=map(int,input().split())
        if t>=k:
            ans+=(t-k)*d
            k=0
        else:
            k-=t
    print(ans)