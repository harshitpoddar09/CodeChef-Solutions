# cook your dish here
import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    ans=[]
    p=math.gcd(a,b)
    ans.append(str(p))
    q=(a*b)//p                #a*b=LCM(a,b)*GCD(a,b)
    ans.append(str(q))
    print(' '.join(ans))