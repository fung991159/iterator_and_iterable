from time import perf_counter
from functools import wraps

#Decorator for function that doens't take arguments
def decorator_time_logger(func):
    @wraps(func) #wraps decorator is applied to change the function name to the actualy function being call, not the wrapper!
    def wrapper(*args,**kwargs):
        t1_start = perf_counter() 
        val = func(*args,**kwargs)   #capture the returned value in wrapper, otherwise it would be lossed
        t1_stop = perf_counter() 
        print(f"Elapsed time: {round(t1_stop - t1_start,2)} sec(s)")  
        return val
    return wrapper

@decorator_time_logger
def func_that_takes_time(num_of_times):
    total = 1
    for i in range(1, num_of_times):
        total += i*i
    return total

a = func_that_takes_time(200035) #Elapsed time: 0.36 sec(s)
print(a)                         #2668046904713686