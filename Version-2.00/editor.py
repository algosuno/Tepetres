from Pila import Pila

#---------------------------------------------------------------------#

class Editor:
    '''Clase que modifica los objetos archivo. Tiene los atributos archivo, t_act,
    pos_t, pila. Posee los metodos representar_cancion, guardar, avanzar, retroceder,
    reproducir, reproducir_tiempos, agregar_nota, quitar_nota.'''
    
#--------------------------------------------------------------------#

    def __init__(self,archivo):
        '''Toma como parametro un archivo y crea la instancia inicial de la clase 
        Editor con sus respectivos atributos''''
        self.archivo=archivo
        self.t_act=self.archivo.tiempos.prim
        self.pos_t=0
        self.pila=Pila()
        
#---------------------------------------------------------------------#

    def representar_cancion(self):
        '''Representa el archivo .plp con el cual esta trabajando en la consola.'''
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
                if nota:        #La idea es que el usuario vea que notas estan activas
                    print('[X]', end='  ')
                else:
                    print('[ ]', end='  ')
            print()
            
#--------------------------------------------------------------------#

    def guardar(self,archivo):
        '''Abre un archivo en modo escritura y escribe la cancion que desea guardar
        el usuario'''
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
            tiempo=0 #pareciera que va bien esta parte
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
        '''Toma como parametro un numero 'x' y avanza 'x' marcas de tiempo 
        respecto a la posicion actual. En caso que no halla una marca siguiente 
        a la actual levanta un IndexError.
        Pre: x debe ser un numero int'''
        for iteracion in range(int(x)):
            if self.t_act.prox is None:
                raise IndexError('Fuera de rango') #aca no se romperia el programa y sale?
            dato=self.t_act
            self.t_act=self.t_act.prox
            self.pila.apilar(dato)
            self.pos_t+=1
            
#--------------------------------------------------------------------#
    
    def retroceder(self,x=1):
        '''Toma como parametro un numero 'x' y retrocede 'x' marcas de tiempo 
        respecto a la posicion actual. En caso que no halla una marca anterior 
        a la actual levanta un IndexError.
        Pre: x debe ser un numero int'''
        for iteracion in range(x):
            if self.t_act is None:
                raise IndexError('Fuera de rango')
            dato=self.t_act
            self.t_act=self.pila.desapilar()
            self.t_act.prox=dato
            self.pos_t-=1
#--------------------------------------------------------------------#

    def reproducir(self):
        '''Reproduce el archivo actual en edicion'''
        self.archivo.reproducir()
        
#---------------------------------------------------------------------#

    def reproducir_tiempos(self,cant_tiempos,segundos=False): #no seria cant_tiempos=False?(lo digo por que se parece a la funcion del reproductor)
        '''Toma como parametro una cant_tiempo que representa los tiempos que
        se desea reproducir y/o los segundos y los reproduce.
        Pre: ¿?¿?¿''' #por ahora no se me ocurrio pero por losparametro que toma deberia haber una pre
        if not cant_tiempos:
            self.archivo.reproducir_tiempos(False,segundos)
            return
        lista_tiempos=[]
        tiempo=self.t_act
        for x in range(cant_tiempos):
            lista_tiempos.append(tiempo.dato)
            tiempo=tiempo.prox
        self.archivo.reproducir_tiempos(lista_tiempos,segundos)
        
#--------------------------------------------------------------------#
  
    def agregar_nota(self,tipo,frequency,volume):
        '''Toma como parametro un tipo de onda, una frequencia y un volumen
        para crear un nuevo sonido y agregar una nueva nota. Modifica el
        objeto_sonido.'''
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
        '''Toma como parametro una posicion y quita la nota en dicha posicion.
        Pre: pos debe ser un numero int'''
        contador=0
        print(self.archivo.objeto_sonidos)
        nota=self.archivo.objeto_sonidos.pop(pos)
        for t in self.archivo.tiempos:
            t.notas.pop(pos)
            if nota in t.obtener_nota_obj():
                t.notas_obj.remove(nota)
                
#--------------------------------------------------------------------#
    
    def agregar_tiempo(self,duracion,pos):


#--------------------------------------------------------------------#




