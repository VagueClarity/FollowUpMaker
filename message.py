import random


class Message():
    
    def __init__(self, pronoun, language):
        
        self.pronoun = pronoun
        self.language = language
        self.introMessage = [" continued to work on " + self.pronoun + " project today.",
                        " worked more on "+ self.pronoun + " " + self.language + " lesson today.",
                        " came in today and worked more on "+ self.pronoun + " game."  ]
          
          
    def getMessage(self):
        
        index = random.randint(0,len(self.introMessage)-1)
        
        return self.introMessage[index]
    


if __name__ == '__main__':
    m = Message("him", 'javascript')
    print(m.getMessage())
    