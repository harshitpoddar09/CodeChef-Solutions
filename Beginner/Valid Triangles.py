# cook your dish here
t=int(input())
for i in range(t):
    [a,b,c]=list(map(int, input().split()))
    if a+b+c==180:
        print('YES')
    else:
        print('NO')