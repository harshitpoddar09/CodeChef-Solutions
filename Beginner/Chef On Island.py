# cook your dish here
t=int(input())
for i in range(t):
    x,y,xr,yr,d=map(int,input().split())
    if x>=xr*d and y>=yr*d:
        print('YES')
    else:
        print('NO')