# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    print(sum(a[k:n-k])/(n-(2*k)))