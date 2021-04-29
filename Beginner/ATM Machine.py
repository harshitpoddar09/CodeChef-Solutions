# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=''
    for i in a:
        if i<=k:
            k-=i
            ans+='1'
        else:
            ans+='0'
    print(ans)