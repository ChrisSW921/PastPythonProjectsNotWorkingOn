def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

class to_do_list:
    def __init__(self, items):
        self.items = items

    def d(self, item):
        for task in self.items:
            if task == item:
                self.items.remove(task)
        self.show_list()

    def show_list(self):
        print("TO DO LIST")
        for i in range(10):
            print('-',end='')
        print('')
        for item in self.items:
            print(f'{item}')
        for _ in range(3):
            print('')

    def md(self, item):
        for task in item:
            print(task)
            self.items[self.items.index(task)] = strike(task)
        self.show_list()

    def a(self, item):
        self.items.extend(item)
        self.show_list()

    def c(self):
        self.items.clear()
        self.show_list()



lyst = to_do_list(["do this", "do that", "Do that too"])

lyst.c()
lyst.a(['Study French and Spanish','Code a flash card app','Go biking', 'Work','Eat Lunch','study IOS','French call'])
lyst.md(['study IOS','French call'])





