import complex


# 7 + 2i
z = complex.ComplexNumber(7, 2)
z.output()

# If this is the source file being executed, then run some special code for this
# if __name__ == "__main__":
# print("This is the main program in modules.py")


print("Modules.py", __name__)


help(int)
