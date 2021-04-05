# cook your dish here
t=int(input())
for i in range(t):
    base=int(input())
    salary=base
    if base<1500:
        salary+=base
    else:
        salary+=500+(0.98*base)
    print(salary)