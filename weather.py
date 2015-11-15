from random import randint

class Weather:

    def stormy(self):
        print self.generator()
        if self.generator() <= 80:
            return False
        else:
            return True

    def generator(self):
        return randint(0,100)
