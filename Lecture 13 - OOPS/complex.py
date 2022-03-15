class ComplexNumber:
    """
    This class represents complex numbers
    """

    real = 0
    imaginary = 0

    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def output(self):
        print("{} + {}i".format(self.real, self.imaginary))


# 5 + 3i
x = ComplexNumber(5, 3)
x.output()

# x = ComplexNumber()
# x.real = 5
# x.imaginary = 3
# x.output()


# 10 - 2i
y = ComplexNumber(10, -2)
y.output()


print("Complex.py", __name__)
if __name__ == "__main__":
    print("This is the main program in complex.py")
