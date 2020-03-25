import random


class Message():
    
    def __init__(self, student, workedOn):
        
        self.student = student 
        self.name = self.student.getName()
        self.pronoun = self.student.getPronoun()
        print(type(self.pronoun))
        self.language = self.student.getLanguage()
        self.workedOn = workedOn
       
    def getIntroMessage(self, customMesg = None):
        
        pos = self.pronoun[1]
        print(type(pos))
        
        self.introMessage = [self.name + " continued to work on " + pos + " project today. ",
                        self.name +" worked more on "+ pos + " " + self.language + " lesson today. ",
                        self.name +" came in today and worked more on "+ pos + " game. "  ]
        
        if customMesg:
            return self.pronoun[1] + customMesg
        else:
            index = random.randint(0,len(self.introMessage)-1)
            return self.introMessage[index]
        
        
    def isFocusedMessage(self):
        self.focusedMessage = [self.pronoun[0] + " was pretty focused and on task during class. ",
                               self.pronoun[0]+ " was productive and focused. ",
                               self.pronoun[0] + " got a lot of work done and made a good progress. ",
                               ]
                            
        index = random.randint(0, len(self.focusedMessage) - 1)
        
        return self.focusedMessage[index]
        
        
        
    def getOutroMessage(self, customMesg = None):
        
        self.outroMessage = [" Next time " + self.pronoun[0] +" will worked on " + self.pronoun[1] +" coding project next time. ",
                             " Next time " + self.pronoun[0] +" will continue to make some progress on " + self.pronoun[1] +" javascript program. ",
                             " Next time " + self.pronoun[0] +" can continue to work on this project. ",
                             " Next time, " + self.pronoun[0] +" can continue to work on " + self.pronoun[1] +" lesson." ]
        
        self.work = self.pronoun[0] + " " + self.workedOn
        
        index = random.randint(0,len(self.introMessage)-1)
        
        return self.work + self.outroMessage[index]
          
    
        
        
      


# if __name__ == '__main__':
#     m = Message("him", 'javascript')
#     print(m.get())
    