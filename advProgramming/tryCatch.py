# try:
#     with open('test.txt') as file:
#         print(file.read())
# except ValueError:
#     print("there is no file named tested test.txt")
# finally:
#     print('tested')
    
# try:
#     with open('test.txt') as file:
#         print(file.read())    
# except FileNotFoundError:
#     print("there is no file named tested test.txt")
    
def factorial(n):
    
    if n < 0:
        raise ValueError("Only positives numbers allowed!")
    
    k = 1
    for i in range(2, n+1):
        k*= i
    return k

print(factorial(3))