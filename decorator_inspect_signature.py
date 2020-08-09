from functools import wraps
from inspect import signature

# I was trying to write a simple decorator that add a forward slash into path,
# but I get to the interesting exploration of how function para info could be get from inspect.signature
# I guess due to its complexity so it isn't possible to write a boilerplate decorator for all functions
# it is easier to confine functino to be keyword arguments only

def check_path(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args):
            # get to the function input args list
            arg_lst = list(signature(eval(func.__name__)).parameters.keys())
            
            # find the target argument position
            pos = arg_lst.index('in_path')
            # update the list if anything changes 
            in_path = arg_lst[pos]
            if in_path[0] != '/':
                in_path = '/' + in_path
            arg_lst[pos] = in_path
            args = tuple(arg_lst)

        # for handling kw
        elif len(kwargs):
            in_path = kwargs['in_path']
            if in_path[0] != '/':
                in_path = '/' + in_path
            kwargs['in_path'] = in_path


        output = func(*args, **kwargs)
        return output
    return wrapper

@check_path
def do_something_arg(in_path):
    print(in_path)
    pass

@check_path
def do_something_kwarg(*, in_path=None):
    print(in_path)
    pass

do_something_arg('Documents')
do_something_kwarg(in_path='Downloads')
