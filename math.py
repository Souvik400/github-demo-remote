#Add Implementation
def add(x,y):
    return x+y
#Substrack Implementation
def substrack(x,y):
    return x-y   #on master branch
#Multiply Implementation
def multiply(x,y):
    return x*y   # on Bug456
#Divide Implementation
def divide(x,y):
    if y==0 :           #on Bug789 branch
        return Divide_By_0_Error
    else:
        return x/y

