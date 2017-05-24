class Pila:
    def __init__(self):
        self.lista=[]
    def apilar(self,x):
        self.lista.append(x)
    def desapilar(self):
        if len(self.lista)==0:
            raise IndexError('La pila esta vacia')
        return self.lista.pop()
    def esta_vacia(self):
        return len(self.lista)==0
