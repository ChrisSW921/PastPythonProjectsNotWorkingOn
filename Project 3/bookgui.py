import bookrecs as books
from breezypythongui import *
"""Chris Withers. I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitutes cheating,
and that I will receive a zero on this project if I am found in violation of this policy."""
    
class firstWindow(EasyFrame):
    """Sets up first window"""
    def __init__(self):
        EasyFrame.__init__(self,title='Book Recommendations')
        self.setBackground("sky blue")
        self.button1 = self.addButton(text="Friends", row=0, column=0, rowspan = 1, columnspan = 1, command = self.friends_button)
        self.button2 = self.addButton(text="Recommend", row=0, column=1, rowspan = 1, columnspan = 1, command = self.recommend_button)
        self.button3 = self.addButton(text="Report", row=0, column=2, rowspan = 1, columnspan = 1, command = self.reportResponse)
        
    def friends_button(self):
        """Calls my friends class and checks if its modified. If it is, then it makes message box"""
        f = friendsResponse(self, "Friends")
        if f.modified():
            self.returned_friends = ""
            self.friends_in_list = books.friends(f.friendly.getText(), f.numbers.getNumber())
            for friend in self.friends_in_list:
                self.returned_friends += friend + '\n'
            self.messageBox('Friends of ' + f.friendly.getText(), self.returned_friends,
                                width = 50)
    def recommend_button(self):
        """Calls my recommend class and checks if its modified. If it is, then it makes message box"""
        r = recommendResponse(self, 'Recommendations')
        if r.modified():
            self.returned_recs = ""
            self.returned_in_list = books.recommend(r.friendly.getText(), r.numbers.getNumber())
            for rec in self.returned_in_list:
                self.returned_recs += ', '.join(rec) + '\n'
            self.messageBox('Recommendations for ' + r.friendly.getText(),
                                self.returned_recs, width=75)       

    def reportResponse(self):
        """Displays my report"""
        self.messageBox("Report", books.report(), width = 100, height = 10)
       
class friendsResponse(EasyDialog):
    """All functions relating to friends"""
    def __init__(self, parent, title):
        EasyDialog.__init__(self, parent, title)
 
    def body(self, parent):
        """Body function"""
        self.addLabel(parent,
                     text="Reader:", row=0, column=0,
                     columnspan = 1,
                     rowspan = 1,
                     sticky = N+W,
                     font = None,)
        self.addLabel(parent,
                     text="# of Friends:", row=1, column=0,
                     columnspan = 1,
                     rowspan = 1,
                     sticky = N+W,
                     font = None,)
        self.friendly = self.addTextField(parent,
                          text = '',
                          row=0,
                          column=1,
                          rowspan = 1,
                          columnspan = 1,
                          width = 20,
                          sticky = N+E,
                          state = NORMAL)
        self.numbers = self.addIntegerField(parent,
                             value=2,
                             row=1,
                             column=1,
                             columnspan = 1,
                             rowspan = 1,
                             width = 20,
                             sticky = N+E,
                             state = NORMAL)
    def apply(self):
        """Apply function"""
        try:
            books.friends(self.friendly.get(), self.numbers.getNumber())
            if self.numbers.getNumber() < 1:
                self.messageBox('Error ', "Invalid number. Must be between 1 and 84",
                            width = 50)
            else:
                self.setModified()
        except:
            try:
                books.friends(self.friendly.get())
                if self.numbers.getNumber() >= 85 or self.numbers.getNumber() < 1:
                    self.messageBox('Error' ,"Invalid number. Must be between 1 and 84",
                            width = 50)
            except:
                if self.numbers.getNumber() >= 85 or self.numbers.getNumber() < 1:
                    
                    self.messageBox('Error' ,"No such reader and invalid number. Must be between 1 and 84",
                                    width = 50)
                else:
                    self.messageBox('Error' ,"No such reader.",
                                    width = 50)
               
                
class recommendResponse(EasyDialog):
    """All functions relating to recommend."""
    def __init__(self, parent, title):
        EasyDialog.__init__(self, parent, title)
 
    def body(self, parent):
        """Body function"""
        self.addLabel(parent,
                     text="Reader:", row=0, column=0,
                     columnspan = 1,
                     rowspan = 1,
                     sticky = N+W,
                     font = None,)
        self.addLabel(parent,
                     text="# of Friends:", row=1, column=0,
                     columnspan = 1,
                     rowspan = 1,
                     sticky = N+W,
                     font = None,)
        self.friendly = self.addTextField(parent,
                          text = '',
                          row=0,
                          column=1,
                          rowspan = 1,
                          columnspan = 1,
                          width = 20,
                          sticky = N+E,
                          state = NORMAL)
        self.numbers = self.addIntegerField(parent,
                             value=2,
                             row=1,
                             column=1,
                             columnspan = 1,
                             rowspan = 1,
                             width = 20,
                             sticky = N+E,
                             state = NORMAL)
        
    def apply(self):
        """Apply function"""
        try:
            books.recommend(self.friendly.get(), self.numbers.getNumber())
            if self.numbers.getNumber() < 1:
                self.messageBox('Error ', "Invalid number. Must be between 1 and 84",
                            width = 50)
            else:
                self.setModified()
        except:
            try:
                books.recommend(self.friendly.get())
                if self.numbers.getNumber() >= 85 or self.numbers.getNumber() < 1:
                    self.messageBox('Error' ,"Invalid number. Must be between 1 and 84",
                            width = 50)
            except:
                if self.numbers.getNumber() >= 85 or self.numbers.getNumber() < 1:
                    
                    self.messageBox('Error' ,"No such reader and invalid number. Must be between 1 and 84",
                                    width = 50)
                else:
                    self.messageBox('Error' ,"No such reader.",
                                    width = 50)
    
        
    
def main():
    """Main function that calls the frame class and starts program"""
    firstWindow().mainloop()

if __name__ =='__main__':
    main()



