class Pila:
    """Clase que almacena datos en forma de pila. El ultimo en guardarse
    es el primero en salir. Contiene los metodos apilar, desapilar, esta_vacia
    y ver_tope."""
    def __init__(self):
        """Contructor de la clase, inicializa la lista vacia que contendra
        los elementos de la pila."""
        self.lista=[]
    def apilar(self,x):
        """Permite apilar un elemento 'x' en la pila."""
        self.lista.append(x)
    def desapilar(self):
        """Permite desapilar el ultimo elemento que fue apilado."""
        if len(self.lista)==0:
            raise IndexError('La pila esta vacia')
        return self.lista.pop()
    def esta_vacia(self):
        """La funcion devuelve un booleano indicando si la pila se encuentra vacia"""
        return len(self.lista)==0
    def ver_tope(self):
        """Permite conocer el ultimo elemento que fue apilado sin dapilarlo."""
        if len(self.lista)==0:
            raise IndexError('La pila esta vacia')
        return self.lista[len(self.lista)-1]
