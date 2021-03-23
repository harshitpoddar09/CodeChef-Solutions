# cook your dish here
t=int(input())
for i in range(t):
    num=int(input())
    fact=1
    while num>=1:
        fact*=num
        num-=1
    print(fact)