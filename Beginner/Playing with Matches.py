# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=a+b
    matches=[6,2,5,5,4,5,6,3,7,6]
    ans=0
    for i in str(c):
        ans+=matches[int(i)]
    print(ans)