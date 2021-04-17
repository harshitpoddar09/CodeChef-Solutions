# cook your dish here
t=int(input())
for i in range(t):
    [k1,k2,k3,v]=list(map(float,input().split()))
    ans=round(100/(k1*k2*k3*v),2)
    if ans<9.58:
        print('YES')
    else:
        print('NO')