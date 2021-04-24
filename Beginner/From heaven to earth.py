# cook your dish here
t=int(input())
for i in range(t):
    n,v1,v2=map(int,input().split())
    t1=((2**0.5)*n)/v1
    t2=(2*n)/v2
    if t1>t2:
        print('Elevator')
    else:
        print('Stairs')