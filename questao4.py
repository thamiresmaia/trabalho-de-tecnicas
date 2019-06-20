class carros(object):
    def __init__(self,km):
       self.a = km
       self.b = 0
       self.c = 0
    def adicionar(self,g):
        self.b += g
    def andar(self,an):
        self.c = an
    def obterGasolina(self):
        if((self.c/self.a)<=self.b):
            return round(self.b-(self.c/self.a),2)
        else:
            return 0
pass
