# cook your dish here
def match(x,y):
    for i in range(len(x)):
        if x[i]!='?' and y[i]!='?':
            if x[i]!=y[i]:
                return 'No'
    return 'Yes'
t=int(input())
for i in range(t):
    x=str(input())
    y=str(input())
    print(match(x,y))