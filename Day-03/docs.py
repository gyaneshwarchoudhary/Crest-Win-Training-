import sys

"""
Topics: 
 - funcutions and modules
 - git pr workflow
 - basic bash scripting 
"""


"""
Functions:
 - block statements 
 - DRY
 - Code readable, maintainable, reusable and modular
 - also have multiple arguments like default, postional, arbitrary args
 - user definend, builtin, lambda, and recursive function
"""

# defining a function with args and kwargs
def function_name(*args,**kwargs):
    """
    Docstring for function_name
    
    :param args: Description
    :param kwargs: Description
    """
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} have the value {value}')

function_name(1,2,3,4,{"a":10,"b":12})
print(function_name.__doc__) 
help(function_name)   



# pass by value and pass by reference 
def change_integer(value):
    value * 2   # make a copy of the value and stores the value calculates the result and forget it 
og_value = 5 # created a og value and stored the numver 5 
change_integer(og_value)
print(og_value)


# analogy - 
    # - pass by value means giving a copy of the notebook to the frient 
    # - pass by ref means sharing a notebook to the friend



# closures in python
def mult(value1):
    """
    provides the isolation that the inner vribales can be hidden 
    biggest use case is decorator 
    """
    def multiplier(value2):
        return value1 * value2
    return multiplier
mult1 = mult(5)

print(mult1(2))


## python virtual environments
# befor virtaul environment activation 
print(sys.prefix)  # C:\Users\gyaneshwar\AppData\Local\Programs\Python\Python312
print(sys.executable) # C:\Users\gyaneshwar\AppData\Local\Programs\Python\Python312\python.exe

# after vir en activation 

print(sys.prefix)  # D:\Training\Day-03\venv
print(sys.executable) # D:\Training\Day-03\venv\Scripts\python.exe


"""
Github pull request 
 - pr lets you propose, review and merge code changes
 - draft pull request 
 - fork-> Local changes -> branch -> commit -> push -> create a pr -> review/discussion -> if not conflicts -> merge
 -                                    ^                                                   | 
                                      |                                                   | if conflict)
                                      |                                                   | 
                                      |___________________________________________________| resolve the conflict-> merge
"""     

# Bash (bourne Again shell)
"""
- translator, cli and scripting for linux/unix
- REPL
- benefit automation 100 file
- .bashrc 
- Aliases, env variahles, the paths, functions, 
"""