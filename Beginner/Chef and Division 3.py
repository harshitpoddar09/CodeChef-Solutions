# cook your dish here
t=int(input())
for i in range(t):
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    print(min(sum(a)//k,d))