import re

pattern = re.compile("")

while True:
    word = input("Test, empty quits:")
    if not word:
        break

    if pattern.search(word):
        print("on")
    else:
        print("wrong")