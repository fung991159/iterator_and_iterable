#first class function is a function that could be assigned to an object
#So it can be assigned to a variable
def yell(msg):
    print(msg)
a = yell
print(a) #<function yell at 0x006D8898>


#higher order function is a function that takes at least one parameter which is itself a function
#here a custom function that simulate standard map function were used
def square(num):
    return num*num

def my_map(func, list_to_apply):
    result=[]
    for item in list_to_apply:
        result.append(func(item))
    return result
print(my_map(square, [1,2,3,4,5])) #[1, 4, 9, 16, 25]