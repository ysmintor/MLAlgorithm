with open('2014 and 2015 CSM dataset.csv') as file:
    file.readline()

    for line in file:
        currLine = line.strip().split(',')
        lineArr = []
        lineArr.extend(currLine[-6:])
        # lineArr.extend(currLine[7:13])
        # lineArr.extend(currLine[-3:])
        print('lineArr', lineArr)

print([1,2,3])
print(['1','2','3'])
data = ['1','2','3']
data = map(int, data)
print(list(data))