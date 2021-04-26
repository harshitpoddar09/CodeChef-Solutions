# cook your dish here
t=int(input())
for i in range(t):
    numbers=list(map(int,input().split()))
    numbers.remove(len(numbers)-1)
    print(max(numbers))