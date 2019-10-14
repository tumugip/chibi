class Expr(object):
    pass


class Val(Expr):
    __slots__ = ['value']
    def __init__(self,value=0):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value


v=Val(1)
print(v)
assert v.eval() == 1

assert isinstance(v,Expr)   #==>True
assert isinstance(v,Val)    #==>True


class Binary(Expr):
    def __init__(self,left,right):
        self.left = left
        self.right = right
    def __repr__(self):
        classname = self.__class__.__name__
        return f'{classname}({self.left},{self.right})'
    def eval(self):
        pass





def toExpr(a):
    if not isinstance(a,Expr):
        a=Val(a)
    return a

class Add(Expr):
    __slots__ = ['left','right']
    def __init__(self,left,right):
        self.left = toExpr(left)    #left,rightは式
        self.right = toExpr(right)
    def eval(self):
        return self.left.eval() + self.right.eval()


e = Add(1,Add(1,2))
print(e.eval())
assert e.eval() == 4

    
class Mul(Expr):
    __slots__ = ['left','right']
    def __init__(self,left,right):
        self.left = toExpr(left)
        self.right = toExpr(right)
    def eval(self):
        return self.left.eval() * self.right.eval()


class Sub(Expr):
    __slots__ = ['left','right']
    def __init__(self,left,right):
        self.left = toExpr(left)
        self.right = toExpr(right)
    def eval(self):
        return self.left.eval() - self.right.eval()



class Div(Expr):
    __slots__ = ['left','right']
    def __init__(self,left,right):
        self.left = toExpr(left)
        self.right = toExpr(right)
    def eval(self):
        return self.left.eval() // self.right.eval()

e=Add(1,2)
assert e.eval()==3
print(e.eval())


e=Add(1,Mul(2,3))
print(e.eval())