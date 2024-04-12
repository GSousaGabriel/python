def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

next(g)

for j in g:
    print(j)

print("----------------------------")

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
print(next(cd))

print("----------------------------")

def firstn(n):
    nums = []
    num = 0

    while num< n:
        nums.append(num)
        num +=1
    return nums

print(firstn(12))

def firstn_generator(n):
    num = 0

    while num< n:
        yield num
        num +=1

print(firstn(12))

mygeneratorline = (i for i in range(10) if i%2 ==0)
mygeneratorline2 = [i for i in range(10) if i%2 ==0]

print(mygeneratorline)
print(mygeneratorline2)