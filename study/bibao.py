def outer(a):
    b = 10

    def iner():
        print(a + b)
    return iner


if __name__ == "__main__":
    deco = outer(5)
    deco()
    deco = outer(10)
    deco()
