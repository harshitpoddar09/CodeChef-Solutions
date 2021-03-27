# cook your dish here
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    a.sort()
    print(a[1])