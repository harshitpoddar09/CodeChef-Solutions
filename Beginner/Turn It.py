# cook your dish here
import math
t=int(input())
for i in range(t):
    [u,v,a,s]=list(map(int,input().split()))
    final=(u**2)-(2*a*s)
    if final<=1:
        print('Yes')
    else:
        if math.sqrt(final)<=v:
            print('Yes')
        else:
            print('No')