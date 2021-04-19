# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for j in range(n):
        s=str(input())
        score=0
        for p in range(k):
            if s[p]=='1':
                score+=a[p]
        print(score)