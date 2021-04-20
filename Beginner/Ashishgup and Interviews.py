# cook your dish here
import math
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    time=list(map(int,input().split()))
    not_ans=time.count(-1)
    if (n-not_ans)<math.ceil(n/2):
        print('Rejected')
    elif any(j>k for j in time):
        print('Too Slow')
    elif all(j<=1 and j>=0 for j in time):
        print('Bot')
    else:
        print('Accepted')