# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    for j in range(n):
        c=(a[j]*20)-(b[j]*10)
        if c>ans:
            ans=c
    print(ans)