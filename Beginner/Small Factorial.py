# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    if n%((n//2)+1)!=0:
        print((n//2)+1)
    else:
        print(n)