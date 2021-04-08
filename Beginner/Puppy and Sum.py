# cook your dish here
def sum_func(n):
    return (n*(n+1))//2
t=int(input())
for i in range(t):
    d,n=map(int, input().split())
    for i in range(d):
        ans=sum_func(n)
        n=ans
    print(ans)