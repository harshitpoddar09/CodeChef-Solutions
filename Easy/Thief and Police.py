# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    thief=n-x+m-y
    police=max(n-a,m-b)
    if police<thief:
        print('NO')
    else:
        print('YES')