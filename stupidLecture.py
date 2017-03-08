class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def lecture(self, stuff): 
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)

        
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

print '1' + e.say('the sky is blue')
print '2' + le.say('the sky is blue')
print '2' + le.lecture('the sky is blue')
print '3' + pe.say('the sky is blue')
print '3' + pe.lecture('the sky is blue')
print '4' + ae.say('the sky is blue')
print '4' + ae.lecture('the sky is blue')