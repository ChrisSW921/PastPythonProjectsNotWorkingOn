from breezypythongui import *

cards = {'No cards added!':'No cards added!'}
french = ['No cards added!']
english = ['No cards added!']

def split_to_list(word):
    english.append(word)
    french.append(cards[word])
    
class mainWindow(EasyFrame):
    """Sets up first window"""
    def __init__(self):
        EasyFrame.__init__(self,title='Flash Cards')
        self.current_index = 0
        self.lang = "English"
        self.setBackground("sky blue")
        self.button1 = self.addButton(text="Add Card", row=2, column=0, rowspan = 1, columnspan = 1, command = self.add_Button)
        self.button2 = self.addButton(text="Flip Current Card", row=2, column=1, rowspan = 1, columnspan = 1, command = self.flip_Button)
        self.button3 = self.addButton(text="View All Cards", row=2, column=2, rowspan = 1, columnspan = 1, command = self.show_Button)
        self.button4 = self.addButton(text="Show New Card", row=2, column=3, rowspan = 1, columnspan = 1, command = self.new_card_Button)
        self.card_area = self.addTextField(text= english[self.current_index], row=0,column=1,rowspan = 1,columnspan = 2,width = 20,state = DISABLED)
        self.label = self.addLabel(text="English: ", row=0, column=1,
     columnspan = 1,
     rowspan = 1,
     font = None,
     background = 'white',    
     foreground = 'black')
        
    def add_Button(self):
        add = add_Response(self, "Add card")
        if add.modified():
            cards[add.english.getText()] = add.french.getText()
            split_to_list(add.english.getText())
            self.messageBox("hello", "Card added!",
                                width = 50)    
        else:
            self.messageBox("Error", "Enter values in both boxes", width = 50)
            
    def flip_Button(self):
        if self.lang == "English": 
            self.card_area.setText(french[self.current_index])
            self.lang = "French"
            self.label = self.addLabel(text="French: ", row=0, column=1,columnspan = 1,rowspan = 1,font = None,background = 'white',    foreground = 'black')
        else:
            self.card_area.setText(english[self.current_index])
            self.lang = "English"
            self.label = self.addLabel(text="English: ", row=0, column=1,columnspan = 1,rowspan = 1,font = None,background = 'white',    foreground = 'black')
        
    def show_Button(self):
        all_cards = ""
        for x in english[1:]:
            all_cards += x + '----' + cards[x] + '\n'
        self.messageBox("All Flash Cards", all_cards, width = 100, height = 10)
        
    def new_card_Button(self):
        try:
            self.current_index += 1
            self.card_area.setText(english[self.current_index])
            self.label = self.addLabel(text="English: ", row=0, column=1,columnspan = 1,rowspan = 1,font = None,background = 'white',foreground = 'black')
            self.lang = "English"
        except:
            self.current_index = 1
            self.card_area.setText(english[self.current_index])
            self.label = self.addLabel(text="English: ", row=0, column=1,columnspan = 1,rowspan = 1,font = None,background = 'white',    foreground = 'black')
            self.lang = "English"
class add_Response(EasyDialog):
    """All functions relating to friends"""
    def __init__(self, parent, title):
        EasyDialog.__init__(self, parent, title)
 
    def body(self, parent):
        """Body function"""
        self.addLabel(parent,
                     text="English:", row=0, column=0,
                     columnspan = 1,
                     rowspan = 1,
                     sticky = N+W,
                     font = None,)
        self.addLabel(parent,
                     text="French:", row=1, column=0,
                     columnspan = 1,
                     rowspan = 1,
                     sticky = N+W,
                     font = None,)
        self.english = self.addTextField(parent,
                          text = '',
                          row=0,
                          column=1,
                          rowspan = 1,
                          columnspan = 1,
                          width = 20,
                          sticky = N+E,
                          state = NORMAL)
        self.french = self.addTextField(parent,
                             text='',
                             row=1,
                             column=1,
                             columnspan = 1,
                             rowspan = 1,
                             width = 20,
                             sticky = N+E,
                             state = NORMAL)
    def apply(self):
        """Apply function"""
        if len(self.french.getText()) > 0 and len(self.english.getText()) > 0: 
            self.setModified()

def main():
    """Main function that calls the frame class and starts program"""
    mainWindow().mainloop()

if __name__ =='__main__':
    main()