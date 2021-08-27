#Basic function defintion
def add(a,b):
   return a+b

# Function with default parameters
def do_something(a=10,b=2):
   return a+b

print(do_something(13))

print(add(3,4))

#Non keyword arguments
def fancy_fun(test=10,*argv):
   for arg in argv:
      print(arg)


fancy_fun(10,'ok','this is', 'a nonkey word arg', '*argv')


#Keyword arguments
def keyword_args(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

# Driver code
keyword_args(first ='Geeks', mid ='for', last='Geeks')  

#Lambdas
lambda_squared= lambda x: x*x
lambda_powered= lambda x,y:x**y

print(lambda_squared(4))
print(lambda_powered(2,3))


def test_doc_string(best_parameter:int=420):
   """
   This documents how document strings work
   """
   return best_parameter


