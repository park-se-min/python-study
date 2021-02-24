class test:
    def __init__(self):
        self.result = 0

    def add(self, b):
	    self.result +=  b
	    return self.result



class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


c = test()
print(c.add(1))
print(c.add(1))
print(c.add(1))




# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))