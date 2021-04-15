# cook your dish here
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=1
    a=x+y+1
    while not prime(a):
        z+=1
        a=x+y+z
    print(z)