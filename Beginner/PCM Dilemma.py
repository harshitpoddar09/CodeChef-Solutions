# cook your dish here
t=int(input())
for i in range(t):
    string=str(input())
    if 'P' in string and 'C' in string and 'M' in string:
        print('YES')
    else:
        print('NO')