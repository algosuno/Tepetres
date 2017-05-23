class Editor:
    def __init__(self,archivo):
        self.archivo=archivo
        self.t_act=self.archivo.tiempos.prim
        self.pos_t=0
        self.pila_t=Pila()

    def representar_cancion(self):
        for t in self.archivo.tiemposs:
            posicion=self.tiempos.index(t)
            if self.pos_t==posicion:
                print('>>',t.obtener_tiempo(),'<<', end='\t')
            else:
                print(t.obtener_tiempo(), end='\t')
        for x in range(len(t.obtener_nota())):
            print(x, end='\t')
            for t in self.tiempos:

                lista_notas=t.obtener_nota()
                nota=lista_notas[x]
                if nota: #La idea es que el usuario vea que notas estan activas
                    print('[X]', end='\t')
                else:
                    print('[ ]', end='\t')
#--------------------------------------------------------------------#
    def guardar(self,archivo):
        with open(archivo,'w') as plp:
            """Quedo medio raro, mas que nada la parte de los tiempos
            pero me parece que funciona"""
            plp.write('C,{}'.format(self.canales))
            for s in self.sonidos:
                tipo=s[0]
                frecuencia=[1]
                volumen=[2]
                plp.write('S,{}|{}|{}'.format(tipo,frecuencia,volumen))
            tiempo=0
            for t in self.tiempos:
                tiempo_nuevo=t.obtener_tiempo()
                if tiempo!=tiempo_nuevo:
                    plp.write('T,{}'.format(tiempo_nuevo))
                cadena=''
                for elem in t.obtener_nota:
                    if elem:
                        cadena+='#'
                    else:
                        cadena+='·'
                plp.write('N,{}',format(cadena))
                tiempo=tiempo_nuevo
        print('El archivo se ha guardado con el nombre ',archivo)
#--------------------------------------------------------------------#
    def avanzar(self,x=1):
        for iteracion in range(x):
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
            if t is self.t_act:
                t.agregar_nota(True)
                t.agregar_nota_obj(sonido_nuevo)
                continue
            t.agregar_nota(False)
        self.archivo.objeto_sonidos.append(sonido_nuevo)
#--------------------------------------------------------------------#
    def quitar_nota(self,pos):
        contador=0
        nota=self.archivo.objeto_sonidos.pop(pos)
        for t in self.archivo.tiempos:
            t.notas.pop(pos)
            t.notas_obj.remove(nota)
