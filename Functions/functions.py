def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open("centred", mode='w') as centered_file:
# call the function
# print(python_food())
#     centre_text("spam and eggs", file=centered_file)
#     centre_text("spam, spam and eggs", file=centered_file)
#     centre_text(12, file=centered_file)
#     centre_text(0b1001, file=centered_file)
#     centre_text(0x1F0D, file=centered_file)
#     centre_text("spam, spam, spam and spam", file=centered_file)
#
#     # print("first", "second", 3, 4, "spam")
#     centre_text("first", "second", 3, 4, "spam", file=centered_file)
#     centre_text("first", "second", 3, 4, "spam", sep=":", file=centered_file)

# print(centre_text("spam and eggs"))
# print(centre_text("spam, spam and eggs"))
# print(centre_text(12))
# print(centre_text(0b1001))
# print(centre_text(0x1F0D))
# print(centre_text("spam, spam, spam and spam"))
#
# # print("first", "second", 3, 4, "spam")
# print(centre_text("first", "second", 3, 4, "spam"))
# print(centre_text("first", "second", 3, 4, "spam"))

with open("menu", mode='w') as menu:
    s1 = centre_text("spam and eggs")
    print(s1, file=menu)
    print(centre_text("spam, spam and eggs"), file=menu)
    print(centre_text(12), file=menu)
    print(centre_text(0b1001), file=menu)
    print(centre_text(0x1F0D), file=menu)
    print(centre_text("spam, spam, spam and spam"), file=menu)

    # print("first", "second", 3, 4, "spam")
    print(centre_text("first", "second", 3, 4, "spam"), file=menu)
    print(centre_text("first", "second", 3, 4, "spam"), file=menu)

