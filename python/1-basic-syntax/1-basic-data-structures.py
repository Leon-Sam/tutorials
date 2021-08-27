#This is a comment
print("Starting test for boolean types")

# This is a variable and it's types
boolean_example=True
boolean_false_example=False

print("1",True or False)
print("2",True and True)
print("3",not False)

#Comparsion checks
print("4", 1<2)
print("5",2<=2)
print("6",1 is 1)

print("Starting number data types")
int_example= 1
float_example =2.2
complex_example= complex(1,3)
print(int_example)
print(float_example)
print(complex_example)


print ("Starting string data types")
example="testing"
two='testing'
print(two[2]) # Pick a character out of string 

# String slicing
# [firstIndex(included),lastIndex(exluded),skipValue] 
# Negative numbers start counting from the right
print(two[::-1])
print("Slice2:",two[::1])
print("Reversed",two[::-1])

#Iterator object: Creates an object that allows you to loop through it
#You can create a custom object with __iter__ and __next__ functions

itr_value='thinkpad'
itr_obj=iter(itr_value)

while True:
    try:
        item=next(itr_obj)
        print(item)
    except StopIteration:
        break

# Sequence types: list, tuple, range

# Lists
# Enclosed in square brackets []
# Are mutable
ex_list=[1,2,4,5,66,3,3,2]

# List comprehension
new_list = [x*x for x in ex_list  if x ==2]

print(new_list)


# Ranges
range(10)
print(range(5))

for i in range(10):
    print(i)

# Tuples
# Denoted by ()
# immutable and generally faster
tuple_example =(4,2,1)
print(tuple_example)

#Set data type
# Denoted by {}
# Unordered
# Duplicates are represented only once

set_example=  {'5','3','dog','test'}
print('5' in set_example) #Checks for set membership
print ('hai' in set_example)

#Dict data type
#Denoted by {}
#Mutable, unordered
# Used to represent key-value pairs

dict_example={'test1':334,'test2':22}
print(dict_example)


# How to do better string formatting
year = 2016

event= 'texas2k'
#String literal formatting
print(f'Results of the {year} {event}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
    print(f'Customer name {name:10} ==>>>> number: {phone:10d}')