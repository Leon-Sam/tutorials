class MyClass:
    """A simple class example"""
    i=12345 #This is scoped to the class globally, doesn't change with new instances

    def __init__(self,iData):
        self.data=[iData] # Self.X variables are scoped to the specific instance

        print(iData)
        print('Creating the object')

    def f(self):
        return self.data
    
    def OGcall(self):
        return 'OG Call'
    

x=MyClass('Leo')

print(x.i)
print(x.f())
print(x.__doc__)


class MyInheritedClass(MyClass):
    def __init__(self,name:str):
        print("Based from Myclass")
        self.name=name
     




y=MyInheritedClass('Simba')
print(y.name)
print(y.OGcall())

#TODO: Iterators

#TODO: Generators

launch control 50 hz