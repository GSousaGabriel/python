#f = open('./intro/data.txt', 'a')
#f.close()

with open("./intro/values.csv") as file:
    valuesToReplace = []
    
    for line in file:
        fixedLine = line.replace("\n", "")
        fixedLine = fixedLine.split(",")
        fixedLine = [int(value) for value in fixedLine]
        print(fixedLine)
        valuesToReplace = valuesToReplace + fixedLine
        
    #file.seek(0)
    #test = file.read()
    #print(test)
    print(valuesToReplace)
    
with open("./intro/test.txt", "w") as file:
    #file.write('tested writing\n')
    #file.write('second tested writing')
    data_to_write = [1,2,3,4,5,6,6,7,3,8,8,2,42]
    data_to_write_string = [str(value) for value in data_to_write]
    file.write(",".join(str(data_to_write)))