#add Implementation
def add(x,y):
    return x+y
#substrack Implementation
def substrack(x,y):
    return x-y   #on master branch
#multiply Implementation
def multiply(x,y):
    return x*y   # on Bug456
#divide Implementation
def divide(x,y):
    if y==0 :           #on Bug789 branch
        return Divide_By_0_Error
    else:
        return x/y
#Square Implementation
def square(x):
    return x*x

