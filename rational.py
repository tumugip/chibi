import math
class Q(object):
    def __init__(self,a,b=1):
        self.a = a
        self.b = b
    def __repr__(self): 
        if self.b == 1:
            return  str(self.a) 
        self.c = math.gcd(self.a,self.b)
        if self.a % self.c ==0 and self.b % self.c == 0:
            self.d = self.a // self.c
            self.e = self.b // self.c
            return f'{self.d}/{self.e}'
        return f'{self.a}/{self.b}'
    
    
    def __add__(self,q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d+b*c,b*d)


    def __sub__(self,q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d-b*c,b*d)


    def __mul__(self,q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*c,b*d)

    def __truediv__(self,q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d,b*c)

    

        

q=Q(2,4)
print(q)


