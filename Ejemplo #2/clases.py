class funcionAritmetica:
    hola = "hola"
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        return self.a + self.b 

    def resta(self):
        return self.a - self.b

    def multiplicacion(self):
        return self.a * self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return 'No se puede dividir entre 0'
        
    def potencia(self):
        return self.a ** self.b
    
    def retornarA(self):
        return self.a
    
    def retornarB(self):
        return self.b
    
    def retornarHola(self):
        return self.hola

prueba = funcionAritmetica(5, 0)
print(prueba.suma()) # 7
print(prueba.resta()) # 3
print(prueba.multiplicacion()) # 10
print(prueba.division()) # 2.5
print(prueba.potencia()) # 25
print(prueba.retornarA()) # 5
print(prueba.retornarB()) # 2
print(prueba.retornarHola()) # hola