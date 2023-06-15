def a():
    return "hello " + b()


def b():
    return "my " + c()


def c():
    return "friend "


print(a())
