"""Two mini projects showing usefulness of classes. The airline project uses no inheritance.
If it did, it would be Airline has levels, and first, second and third class are levels.
The hotel project implements this as Hotel has room types and penthouse and standard are roomtypes"""


from abc import ABC, abstractmethod


class Airline:
    def __init__(self, levels):
        self.levels = levels
    
    def book(self,seat):
        Not_contained = 0
        for x in self.levels:
            if seat in x.seats.keys():
                x.book(seat)
            else:
                Not_contained += 1
        if Not_contained == len(self.levels):
            print("Not a valid seat")

    def show_seats(self,level):
        for x in self.levels:
            if level == x.name:
                x.show_seats()
        
    def make_available(self, seat):
        Not_contained = 0
        for x in self.levels:
            if seat in x.seats.keys():
                x.make_available(seat)
            else:
                Not_contained += 1
        if Not_contained == len(self.levels):
            print("Not a valid seat")

class Level:
    def __init__(self,name,seats,price):
        self.name = name
        self.seats = seats
        self.price = price
        
    def book(self, seat):
        if self.seats[seat]:
            print(f'Reserving seat {seat} for ${self.price}')
            self.seats[seat] = False
        else:
            print("Already reserved!")
            
    def show_seats(self):
        print(f"Available seats in {self.name}: ")
        for key in self.seats.keys():
            if self.seats[key] == True:
                print(key)
                
    def make_available(self,seat):
        if not self.seats[seat]:
            print(f'Seat {seat} now available!')
            self.seats[seat] = True
        else:
            print("Seat already available")


Jetblue = Airline([Level('First class', {'F1':True, 'F2':True, 'F3':True, 'F4':True, 'F5':True}, 120),
                   Level('Second class', {'S1':True, 'S2':True, 'S3':True, 'S4':True, 'S5':True}, 100),
                   Level('Coach', {'C1':True, 'C2':True, 'C3':True, 'C4':True, 'C5':True}, 80)])

Jetblue.show_seats('First class')
Jetblue.book('F1')
Jetblue.book('S4')
Jetblue.show_seats('Second class')
Jetblue.book('A5')
Jetblue.make_available('F1')



"""---------------------------------------------------------------"""





class Hotel:
    def __init__(self,rooms):
        self.rooms = rooms       
    def show_rooms(self,type_of_room):
        if type_of_room is Penthouse:
            print('Penthouse rooms available:')
        else:
            print('Standard rooms available:')
        for x in self.rooms:
            if isinstance(x,type_of_room):
                if x.state == True:
                    print(x.number)
    def reserve(self,room):
        for x in self.rooms:
            if room == x.number:
                x.reserve()
    def check_out(self,room):
        for x in self.rooms:
            if room == x.number:
                x.check_out()
            

class room_type(ABC):
    def __init__(self,number,state=True):
        self.number = number
        self.state = state
    @abstractmethod
    def reserve(self):
        pass
    @abstractmethod
    def check_out(self):
        pass

class Penthouse(room_type):
    price = 500
    def __init__(self, number):
        super().__init__(number)
    def check_out(self):
        self.state = True
        print(f'You have checked out of room {self.number}. Have a nice day!')
    def reserve(self):
        self.state = False
        print(f'You have reserved room {self.number} for ${self.price}')

class Standard(room_type):
    price = 150
    def __init__(self, number):
        super().__init__(number)
    def check_out(self):
        self.state = True
        print(f'You have checked out of room {self.number}. Have a nice day!')
    def reserve(self):
        self.state = False
        print(f'You have reserved room {self.number} for ${self.price}')
        
        
Hampton = Hotel([Penthouse('514'),Penthouse('515'),Penthouse('516'),Penthouse('517'),Penthouse('518'),
                Standard('120'),Standard('121'),Standard('122'),Standard('123'),Standard('124')])

Hampton.show_rooms(Standard)
Hampton.show_rooms(Penthouse)
Hampton.reserve('514')
Hampton.check_out('514')
Hampton.show_rooms(Penthouse)