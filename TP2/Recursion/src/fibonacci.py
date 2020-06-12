
from ap2_decorators import trace
from ap2_decorators import count

@trace
@count
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1   
    else:    
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci.counter)
print(fibonacci(4))
# print(fibonacci.counter)
# print(fibonacci(10))
# print(fibonacci.counter)
# print(fibonacci(40))
# print(fibonacci.counter)

