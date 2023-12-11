line = "1,2,3,4,2,4,5,2,5,3,46,4,333,222"
items = line.split(",")
values= [int(item) for item in items]
print(values)

sentence = "hello for all viewers of this code!"
all_caps = " ".join([word.upper() for word in sentence.split()])
print(all_caps)

def factorial(value: int) -> int:
    k= 1
    for i in range(2, value + 1):
        k*= i

    return k

values = [1, 5, 4, 6, 7, 2, 3, 8]
factorials= [factorial(value) for value in values]
print(factorials)


values = [1, 5, 4, 6, 7, 2, 3, 8]
even = [number for number in values if number % 2 == 0]
print(even)


values = [1, -5, 4, -6, 7, 2, 3, -8]
absolute = [abs(number) for number in values]
print(absolute)

values = [1,2,3,4,5,6,7,8,9]
dictN = {number: number * 10 for number in values}
print(dictN)

from string import ascii_lowercase

char_amounts = {letter: 0 for letter in ascii_lowercase}
print(char_amounts)

sentence = "a little red cat is walking outside"
for char in sentence:
    char_amounts[char] = sentence.count(char)
print(char_amounts)

letters = list("abcdefg")
numbers = [10,20,30,40,50,60,70]
comb = zip(letters, numbers)
print(list(comb))

dictComb = {key: value for key, value in zip(letters, numbers)}
print(dictComb)

d1 = {1: 10, 2: 20, 3: 30, 4: 40}
d2 = {value: key for key, value in zip(d1.keys(), d1.values())}
print(d2)