class MathDojo(object):
    def __init__(self):
        self.sum = 0
    def add(self, *args):
        for arg in args:
            if type(arg) is not int and type(arg) is not float:
                self.sum += sum(arg)
            else:
                self.sum += arg
        return self
    def subtract(self, *args):
        for arg in args:
            if type(arg) is not int and type(arg) is not float:
                self.sum - sum(arg)
            else:
                self.sum -= arg
        return self
    def result(self):
        return self.sum

md = MathDojo()

print md.add(2).add(2, 5).subtract(3, 2).result()

part2 = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()

print part2

part3 = MathDojo().add([1],3,4).add((3, 5, 7, 8), [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()

print part3

#print sum((2,4,6))
