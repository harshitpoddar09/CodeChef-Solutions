# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    ans=0
    for i in str(n):
        if i=='4':
            ans+=1
    print(ans)