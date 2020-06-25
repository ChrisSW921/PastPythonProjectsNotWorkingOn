import webbrowser as web

def open_sites(mode):
    if mode == "ios":
        web.open('https://udemy.com', new=2)
        web.open('https://www.appbrewery.co/p/ios-course-resources/', new=1)
        web.open('https://stackoverflow.com', new=1)
        web.open('https://developer.apple.com/documentation/', new=1)

    elif mode == "uvu":
        web.open('https://my.uvu.edu', new=2)
        web.open('https://uvu.instructure.com', new=1)
        web.open('https://www.youtube.com/watch?v=lTRiuFIWV54', new=1)

    elif mode == "python":
        web.open('https://www.codecademy.com/learn', new=2)
        web.open('https://www.youtube.com/watch?v=lTRiuFIWV54', new=1)

open_sites('python')


