from Pila import Pila
class _Nodo:
    """Clase que almacena datos en nodos, los cuales solo contienen
    una referencia al nodo siguiente."""
    def __init__(self,dato=None,prox=None):
        """Constructor de la clase. Inicializa el nodo con su dato y su
        refencia al siguiente. Estos atributos pueden no pasarse como
        parametro."""
        self.dato=dato
        self.prox=prox

    def __str__(self):
        return str(self.dato)
    def __repr__(self):
        return str(self.dato)

#--------------------------------------------------------------

class ListaEnlazada:
    """Clase que enlaza los nodos. Contiene los metodos index, insert,
    append, remove, pop y devolver_posicion."""
    def __init__(self):
        """Constructor de la clase, inicializa la lista vacia."""
        self.prim=None
        self.len=0

    def __str__(self):
        lista=[]
        nodo_actual=self.prim
        while nodo_actual is not None:
            lista.append(nodo_actual.dato)
            nodo_actual=nodo_actual.prox

        return str(lista)

    def __len__(self):
        return self.len

    def pop(self,i=None):
        """El metodo elimina el elemento en la posicion 'i' de la lista.
        Pre:
            i (int): Debe ser un numero entero."""
        if i==None:
            i= self.len-1
        if i<0 or i>=self.len:
            raise IndexError('Indice fuera de rango')
        if i==0:
            dato=self.prim.dato
            self.prim=self.prim.prox
        else:
            nodo_anterior=self.prim
            nodo_actual=nodo_anterior.prox
            for posicion in range(1,i):
                nodo_anterior=nodo_actual
                nodo_actual=nodo_anterior.prox
            dato=nodo_actual.dato
            nodo_anterior.prox=nodo_actual.prox
        self.len -=1
        return dato

    def remove(self,x):
        """El metodo busca en la lista el elemento 'x' dado como parametro y,
        en caso de encontrarlo, lo elimina."""
        if self.len==0:
            raise ValueError('Lista vacia')
        pos=self.index(x)
        self.pop(pos)

    def insert(self,i,x):
        """El metodo inserta en la posicion 'i' el elemento 'x', ambos pasados
        como parameto.
        Pre:
            i (int): Debe ser un numero entero."""
        if i<0 or i>= self.len:
            raise IndexError('Indice fuera de rango')
        nuevo= _Nodo(x)
        if i==0:
            nuevo.prox=self.prim
            self.prim=nuevo
            self.act=self.prim
        else:
            nodo_anterior=self.prim
            for posicion in range(1,i):
                nodo_anterior=nodo_anterior.prox
            nuevo.prox=nodo_anterior.prox
            nodo_anterior.prox=nuevo
        self.len+=1

    def append(self,x):
        """El metodo inserta un elemento 'x' al final de la lista."""
        nuevo= _Nodo(x)

        if self.len==0:
            self.prim=nuevo
            self.act=self.prim
        else:
            nodo_anterior=self.prim
            nodo_actual=nodo_anterior.prox
            while nodo_actual is not None:
                nodo_anterior=nodo_actual
                nodo_actual=nodo_anterior.prox
            nodo_anterior.prox=nuevo
        self.len+=1

    def index(self,x):
        """El metodo busca el elemento 'x' dado como parametro y devuelve su
        posicion en la lista."""
        if self.len==0:
            raise ValueError('Lista vacia')
        if self.prim==x:
            posicion=0
        else:
            posicion=0
            nodo_actual=self.prim
            while nodo_actual is not None and nodo_actual.dato!=x:
                nodo_actual=nodo_actual.prox
                posicion+=1
            if nodo_actual is None:
                raise ValueError('El valor no esta en la lista')
        return posicion

    def __iter__(self):
        return _IteradorListaEnlazada(self.prim)

    def devolver_posicion(self,i=None):
        """El metodo devuelve el elemento que se encuenta en la posicion 'i'
        dentro de la lista.
        Pre:
            i (int): Debe ser un numero entero."""
        if i<0 or i>=self.len:
            raise IndexError('Indice fuera de rango')
        if i==0:
            dato=self.prim.dato
        else:
            nodo_anterior=self.prim
            nodo_actual=nodo_anterior.prox
            for posicion in range(1,i):
                nodo_anterior=nodo_actual
                nodo_actual=nodo_anterior.prox
            dato=nodo_actual.dato
        return dato

        def __len__(self):
            return self.len


#-----------------------------------------------------------------------

class _IteradorListaEnlazada:
    """Clase que itera sobre la lista enlazada. Contiene los metodos next,
    prev, insertar_marca_despues e insertar_marca_antes."""
    def __init__(self,prim):
        self.actual=prim
        self.pila=Pila()
    def __next__(self):
        if self.actual is None:
            raise StopIteration()
        dato=self.actual.dato
        self.actual=self.actual.prox
        return dato
    def next(self):
        """El metodo devuleve el dato sobre el cual se encuenta y actualiza su
        posicion al siguiente nodo."""
        if self.actual is None:
            raise StopIteration()
        dato=self.actual.dato
        self.pila.apilar(self.actual)
        self.actual=self.actual.prox
        return dato
    def prev(self):
        if self.pila.esta_vacia():
            raise ValueError
        self.actual=self.pila.desapilar()
        return self.pila.ver_tope().dato
    def insertar_elem_despues(self,elem):
        """Dado un elemento 'elem' pasado por parametro, el metodo crea un nodo
        conteniendolo y lo inserta en la posicion actual del iterador."""
        nodo=_Nodo(elem)
        nodo.prox=self.actual
        self.actual=nodo
        self.pila.ver_tope().prox=self.actual
    def insertar_elem_antes(self,elem):
        """Dado un elemento 'elem' pasado por parametro, el metodo crea un nodo
        conteniendolo y lo inserta justo antes de la posicion actual del iterador"""
        dato=self.pila.desapilar()
        nodo=_Nodo(elem)
        nodo.prox=dato
        self.pila.apilar(nodo)
        self.pila.apilar(dato)
