# cook your dish here
def diet(n,k,a):
    b=0
    for j in range(n):
        b+=a[j]
        b-=k
        if b<0:
            return 'NO '+str(j+1)
    return 'YES'
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    print(diet(n,k,a))