# cook your dish here
t=int(input())
for i in range(t):
    [n,k]=list(map(int,input().split()))
    s=str(input())
    count=0
    for j in range(n):
        if s[j]=='*':
            count+=1
            if count==k:
                print('YES')
                break
        else:
            count=0
    else:
        print('NO')