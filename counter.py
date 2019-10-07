
class Counter(object):
    def __init__(self): #コンストラクタ 第一引数はself
        self.cnt = 0
    
    def count(self):
        self.cnt +=1

    def reser(self):
        self.cnt = 0

    def show(self):
        print(self.cnt)

    def doublecount(self):
        self.cnt += 2

    def __repr__(self): #文字列を返すと表示される
        return str(self.cnt)

c = Counter()
c.show()
c.count()
c.show()
c.doublecount()
c.show()
print(type(c))
print(c)


