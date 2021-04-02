# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    if str(n)==str(n)[::-1]:
        print('wins')
    else:
        print('loses')