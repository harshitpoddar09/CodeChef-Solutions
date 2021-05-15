# cook your dish here
t=int(input())
for i in range(t):
    s0,s1,s2=map(int,input().split())
    ans=s0
    if s2>s1:
        ans+=(s2-s1)//3
        s2-=((s2-s1)//3)*3
    if s2>s1:
        ans+=1
        s2-=3
    ans+=s2
    s1-=s2
    ans+=s1//3
    print(ans)