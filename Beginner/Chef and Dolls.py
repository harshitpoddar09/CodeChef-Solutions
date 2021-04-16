# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    dolls=[]
    for i in range(n):
        dolls.append(int(input()))
    for j in set(dolls):
        if dolls.count(j)%2!=0:
            print(j)