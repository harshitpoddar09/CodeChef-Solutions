# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    ans=''
    for j in range(n):
        ques=str(input())
        f=ques.count('F')
        if f>=x or (f==x-1 and ques.count('P')>=y):
            ans+='1'
        else:
            ans+='0'
    print(ans)