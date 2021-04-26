# cook your dish here
def chocolate(n,x,a):
    ans=len(set(a))
    if n-ans>=x:
        return ans
    x=x-(n-ans)
    ans-=x
    return ans
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    print(chocolate(n,x,a))