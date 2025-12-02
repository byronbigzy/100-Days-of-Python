def logging_decorator(function):
    def wrapper_function(*args):
        result = function(*args)
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {result}")
    return wrapper_function

@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)
'''
import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        function()
        runspeed = time.time() - current_time
        print(f"{function.__name__} run speed: {runspeed}")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
'''