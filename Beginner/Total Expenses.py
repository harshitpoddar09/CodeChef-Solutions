# cook your dish here
t=int(input())
for i in range(t):
    [qty,price]=list(map(int,input().split()))
    expense=qty*price
    if qty>1000:
        expense=0.9*expense
    print(expense)