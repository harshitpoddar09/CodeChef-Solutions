# cook your dish here
t=int(input())
for i in range(t):
    [a,b]=list(map(int,input().split()))
    ans=[str(max(a,b)),str(a+b)]
    print(' '.join(ans))