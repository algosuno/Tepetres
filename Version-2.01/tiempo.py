from ListaEnlazada import ListaEnlazada
class Tiempo:
    def __init__(self,duracion):
        """Esto no es una documentacion, es solo un comentario sobre
        el funcionamiento. La idea es que cada objeto tiempo tenga
        como atributo, ademas de su duracion, una lista con los tiempos
        en forma de True y False (que sirver para representar la cancion)
        y una lista con los objetos a reproducir."""
        self.duracion=duracion
        self.notas=ListaEnlazada()
        self.notas_obj=ListaEnlazada()
#--------------------------------------------------------------------#
    def agregar_nota(self,nota,pos=False):
        if pos==len(self.notas):
            pos=False
        if pos:
            self.notas.insert(pos,nota)
            return
        self.notas.append(nota)
#--------------------------------------------------------------------#
    def quitar_nota(self,pos):
        self.notas.pop(pos)
#--------------------------------------------------------------------#
    def obtener_nota(self):
        #Hay que implementar la clase iterador para porder convertir
        # a la lista enlazada en una lista de python
        return list(self.notas)
#--------------------------------------------------------------------#
    def agregar_nota_obj(self,nota,pos=False):
        if pos:
            self.notas_obj.insert(pos,nota)
        self.notas_obj.append(nota)

    def quitar_nota_obj(self,pos):
        self.notas_obj.pop(pos)
#--------------------------------------------------------------------#
    def obtener_nota_obj(self):
        #Hay que implementar la clase iterador para porder convertir
        # a la lista enlazada en una lista de python
        return list(self.notas_obj)
#--------------------------------------------------------------------#
    def obtener_tiempo(self):
        return self.duracion
    def __str__(self):
        return 'Tiempo de duracion: {} segundos'.format(self.duracion)
    def index_notas(self,pos):
        return self.notas.devolver_posicion(pos)
