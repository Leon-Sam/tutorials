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
print(two[::-1])

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



