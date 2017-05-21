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
    def agregar_nota(self,nota=None):
        self.notas.append(nota)
    def quitar_nota(self,pos=None):
        self.notas.pop(pos)
    def obtener_nota(self):
        #Hay que implementar la clase iterador para porder convertir
        # a la lista enlazada en una lista de python
        return list(self.notas)
    def agregar_nota_obj(self,nota):
        self.notas_obj.append(nota)
    def obtener_nota_obj(self):
        #Hay que implementar la clase iterador para porder convertir
        # a la lista enlazada en una lista de python
        return list(self.notas_obj)
    def obtener_tiempo(self):
        return self.duracion
