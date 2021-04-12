# cook your dish here
def origin(s):
    for i in set(s):
        if i=='Y':
            return 'NOT INDIAN'
        elif i=='I':
            return 'INDIAN'
    return 'NOT SURE'
    
t=int(input())
for i in range(t):
    n=int(input())
    s=str(input())
    print(origin(s))