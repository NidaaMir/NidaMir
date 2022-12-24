# Global and local Variables

num1 = 2  # global


def add():
    num2 = 1  # local
    sum = num1 + num2
    print(sum)


add()


def add1():
    num3 = 3
    num4 = 7
    sum1 = num3 + num4
    print(sum1)

    def add2():
        num5 = 5  # nonlocal
        sum2 = sum1 + num5
        print(sum2)

    add2()


add1()


def add3():
    num6 = int(input("Enter a num: "))
    num7 = int(input("Enter another num: "))
    sum3 = num6 + num7
    print(sum3)


add3()
