class _Nodo:
    def __init__(self,dato=None,prox=None):
        self.dato=dato
        self.prox=prox
    def __str__(self):
        return str(self.dato)

#--------------------------------------------------------------
    
class ListaEnlazada:
    def __init__(self):
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
                nodo_anterior=nodo_siguiente
                nodo_actual=nodo_anterior.prox
            dato=nodo_actual.dato
            nodo_anterior.prox=nodo_actual.prox
        self.len -=1
        return dato
    def remove(self,x):
        if self.len==0:
            raise ValueError('Lista vacia')
        if self.prim.dato==x:
            self.prim=self.prim.prox
        else:
            nodo_anterior=self.prim
            nodo_actual=nodo_anterior.prox
            while nodo_actual is not None and nodo_actual.dato!=x:
                nodo_anterior=nodo_actual
                nodo_actual=nodo_anterior.prox
            if nodo_actual==None:
                raise ValueError('El elemento no esta en la lista')
            nodo_anterior.prox=nodo_actual.prox
        self.len-=1

    def insert(self,i,x):
        if i<0 or i>= self.len:
            raise IndexError('Indice fuera de rango')
        nuevo= _Nodo(x)
        if i==0:
            nuevo.prox=self.prim
            self.prim=nuevo
        else:
            nodo_anterior=self.prim
            for posicion in range(1,i):
                nodo_anterior=nodo_anterior.prox
            nuevo.prox=nodo_anterior.prox
            nodo_anterior.prox=nuevo
        self.len+=1
    def append(self,x):
        nuevo= _Nodo(x)
        
        if self.len==0:
            self.prim=nuevo
        else:
            nodo_anterior=self.prim
            nodo_actual=nodo_anterior.prox
            while nodo_actual is not None:
                nodo_anterior=nodo_actual
                nodo_actual=nodo_anterior.prox
            nodo_anterior.prox=nuevo
        self.len+=1
    def index(self,x):
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

#-----------------------------------------------------------------------

class _IteradorListaEnlazada:
    def __init__(self,prim):
        self.actual=prim
    def __next__(self):
        if self.actual is None:
            raise StopIteration()
        dato=self.actual.dato
        self.actual=self.actual.prox
        return dato
        
    