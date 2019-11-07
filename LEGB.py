#LEGB = Local, Enclosing, Global, Built-in

global z
z = 'global z'          #global variable is available in all namespaces, usually not a good idea to use it
def outer():
    x = 'outer x'        #local var for outer func, but alos is enclosing var for inner func
    y = 'outer y'
    def inner():
        nonlocal y        #non-local variable will bring alter the variable in the upper level, but will not affect the global namespace
        x = 'inner x'     #if this line is commented out, x value will become outer x
        y = 'inner y'
        print(x, y, z)

    inner()
    print(x, y, z)
    
outer()

import builtins
def min():
    pass
m = min([5,1,4,2,3])    #ERROR: because the built in function min has been replaced by custom min function


