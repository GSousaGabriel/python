from functools import reduce

def filter_values(values: list, criteria: callable):
    for value in values:
        if criteria(value):
            print(value, end=" ")

v= [12,3,4,5,5,7,7,568,967,2,423,4,6,-1,-654,-634,-12,-5]

def is_prime(number: int):
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

print(filter_values(v, lambda value: value>0 and value%2 == 0))
print(filter_values(v, lambda value: value>5))
print(filter_values(v, is_prime))

print("------------------------------")

def min_to_max(minimum: int, maximum: int):
    value = minimum
    while value<=maximum:
        yield value
        value +=1

gen = min_to_max(1, 10)

try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(gen)
except StopIteration:
    print("ended!")



values = [12,31,53,6]
m = list(map(lambda x: -x, values))
print(m)

val = reduce(lambda x,y: x+y, values)
print(val)