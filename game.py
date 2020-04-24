import random
import libdw.sm as sm
#user has to install libdw (python -m pip install libdw)

class Guess_no(sm.SM):
    
    def __init__(self):
        self.start_state = 1
        self.codelst = [random.randrange(1,7) for i in range(4)]
        self.code = ''.join(map(str,self.codelst))
        self.playing = True
    
    def get_next_values(self, state, inp):
        guess = str(inp)
        code = self.code
        returnlst = [0,0]

        if inp == code:  
            self.playing = False
            return self.state,'You win! :)'
        
        for i in range(4):
            if guess[i] == code[i]:
                returnlst[0] += 1
                guess = f'{guess[:i]}{0}{guess[i+1:]}'
                code = f'{code[:i]}{0}{code[i+1:]}'

        for i in range(4):
            if guess[i] in code and guess[i] != '0':
                returnlst[1] += 1
                code = code.replace(guess[i],'0',1)
                guess = f'{guess[:i]}{0}{guess[i+1:]}'
                
        if returnlst == [0,0]:
            output = 'None correct, try again!'
        else:
            output = returnlst
            
        self.state += 1
        return self.state, output
    
    def run(self):
        self.start()
        print('Guess the 4-digit code')
        while self.playing:
            if self.state <= 10:
                inp = input(f'Attempt {self.state}:')
                if inp == 'master':
                    print(self.code)
                    continue
                output = self.step(inp)
                print(output)
            else:
                print(f'You have finished all guesses. Code is {self.code}')
                self.playing = False
        again = input('Play again? (y/n)')
        if again == 'y':
            g = Guess_no()
            g.run()
        else:
            print('Suit yourself.')

g = Guess_no()
g.run()
