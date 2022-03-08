apple_count = 4
orange_count = 5
guava_count = 10


# I have 4 apples, 5 oranges, 10 guavas


# s = (
#     "I have "
#     + str(apple_count)
#     + " apples, "
#     + str(orange_count)
#     + " oranges, and "
#     + str(guava_count)
#     + " guavas."
# )


# s = f"I have {apple_count} apples, {orange_count} oranges, and {guava_count} guavas."
apple_count = 4
orange_count = 5
guava_count = 10
s = "I have {} apples, {} oranges, and {} guavas.".format(
    apple_count, orange_count, guava_count
)

print(s)
