# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*n
    for i in range(n):
        for j in a[:i]:
            if j>a[i]:
                b[i]+=1
        for k in a[i+1:]:
            if k>a[i]:
                b[i]+=1
    print(*b)