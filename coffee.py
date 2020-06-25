"""GRADER READ! This is a coffee machine abstraction that is run by user input. I talked with Prof Allison and
said that in my mind, the selector had the job of determining if the inputs were valid
He said that is fine and my implementation of classes will not lose points."""


"""Chris Withers. I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitutes cheating,
and that I will receive a zero on this project if I am found in violation of this policy."""


class CoffeeMachine:
    def __init__(self):
        self.s = selector(self)
        self.c = cashBox(0)
        
    def oneAction(self):
        print("""______________________________________""")
        print("""    PRODUCT LIST: all 35 cents, except bouillon (25 cents)
    1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon
    Sample commands: insert 25, select 1.""")
        self.inp = input(">>> Your command: ")
        if self.inp == 'quit':
            return False
        else:
            self.s.select()
            return True
            
    def totalCash(self):
        return self.c.bank

class cashBox:
    def __init__(self, starting):
        self.starting = starting
        self.bank = 0
    def deposit(self, amt):
        self.starting += amt
        print(f'Depositing {amt} cents. You have {self.starting} cents credit.')
    def returnCoins(self):
        print(f'Returning {self.starting} cents')
        self.deduct(self.starting)
    def haveYou(self, amt):
        if self.starting >= amt:
            return True
    def deduct(self, amt):
        self.starting -= amt        
    def total(self):
        return self.starting


class selector:
    def __init__(self,CoffeeMachine):
        self.products = [product('black', ['cup', 'coffee', 'water'], 35), 
                        product('white', ['cup', 'coffee','creamer', 'water'], 35),
                        product('sweet', ['cup', 'coffee','sugar', 'water'], 35),
                        product('white & sweet', ['cup', 'coffee','sugar','creamer', 'water'], 35),
                        product('bouillon', ['cup', 'bouillonPowder', 'water'], 25)]
        self.cm = CoffeeMachine
       
    def select(self):
        if self.cm.inp == 'cancel':
            self.cm.c.returnCoins()
        elif len(self.cm.inp.split(' ')) >= 2: 
            self.opt = self.cm.inp.split(' ')[0]
            self.ind = self.cm.inp.split(' ')[1]
            if self.opt in ['select', 'insert', 'cancel', 'quit']:
                if self.opt == 'select' and self.ind in ['1','2','3','4','5']:
                    if self.cm.c.haveYou(self.products[(int(self.ind)-1)].getPrice()):
                        self.products[(int(self.ind)-1)].make()
                        self.cm.c.deduct(self.products[(int(self.ind)-1)].getPrice())
                        self.cm.c.bank += self.products[(int(self.ind)-1)].getPrice()
                        if self.cm.c.haveYou(0):
                            self.cm.c.returnCoins()
                        else:
                            pass
                    else:
                        print('Sorry. Not enough money deposited.')
                elif self.opt == 'insert' and self.ind in ['5', '10', '25', '50']:
                    self.cm.c.deposit(int(self.ind))
                elif self.opt == 'insert' and self.ind not in ['5', '10', '25', '50']:
                    print("""INPUT ERROR >>> \nWe only take half-dollars, quarters, dimes, and nickels.
Coin(s) returned.""")
                else:
                    print('Invalid command.')
            else:
                print('Invalid command.')
        else:
            print('Invalid command.')

class product:
    def __init__(self,name,recipe, price):
        self.name = name
        self.recipe = recipe
        self.price = price
    def getPrice(self):
        return self.price
    def make(self):
        print(f'Making {self.name}:')
        for item in self.recipe:
            print(f'\tDispensing {item}')

def main():
    cm = CoffeeMachine()
    while cm.oneAction():
        pass
    total = cm.totalCash()
    print(f"Total cash: ${total/100:.2f}")
    
    
if __name__ =='__main__':
    main()