class Person:
    a = 0

    def __init__(self, initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.a = initialAge

    def amIOld(self):
        if self.a < 13:
            print("You are young.")
        elif 13 <= self.a < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.a += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
        p.amIOld()
    print("")
