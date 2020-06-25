def censor_string(txt, lyst):
    new = []
    splits = ['.',',','?','!',';',' ']
    final = {}
    censored = []
    done = []
    for item in txt.split(' '):
        new.append(item)
    for item in new:
        cens = ""
        cens2 = ""
        if item[-1] in splits:
            if item[:-1] in lyst:
                for _ in range(len(item)-1):
                    cens += "*"
                cens += item[-1]
                done.append(cens)
            else:
                done.append(item)
        elif item in lyst:
            for _ in range(len(item)):
                cens2 += "*"
            done.append(cens2)
        else:
            done.append(item)


    print(new)
    print(" ".join(done))

censor_string("Hello there my friend! How are you? Good.", ['Hello', "Good", "my"])
