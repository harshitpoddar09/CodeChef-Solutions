# cook your dish here
import math
t=int(input())
for i in range(t):
    r=int(input())
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    d12=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    d13=math.sqrt(((x1-x3)**2)+((y1-y3)**2))
    d23=math.sqrt(((x3-x2)**2)+((y3-y2)**2))
    if (d12<=r and d13<=r) or (d12<=r and d23<=r) or (d13<=r and d23<=r):
        print('yes')
    else:
        print('no')