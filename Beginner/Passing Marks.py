# cook your dish here
t=int(input())
for i in range(t):
    amin,bmin,cmin,tmin,a,b,c=map(int,input().split())
    if a>=amin and b>=bmin and c>=cmin and a+b+c>=tmin:
        print('YES')
    else:
        print('NO')