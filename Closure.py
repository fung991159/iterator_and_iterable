#Closure is just a first class function with embeddeed value,
# as the example below msg was embedded in the inner function

def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

print(hi_func(), hello_func()) #Hi, Hello