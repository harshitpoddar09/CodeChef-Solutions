# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    i=1
    while a>=i and b>=i+1:
        a-=i
        b-=i+1
        i+=2
    if a<i:
        print('Bob')
    else:
        print('Limak')