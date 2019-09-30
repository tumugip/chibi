def calc(s):
    print("s=",s)
    if "+" in s:

        nums = map(int,s.split('+'))
        #print('nums=',nums)
        return sum(nums)
    elif "*" in s:
        nums = map(int,s.split('*'))
        #print('nums=',nums)
        return 


print(calc("1"))
print(calc("1+2"))
print(calc("1+2+3"))
