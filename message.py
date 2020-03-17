import random


class Message():
    
    def __init__(self, student):
        
        self.student = student 
        self.name = self.student.getName()
        self.pronoun = self.student.getPronoun()
        self.language = self.student.getLanguage()
       
    def getIntroMessage(self, customMesg = None):
        
        self.introMessage = [" continued to work on " + self.pronoun + " project today.",
                        " worked more on "+ self.pronoun + " " + self.language + " lesson today.",
                        " came in today and worked more on "+ self.pronoun + " game."  ]
        
        if customMesg:
            return self.pronoun + customMesg
        else:
            index = random.randint(0,len(self.introMessage)-1)
            return self.pronoun + self.introMessage[index]
        
        
    def isFocusedMessage(self):
        self.focusedMessage = ["he was pretty focused and on task during class. ",
                                 "he was productive and focused "]
        
        
        
        
    def getOutroMessage(self, customMesg = None):
        
        self.outroMessage = ["Next time " + self.pronoun +" will worked on " + self.pronoun +" coding project next time.",
                             "Next time " + self.pronoun +" continues to make some progress on " + self.pronoun +" javascript program",
                             "Next time " + self.pronoun +" can continue to work on this project",
                             "Next time, " + self.pronoun +" can continue to work on " + self.pronoun +" lesson." ]
        
        index = random.randint(0,len(self.introMessage)-1)
        
        return self.outroMessage[index]
          
    
        
        
      


# if __name__ == '__main__':
#     m = Message("him", 'javascript')
#     print(m.get())
    