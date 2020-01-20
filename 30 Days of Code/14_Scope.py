class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        a.sort(reverse=True)
        self.maximumDifference = a[0]-a[-1]

_ = input()
a = [int(e) for e in input().split(' ')]
print(a)
print(type(a))

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)