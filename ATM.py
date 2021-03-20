# cook your dish here
[x,y]=list(map(float,input().split()))
ans=0
if x+0.5>y:
    ans=y
else:
    if x%5==0:
        ans=y-x-0.50
    else:
        ans=y
print("{0:.2f}".format(ans))