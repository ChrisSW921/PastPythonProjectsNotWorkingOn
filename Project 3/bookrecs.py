from operator import itemgetter
booklist = []
ratings1 = []
ratingsfinal = {}
dots = []
all_keys = []
y = 1
with open("booklist.txt") as books:
    booksfinal = [tuple(line.strip().split(',')) for line in books]
with open("ratings.txt") as ratings:
    for line in ratings:
        if len(line) < 20:
            ratings1.append(line.strip().lower())
        else:
            ratings1.append(line.strip())
for x in ratings1:
    if len(x) < 20:
        ratingsfinal[x] = list(ratings1[y].strip().split())
        y += 2
dicti = {}    
def dot_prod(v,b):
    """Get the affinity score between two people"""
    j = 0
    vlist = []
    blist = []
    added = []
    for val in ratingsfinal.get(v):
        vlist.append(int(val))
    for val in ratingsfinal.get(b):
        blist.append(int(val))
    for a in vlist:
        added.append(a * blist[j]) 
        j += 1
    dots.append(sum(added))
    dicti[b] = sum(added)

def dot_prods_all(person):
    """Get the affinity score for every other person to find the highest"""
    dots.clear()
    all_keys.clear()
    dicti.clear()
    for key in ratingsfinal.keys():
        all_keys.append(key)
    for n in all_keys:
        if n != person:
            dot_prod(person, n)
   
def friends(person, nfriends=2):
    """Returns the two friends of person"""
    dot_prods_all(person)
    sorted1 = sorted(dots, reverse = True)
    friends1 = []
    friends2 = []
    for h in range(nfriends):
        friends2.append(sorted1[h])
    for key in all_keys:
        if dicti.get(key) in friends2 and len(friends1) < nfriends:
            friends1.append(key)
    friends3 = sorted(friends1)
    return friends3
                    
    
def recommend(name, nfriends = 2):
    """Returns a list of recommended books"""
    starting_index = 0
    friends_list = friends(name,nfriends)
    names_books = ratingsfinal[name]
    friend1_books = [ratingsfinal[item1] for item1 in friends_list]
    x_books = []
    xc = -1
    list_books = []
    first = []
    last = []
    names = []
    title = []
    final = []
    list_books.clear()
    for _ in names_books:
        if names_books[starting_index] == '0':
            for t in friend1_books:
                if t[starting_index] in ['3', '5']:
                    if booksfinal[starting_index] not in x_books:
                        x_books.append(booksfinal[starting_index])
        starting_index += 1
    sorted_x_books = sorted(x_books)
    for book in sorted_x_books:
        list_books.append(list(book))
    for q in list_books:
        for t in q:
            if t == q[0]:
                names.append(t)
            else:
                title.append(t)
    for w in names:
        xc = 0
        if w == 'Shueisha':
            last.append(w)
            first.append(w)
        else:
            for c in w[::-1]:
                if c == " ":
                    last.append(w[xc:])
                    first.append(w[:xc-1])
                    break
                xc -= 1
    merged_list = list(zip(first,last,title))
    sorted1 = sorted(merged_list, key=itemgetter(1,0,2))
    for r in sorted1:
        for g in sorted_x_books:
            if r[2] == g[1]:
                final.append(g)           
    return final
              
def report():
    """Returns the final report of the code"""
    p = ""
    new_keys = []
    for z in ratingsfinal.keys():
        new_keys.append(z)
    sorted_keys = sorted(new_keys)
    for d in sorted_keys:
        finals = recommend(d)
        recbookprint = ""
        for item in finals:
            recbookprint += f'\t{item}\n'
        p += f'{d}: {friends(d)}\n{recbookprint}\n'
    return p
 
def main():
    """ Prints recommendations for all readers """
    with open("recommendations.txt", "w") as rec_file:
        print(report(), file=rec_file)
    

if __name__ =='__main__':
    pass
