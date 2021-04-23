# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=str(input())
    r=s.count('R')
    g=s.count('G')
    b=s.count('B')
    print(n-max(r,g,b))