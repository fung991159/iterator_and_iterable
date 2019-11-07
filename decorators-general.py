#a decorator simply wrap a function, so it is possible to add functionality 
#to the original function, without actually modifying the original function itself
from functools import wraps

#Decorator for function that doens't take arguments
def decorator_without_arg(func):
    @wraps(func) #wraps decorator is applied to change the function name to the actualy function being call, not the wrapper!
    def wrapper():
        print("Preparing to yell!")
        func()
        print("Finish yelling!")
    return wrapper

@decorator_without_arg
def yell():
    print("Hello World~~~~!")

a = decorator_without_arg(yell)
print(a) #<function yell at 0x031A5610>

print(yell())# Preparing to yell!
            # Hello World~~~~!
            # Finish yelling!

#Decorator for function that takes arguments
def decorator_with_arg(func):
    @wraps(func) #wraps decorator is applied to change the function name to the actualy function being call, not the wrapper!
    def wrapper(*args, **Kwargs):   
        print("Preparing to yell!")
        func(*args, **Kwargs)
        print("Finish yelling!")
    return wrapper

@decorator_with_arg
def yell2(msg):
    print(msg)

b = yell2('This is a variable!')
print(b)# Preparing to yell!
        # This is a variable!
        # Finish yelling!

