import random
class Bot:
    def __init__(self):
        self.message = 'Hi, I\'m Bobert McGee! How may I be of assistance?'
        self.greetings = ['Hey, what\'s up?','How are you doing?', 'Hi! What\'s up?',
                          'Greetings! How do you do?', 'Hola! Como estas?']
        self.repeated_greet = ['...Hi? Are you okay?', '...yes...hi...how are you?','Um...hi, again. How are you?',
                               'Yes, hello, how are you?', 'Okay, you just said hi to me multiple times, you good?']
        self.confused = ['I\'m sorry, what was that again?', 'I missed you, can you repeat?',
                         '...Umm... can you say that again?']
        self.running = True
        while self.running:
            user_answer = input(self.message+'\n')
            self.reply(user_answer)

    def reply(self, answer):
        hello = ['hi', 'hello','good morning',
                 'good afternoon','hola', 'buenos dias', 'buenas tardes']
        bye = ['bye', 'good-bye', 'goodbye', 'good bye',
                 'good night', 'adios', 'chao']
        is_first_greet = self.message not in self.greetings and self.message not in self.repeated_greet
        if answer.lower() in bye:
            self.message = 'Good-bye!'
            print(self.message)
            self.running = False
        elif len(answer) == 0:
            index = random.randint(0,len(self.confused)-1)
            self.message = self.confused[index]
        elif is_first_greet:
            if answer.lower() in hello:
                index = random.randint(0,len(self.greetings)-1)
                self.message = self.greetings[index]
        elif self.message in self.greetings or self.message in self.repeated_greet:
            if answer.lower() in hello:
                index = random.randint(0,len(self.repeated_greet)-1)
                self.message = self.repeated_greet[index]
        else:
            pass
            
        

Bot()
