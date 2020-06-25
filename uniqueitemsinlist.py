def returnUnique(lyst):
    unique = []
    for item in lyst:
        if lyst.count(item) == 2:
            continue
        else:
            unique.append(item)
    print(unique)


returnUnique([1,2,2,1,3,3,4,5,5,6,7,7])