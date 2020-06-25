import wikipedia as wiki
import webbrowser as web

def display_page():

    searches = input("Search for wikipedia article to read: ")
    if not searches:
        return False
    lang = input("fr = French, en = English, es = Spanish--Enter Language: ")

    if lang not in ['fr', 'en', 'es']:
        print("Not a valid language. Try again")
        display_page()
    wiki.set_lang(lang)

    try:
        suggest = wiki.search(searches)
        page = wiki.page(suggest[0])
        web.open(page.url, new=2)
        if searches:
            display_page()
    except:
        print("No such article! Search again")
        display_page()




def main():
    while True:
        if not display_page():
            break

main()