# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    ans=0
    for j in p:
        if j>k:
            ans+=j-k
    print(ans)