def number_of_vowels(sentence: str) -> int:
    return len([c for c in sentence if c in "aeiouy"])

def number_of_other(sentence: str) -> int:
    return len(sentence) - number_of_vowels(sentence)

def shout(sentence: str):
    sentence+= "!"
    print(sentence)
    shout(sentence)

#shout("Hello")

def fill_list(values: list):
    if len(values) < 32:
        values.append(0)
        fill_list(values)
    return list

numbers = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 4, 5, 6]
fill_list(numbers)
print(numbers)

while len(numbers2) < 32:
    numbers2.append(0)
print(numbers2)

def factorial(n: int)->int:
    if n < 2:
        return 1
    
    return n * factorial(n - 1)

print(factorial(3))

def fibo(n: int)->int:
    if n <= 2:
        return 1
    
    return fibo(n - 1) + fibo(n - 2)

print(fibo(4))