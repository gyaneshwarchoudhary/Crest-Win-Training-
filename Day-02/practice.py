#  numeric data type 
variable_int = 1
print(type(variable_int))
variable_float = 12.34 # float 
variable_complex = 3 + 5j # complex 

# squential datatypes
variable_string = "hey" # str datatype 
variable_list = [1,2,3,4] # list 
variable_tuple = (1,2,3) # tuple datatype

# mapping and set dattype 
variable_dict = {"a":1,"b":2} # dictionary
variable_set = {1,2,3,4} # set 
variable_frozen_set = ({1,2,3,4}) # frozenset

# boolean 
variable_bool = True # bool 


# control flow 

first_integer = 10
second_integer = 20

if first_integer < second_integer:
    print(f'{first_integer} < {second_integer}')
elif first_integer > second_integer:
    print(f'{first_integer} > {second_integer}')
else:
    print(f'{first_integer} = {second_integer}')

