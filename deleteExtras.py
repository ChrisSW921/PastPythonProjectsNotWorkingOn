def delete_occurences(lyst, num):
    new = []
    seen = []
    for item in lyst:
        if item in seen:
            continue
        else:
            if lyst.count(item) >= num:
                seen.append(item)
                for _ in range(num):
                    new.append(item)
    print(new)


delete_occurences([1,1,1,1,1,3,3,3,4,4,4,None,None,5,5,],3)
