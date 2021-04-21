# cook your dish here
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    k=int(input())
    for i in range(9,-1,-1):
        if a[i]>k:
            print(i+1)
            break
        elif k>=a[i]:
            k=k-a[i]