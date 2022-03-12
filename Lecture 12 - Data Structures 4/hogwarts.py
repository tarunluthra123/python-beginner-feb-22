def hogwarts(house1, house2, house3, house4, *args, **kwargs):
    print("Houses are ", house1, house2, house3, house4)
    print()
    print("Args :", args)
    print()
    print("Kwargs :", kwargs)


hogwarts(
    "Gryffindor",
    "Ravenclaw",
    "Hufflepuff",
    "Slytherin",
    "Severus Snape",
    "Horace Slughorn",
    "Remus Lupin",
    headmaster="Albus Dumbledore",
    deputy_headmistress="Minerva McGonagall",
)
