def tallestSkyscraper(lyst):
    buildings_height = {}
    key = 0
    for item in lyst[0]:
        buildings_height[key] = 0
        key += 1

    for item in range(0, len(lyst)):
        index = 0
        for x in range(0, len(lyst[0])):
            buildings_height[x] += lyst[item][index]
            index += 1

    print(f'Highest skyscraper is {max(buildings_height.values())} stories high')



tallestSkyscraper([[1,0,0],
                    [1,1,0],
                    [1,1,0],
                    [1,1,1],
                    [1,1,1]
                    ])
