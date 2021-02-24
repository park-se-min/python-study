class fourCal:
    asdf = 0
    asdf2 = 10
    asdf3 = 30

    def __init__(self, a, b):
	    self.aaa = a
	    self.bbb = b

    def start(self, a, b):
	    self.aaa = a
	    self.bbb = b

    def add(self):
	    return self.aaa + self.bbb

    def add2(self):
	    return self.asdf2 + self.asdf3

    def mul(self):
        return self.aaa * self.bbb

    def sub(self):
        return self.aaa - self.bbb

    def div(self):
        return self.aaa / self.bbb


class moreFourCal(fourCal):
    def pow(self):
	    return self.aaa ** self.bbb

    def div(self):
	    if self.aaa == 0 or self.bbb == 0:
		    return 0
	    else:
	        return self.aaa / self.bbb

class moreFourCal2(moreFourCal):
    pass


c = moreFourCal2(3, 4)
a = moreFourCal(3, 4)
b = fourCal(3, 4)

print(a.add2())
print('--------')

print(a.add())
print(b.add())

print(a.pow())
print(a.div())

print(b.div())
# print(b.pow())


print(c.add())
print(c.pow())
print(c.div())