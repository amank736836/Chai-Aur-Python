username = "Aman Kumar"


def test():
    pass


def func():
    username = "Aman"
    print(username)


def innerFunc():
    print(username)


print(username)
func()
innerFunc()

x = 99


def func2(y):
    z = x + y
    return z


result = func2(1)
print(result)


def func3():
    global x
    x = 88


func3()
print(x)

x = 99


def f1():
    x = 88

    def f2():
        print(x)

    return f2


myResult = f1()
myResult()
print(x)


def amanCoder(num):
    def aman(x):
        return x**num

    return aman


square = amanCoder(2)
cube = amanCoder(3)

print(square(2))

print(cube(2))
