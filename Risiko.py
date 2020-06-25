def risiko(attacker, defender):
    att = sorted(attacker, reverse=True)
    deff = sorted(defender, reverse=True)
    armies_lost = 0
    index = 0 

    for item in att:
        if item > deff[index]:
            armies_lost += 1
            print("Defender loses and army!")
        index += 1
    print(f'Defender lost {armies_lost} armies')

risiko([6,6,5],[2,3,6])

