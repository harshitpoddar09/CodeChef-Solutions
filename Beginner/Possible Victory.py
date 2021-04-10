# cook your dish here
[r,o,c]=list(map(int,input().split()))
if r-c<(20-o)*6*6:
    print('YES')
else:
    print('NO')