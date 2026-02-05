def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet():
    print("Hello, World!")
greet()

# parameterized decorator

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        result = func(*args, **kwargs)
        print("After calling the function.")
        return result
    return wrapper
@decorator
def add(a,b,c,d):
    return a + b + c + d
print(add(1,2,3,4))
