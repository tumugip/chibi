
class Val(object):
    __slots__ = ['value']
    def __init__(self,value=0):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value


class Add(object):
    __slots__ = ['left','right']
    def __init__(self,left,right):
        self.left = left    #left,rightは式
        self.right = right
    def eval(self):
        return self.left.eval() + self.right.eval()

    
class Mul(object):
    __slots__ = ['left','right']
    def __init__(self,left,right):
        self.left = left
        self.right = right
    def eval(self):
        return self.left.eval() * self.right.eval()


e=Add(Val(1),Val(2))
assert e.eval()==3

e = Add(Add(Val(1),Val(2)),Val(3))
assert e.eval()==6


e = Mul(Val(1),Val(2))
assert e.eval() == 2