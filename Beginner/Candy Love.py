# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if sum(a)%2==0:
        print('NO')
    else:
        print('YES')