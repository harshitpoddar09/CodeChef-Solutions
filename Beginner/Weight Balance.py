# cook your dish here
t=int(input())
for i in range(t):
    w1,w2,x1,x2,M=map(int,input().split())
    if (w2-w1)/M>=x1 and (w2-w1)/M<=x2:
        print(1)
    else:
        print(0)