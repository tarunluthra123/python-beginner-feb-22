s = "Python is amazing"
s2 = "Python is amazing"
s3 = "Python is awesome"


# Multiline string
books = """
Harry Potter and the Philospher's Stone
Harry Potter and the Chamber of Secrets
Harry Potter and the Half Blood Prince
"""


# This would be interpreted as a comment
"""
This is a comment
spanning
over 
multiple 
lines
"""


def hello():
    """
    This is a docstring
    """
    print("Hello")


help(hello)

print(type(s))
print(type(s2))


print(id(s))
print(id(s2))

print(books)
print(type(books))
