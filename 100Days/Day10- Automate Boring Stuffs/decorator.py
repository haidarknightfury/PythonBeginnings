"""
Decorator must always return a function
takes as input a function
"""
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return inner_func

@print_args
def multiply(num_a, num_b):
    return num_a * num_b

if __name__ == "__main__":
    print(multiply(3,5))