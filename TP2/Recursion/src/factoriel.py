
from ap2_decorators import trace as t1

@t1
def fact(n):
    if n == 0:
       return 1
    else:
       return n * fact(n - 1)

print(fact(6)) 