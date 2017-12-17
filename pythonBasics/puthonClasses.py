#python class Examples

class Calculator:

    #Constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #getter
    def getX(self):
        return self.x

    #setter
    def setX(self,x):
        self.x = x

    def adds(self):
        add = self.x + self.y
        return add

    def subs(x,y):
        sub = x+y
        return sub

    def muls(x,y):
        mul = x*y
        return mul

    def divs(x,y):
        div = x/y
        return div


c = Calculator(10,20)
print(c.getX())
print(c.adds())
x=input('X vlaue ?')
#get Input from User
c.setX(x)
print(c.getX())
