from ListaEnlazada import ListaEnlazada


class MarcaTiempo:
    """Clase que representa una marca de tiempo de una cancion. Contiene
    los atributos agregar_nota, quitar_nota, obtener_notas, index_notas y
    obtener_tiempo."""
    def __init__(self,duracion):
        """Constructor de la clase, inicializa una lista de notas y la duracion
        de la marca de tiempo."""
        self.duracion=duracion
        self.estado_notas=ListaEnlazada()
#-----------------MANEJO DE NOTAS EN FORMATO DE BOOLEANOS----------------#

    def cambiar_estado(self,pos,nuevo_estado):
        """El metodo toma como parametro una posicion (int) y un nuevo_estado
        (bool) para esa posicion. El metodo cambia el estado de esa posicion,
        por el dado como parametro."""
        estado_actual=self.estado_notas.devolver_posicion(pos)
        if estado_actual==nuevo_estado:
            raise ValueError
        self.estado_notas.pop(pos)
        self.estado_notas.insert(pos,nuevo_estado)

    def agregar_estado(self,estado,pos=-1):
        """El metodo toma como parametro una booleano y la agrega a la lista
        de booleanos del objeto MarcaTiempo.
        Pre: nota (bool) debe ser un booleano que indique con 'True' si
        la nota suena o 'False' en caso contrario."""
        if pos==-1 or pos==len(self.estado_notas):
            self.estado_notas.append(estado)
            return
        self.estado_notas.insert(pos,estado)


    def quitar_estado(self,pos):
        """El metodo toma como parametro una posicion. Quita la nota de la
        la lista de notas del objeto tiempo ubicada en esa posicion.
        Pre:
            pos (int): debe ser un entero indicando la posicion de la nota."""
        self.estado_notas.pop(pos)

    def obtener_lista_estados(self):
        """El metodo devuelve una lista de notas.
        Post:
            La lista devuelta contiene booleanos indicando si la nota
            correspondienta suena o no."""
        return list(self.estado_notas)

    def devolver_estado(self,pos):
        """El metodo devuelve la nota que se encuentre en la posicion
        dada como parametro. No elimina la nota de la lista.
        Post:
            La nota devuelta sera un booleano (bool)"""
        return self.estado_notas.devolver_posicion(pos)


    def obtener_tiempo(self):
        """El metodo devuelve la duracion de la marca de tiempo."""
        return self.duracion

    def __str__(self):
        return 'Tiempo de duracion: {}'.format(self.duracion)

    def __repr__(self):
        return 'MarcaTiempo({})'.format(self.duracion)
