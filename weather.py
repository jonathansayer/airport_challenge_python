from random import randint

class Weather:

    def stormy(self):
        generator = randint(0,100)
        if generator < 80:
            return False
        
