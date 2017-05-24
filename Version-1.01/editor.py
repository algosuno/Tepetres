from Pila import Pila
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
#--------------------------------------------------------------------#
    def retroceder(self,x=1):
        for iteracion in range(x):
            if self.t_act is None:
                raise IndexError('Fuera de rango')
            dato=self.t_act
            self.t_act=self.pila.desapilar()
            self.t_act.prox=dato
            self.pos_t-=1
#--------------------------------------------------------------------#
    def reproducir(self,seg=False,lim_tiempos=False):
        self.archivo.reproducir()
#--------------------------------------------------------------------#
    def agregar_nota(self,tipo,frequency,volume):
        sonido_nuevo=self.archivo.convertir_objeto([tipo,frequency,volume])
        for t in self.archivo.tiempos:
            if t is self.t_act.dato:
                t.agregar_nota(True)
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
