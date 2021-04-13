# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if x%10==0:
        print(0)
    elif x%10==5:
        print(1)
    else:
        print(-1)