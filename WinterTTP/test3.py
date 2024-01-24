time = input("Enter four digits: ")
time = time.split()
result = []
for i in range(4):
    if i == 0:
        if 2 in time:
           result.append(2)
           time.remove(2) 
        elif 1 in time:
            result.append(1)
            time.remove(1)
        elif 0 in time:
            result.append(0)
            time.remove(0)
        else:
            result.append(0)
    if i == 1:
        if result[0] == 2:
            for x in range(4, -1, -1):
                if x in time:
                    result.append(x)
                    time.remove(x)
                    break
            if len(result) == 1:
                result.append(0)
        else:
            result.append(max(time))
            time.remove(result[1])
    if i == 2:
        for x in range(5, -1, -1):
            if x in time:
                result.append(x)
                time.remove(x)
                break
            if len(result) == 2:
                result.append(0)
    result.append(max(time))
print(result)
    

