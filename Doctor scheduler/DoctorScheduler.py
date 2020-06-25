class Doctor:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        
    def schedule(self,time,patient):
        if self.hours[time] == None:
            self.hours[time] = patient
            print(f'{patient.name} scheduled for {time}pm!')
        else:
            print("This time already booked")
            
    def clear_hours(self, *slots):
        for hour in slots:
            self.hours[hour] = None
            print(f'{hour}pm cleared on your schedule')
        
    def show_sched(self):
        
        for item in self.hours.keys():
            if self.hours[item]:
                print(f'{item}pm you have {self.hours[item].name} with {self.hours[item].problem}')
                
                


class Patient:
    def __init__(self, name, problem):
        self.name = name
        self.problem = problem
        
    def change_problem(self,problem):
        self.problem = problem
        

king = Doctor("Dr King", {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None})

john = Patient("John James", "Corona")
Mark = Patient("Mark Olson", "Plague")
Jake = Patient("Jake J", "Leg broken")

king.schedule(1,john)
king.schedule(2,Mark)
king.schedule(4,Jake)
Mark.change_problem("Flu")

king.show_sched()

king.clear_hours(1,2,4)
king.show_sched()


