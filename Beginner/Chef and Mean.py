# cook your dish here
def mean(n,a):
    mean=sum(a)/n
    for i in range(n):
        if a[i]==mean:
            return i+1
    return 'Impossible'
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(mean(n,a))