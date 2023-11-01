names = ["Paul", "Paula", "Peter"]
temperature = [13.5, 12.5, 40]
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)

#matrix = to 
# 1 2 3
# 3 4 5
# 5 6 7

#multiply the matrix by 2 ?

for row in matrix:
    for i in range(len(row)):
        row[i] = row[i] * 2
        
        
print(matrix)

#copy list

list1 = [1,2,3]

list2 = list1[:]

list2[0]= 100

print(list1)
print(list2)

#########################
print('################################')

def second_smallest(values: list) -> int:
    sortedList = sorted(values)
    return sortedList[1]

results = [12, 13, 4, 17, 124, 1]

ss = second_smallest(results)
print(ss)
print(results)