from Pila import Pila
from tiempo import Tiempo
class Editor:
    def __init__(self,archivo):
        self.archivo=archivo
        self.t_act=self.archivo.tiempos.prim
        self.pos_t=0
        self.pila=Pila()

    def representar_cancion(self):
        print('↓ Nro de track',end='\t\t\t\t\t')
        print('Tiempos (en segundos)')
        print(end='  ')
        for t in self.archivo.tiempos:
            posicion=self.archivo.tiempos.index(t)
            if self.pos_t==posicion:
                print('>'+str(t.obtener_tiempo())+'<', end=' ')
            else:
                print(t.obtener_tiempo(), end='  ')
        print()
        for x in range(len(t.obtener_nota())):
            print(x, end='  ')
            for t in self.archivo.tiempos:

                lista_notas=t.obtener_nota()
                nota=lista_notas[x]
                if nota: #La idea es que el usuario vea que notas estan activas
                    print('[X]', end='  ')
                else:
                    print('[ ]', end='  ')
            print()
#--------------------------------------------------------------------#
    def guardar(self,archivo):
        with open(archivo,'w') as plp:
            """Quedo medio raro, mas que nada la parte de los tiempos
            pero me parece que funciona"""
            plp.write('FIELD,DATA\n')
            plp.write('C,{}\n'.format(self.archivo.canales))
            for s in self.archivo.sonidos:
                tipo=s[0]
                frecuencia=[1]
                volumen=[2]
                plp.write('S,{}|{}|{}\n'.format(tipo,frecuencia,volumen))
            tiempo=0
            for t in self.archivo.tiempos:
                tiempo_nuevo=t.obtener_tiempo()
                if tiempo!=tiempo_nuevo:
                    plp.write('T,{}\n'.format(tiempo_nuevo))
                cadena=''
                for elem in t.obtener_nota():
                    if elem:
                        cadena+='#'
                    else:
                        cadena+='·'
                plp.write('N,{}\n'.format(cadena))
                tiempo=tiempo_nuevo
        print('El archivo se ha guardado con el nombre ',archivo)
#--------------------------------------------------------------------#
    def avanzar(self,x=1):
        for iteracion in range(int(x)):
            if self.t_act.prox is None:
                raise IndexError('Fuera de rango')
            dato=self.t_act
            self.t_act=self.t_act.prox
            self.pila.apilar(dato)
            self.pos_t+=1
            print(self.t_act)
#--------------------------------------------------------------------#
    def retroceder(self,x=1):
        for iteracion in range(int(x)):
            if self.t_act is None:
                raise IndexError('Fuera de rango')
            dato=self.t_act
            self.t_act=self.pila.desapilar()
            self.t_act.prox=dato
            self.pos_t-=1
#--------------------------------------------------------------------#
    def reproducir(self):
        self.archivo.reproducir()

    def reproducir_tiempos(self,cant_tiempos,segundos=False):
        if not cant_tiempos:
            cant_tiempos=20
            return
        lista_tiempos=[]
        tiempo=self.t_act
        for x in range(cant_tiempos):
            if tiempo is None:
                break
            lista_tiempos.append(tiempo.dato)
            tiempo=tiempo.prox
        self.archivo.reproducir_tiempos(lista_tiempos,segundos)
#--------------------------------------------------------------------#
    def agregar_nota(self,tipo,frequency,volume):
        sonido_nuevo=self.archivo.convertir_objeto([tipo,frequency,volume])
        print(sonido_nuevo)
        print(self.archivo.objeto_sonidos)
        for t in self.archivo.tiempos:
            if t is self.t_act.dato:
                t.agregar_nota(True)
                print(sonido_nuevo)
                t.agregar_nota_obj(sonido_nuevo)
                continue
            t.agregar_nota(False)
        self.archivo.objeto_sonidos.append(sonido_nuevo)
#--------------------------------------------------------------------#
    def quitar_nota(self,pos):
        contador=0
        print(self.archivo.objeto_sonidos)
        nota=self.archivo.objeto_sonidos.pop(pos)
        for t in self.archivo.tiempos:
            t.notas.pop(pos)
            if nota in t.obtener_nota_obj():
                t.notas_obj.remove(nota)
    def activar_nota(self,pos):
        dato=self.t_act.dato.index_notas(pos)
        if dato:
            raise ValueError('El track elegido ya esta activado')
        self.t_act.dato.quitar_nota(pos)
        self.t_act.dato.agregar_nota(True,pos)
        nota=self.archivo.objeto_sonidos.devolver_posicion(pos)
        self.t_act.dato.agregar_nota_obj(nota)
    def desactivar_nota(self,pos):
        dato=self.t_act.dato.index_notas(pos)
        if not dato:
            raise ValueError('El track elegido ya esta desactivado')
        self.t_act.dato.quitar_nota(pos)
        self.t_act.dato.agregar_nota(False,pos)
        nota=self.archivo.objeto_sonidos.devolver_posicion(pos)
        self.t_act.dato.notas_obj.remove(nota)

    def anadir_marca(self,duracion):
        tiempo=Tiempo(duracion)
        for iteracion in range(len(self.archivo.objeto_sonidos)):
            tiempo.agregar_nota(False)
        self.archivo.tiempos.append(tiempo)

    def anadir_marca_next(self,duracion):
        tiempo=Tiempo(duracion)
        for iteracion in range(len(self.archivo.objeto_sonidos)):
            tiempo.agregar_nota(False)
        posicion=self.archivo.tiempos.index(self.t_act.dato)+1
        self.archivo.tiempos.insert(posicion,tiempo)

    def anadir_marca_prev(self,duracion):
        tiempo=Tiempo(duracion)
        for iteracion in range(len(self.archivo.objeto_sonidos)):
            tiempo.agregar_nota(False)
        posicion=self.archivo.tiempos.index(self.t_act.dato)-1
        self.archivo.tiempos.insert(posicion,tiempo)
        nodo=self.archivo.tiempos.obtener_nodo(posicion)
        self.pila.apilar(nodo)
