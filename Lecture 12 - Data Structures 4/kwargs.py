def hello(**kwargs):
    print(kwargs)
    print(type(kwargs))


hello()
hello(name="Peter Parker", age=20, villains=["Venom", "Electro"])
