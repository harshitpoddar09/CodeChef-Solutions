# cook your dish here
def tension(n,r,a,b):
    tensions=[]
    t=0
    for i in range(n-1):
        t=t+b[i]
        tensions.append(t)
        t=max(t-((a[i+1]-a[i])*r),0)
    tensions.append(t+b[-1])
    return max(tensions)
t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(tension(n,r,a,b))