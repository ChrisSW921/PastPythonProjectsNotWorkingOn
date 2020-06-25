import random
def give_subject_and_tense():
    tenses = ['present','past','conditional','future','command',
              'two subject','any tense']
    subjects = ['animals','food','technology','nature','prepositions','things in a house','things in a city',
                'parts of the body','verbs','anything','sports','clothes','family']

    tense = random.choice(tenses)
    subjects_chosen = []
    for _ in range(3):
        subjects_chosen.append(random.choice(subjects))
    print(tense)
    if 'anything' in subjects_chosen:
        print('anything')
    else:
        print(subjects_chosen)

give_subject_and_tense()