a= False
b= 10
c= 23

# If/Else Statement
if (a):
     b=c

elif (not a):
    print("A is not False")
else:
    print("Okay")

print(b)


#For loops

for val in range(10):
    print(val)

a = ['Mary', 'had', 'a', 'little', 'lamb']

for name in a:
    print(name)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

#For loop through a dict object
for k,v in knights.items():
    print(f'The name of the night is {k} and a horse {v}')

# Zip function: Merges lists together to iterate as a single unit
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#Enumerate function
print(enumerate(a)) # Returns item in list and the index numbe


# Do While Loop doesn't exist
# Switch case statements

a= 1
#While loop

while (a<10):
    print(a)
    a+=1

do