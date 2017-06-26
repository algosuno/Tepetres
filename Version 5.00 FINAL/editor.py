import soundPlayer as pysounds
from ListaEnlazada import ListaEnlazada
from marca_tiempo import MarcaTiempo
from Pila import Pila

LETRA_CANALES='C'
LETRA_SONIDOS='S'
LETRA_MARCAS='T'
LETRA_NOTAS='N'
NOTA_ACTIVADA='#'
NOTA_DESACTIVADA='·'
SONIDO_ACTIVADO='[X]'
SONIDO_DESACTIVADO='[ ]'
SEPADADOR_PARAMETROS=','
SEPARADOR_PARAM_SONIDOS='|'
CABECERA_ARCHIVO='FIELD,DATA'
ONDA_SQUARE='SQ'
ONDA_TRIA='TR'
ONDA_SINE='SI'
ONDA_NOISE='NO'


class Editor:
    '''Clase que modifica los objetos archivo. Tiene los atributos archivo, t_act,
    pos_t, pila. Posee los metodos representar_cancion, guardar, avanzar, retroceder,
    reproducir, agregar_nota, quitar_nota.'''
    def __init__(self,archivo):
        '''Toma como parametro un nombre de archivo y crea la instancia inicial
        de la clase Editor con sus respectivos atributos'''
        self.archivo=archivo
        self.tiempos=ListaEnlazada()
        self.sonidos_str=[] #Esta variable guarda los parametros del sonidos
                            #en forma de cadena para poder guardar el archivo.
        self.sonidos=ListaEnlazada()
        self.leer()
        self._conversion_a_sonido()
        self.iterador=iter(self.tiempos)

#-----------------------ABRIR E INICIALIZAR CANCION------------------------#

    def leer(self):
        '''El metodo abre el archivo que tiene como atributo el objeto editor.
        Lee y guarda los datos del archivo en los atributos correspondientes.'''
        with open(self.archivo) as plp:
            linea=plp.readline()
            linea=linea.rstrip('\n').split(',')
            while len(linea)>1:

                if linea[0].upper()==LETRA_SONIDOS:
                    parametros_sonido=linea[1].split(SEPARADOR_PARAM_SONIDOS)
                    self.sonidos_str.append(parametros_sonido)

                if linea[0].upper()==LETRA_MARCAS:
                    duracion=float(linea[1])
                    linea=plp.readline()
                    linea=linea.rstrip('\n').split(',')
                    while linea[0].upper()==LETRA_NOTAS:
                        t=MarcaTiempo(duracion)
                        for c in linea[1]:
                            t.agregar_estado(c==NOTA_ACTIVADA)
                        self.tiempos.append(t)
                        linea=plp.readline()
                        linea=linea.rstrip('\n').split(',')
                    continue
                linea=plp.readline()
                linea=linea.rstrip('\n').split(',')

    def _conversion_a_sonido(self):
        '''El metodo llama al metodo "convertir_a_objeto_sonido" para cada uno de los
        sonidos obtenidos del archivo a editar.'''
        sonidos=self.sonidos_str[:]
        for s in sonidos:
            self.sonidos.append(self.convertir_a_objeto_sonido(s))

#--------------------------REPRESENTAR Y GUARDAR-------------------------#
    def representar_cancion(self):
        '''Representa por consola la cancion en edicion, mostrando las marcas
        de tiempo con sus respectivos tracks y el estado en que se encuentran.'''
        print('↓ Nro de track',end='\t\t\t\t\t')
        print('Tiempos (en segundos)')
        print(end='  ')
        marca_actual=self.iterador.actual()
        for t in self.tiempos:
            if t is marca_actual:
                print('>'+str(t.obtener_tiempo())+'<', end=' ')
            else:
                print(t.obtener_tiempo(), end='  ')
        print()
        for x in range(len(self.sonidos)):
            print(x, end='  ')
            for t in self.tiempos:
                lista_notas=t.obtener_lista_estados()
                nota=lista_notas[x]
                if nota: #La idea es que el usuario vea que notas estan activas
                    print(SONIDO_ACTIVADO, end='  ')
                else:
                    print(SONIDO_DESACTIVADO, end='  ')
            print()

    def guardar(self,archivo):
        '''Abre un archivo en modo escritura y guarda la cancion que se encuentra
        en edicion.'''
        with open(archivo,'w') as plp:
            plp.write('{}\n'.format(CABECERA_ARCHIVO))
            plp.write('{},{}\n'.format(LETRA_CANALES,len(self.sonidos)))
            for s in self.sonidos_str:
                tipo=s[0]
                frecuencia=s[1]
                volumen=s[2]
                plp.write('{},{}|{}|{}\n'.format(LETRA_SONIDOS,tipo,frecuencia,volumen))
            tiempo=0 #Contador para evitar repetir el tiempo cuando es el mismo
            for t in self.tiempos:
                tiempo_nuevo=t.obtener_tiempo()
                if tiempo!=tiempo_nuevo:
                    plp.write('{},{}\n'.format(LETRA_MARCAS,tiempo_nuevo))
                cadena=''
                for elem in t.obtener_lista_estados():
                    if elem:
                        cadena+=NOTA_ACTIVADA
                    else:
                        cadena+=NOTA_DESACTIVADA
                plp.write('{},{}\n'.format(LETRA_NOTAS,cadena))
                tiempo=tiempo_nuevo
        print('El archivo se ha guardado con el nombre ',archivo)

    def convertir_a_objeto_sonido(self, parametros):
        '''El metodo convierte una lista de parametros a un objeto sonido
        de la clase SoundFactory.
        Pre:
            lista (list): Debe contener, en este orden, el tipo de sonido,
            la frecuencia y por ultimo el volumen del mismo.'''
        frequency=float(parametros[1])
        volume=float(parametros[2])
        funciones={ONDA_SQUARE:pysounds.SoundFactory.get_square_sound,
                   ONDA_TRIA:pysounds.SoundFactory.get_triangular_sound,
                   ONDA_SINE:pysounds.SoundFactory.get_sine_sound,
                   ONDA_NOISE:pysounds.SoundFactory.get_noise_sound}
        return funciones[parametros[0][0:2]](frequency,volume)

#----------------------------REPRODUCCION----------------------------#
    def obtener_sonidos(self,marca_tiempo):
        """Dado un objeto de la clase MarcaTiempo, se obtienen las notas
        que deben sonar y se devuelve una lista con las mismas.
        Pre:
            marca_tiempo (MarcaTiempo): debe ser una marca de tiempo de la
            clase MarcaTiempo.
        Post:
            sonidos (list): Es una lista que contiene instancias de sonido
            de la clase SoundFactory."""
        lista_notas=marca_tiempo.obtener_lista_estados()
        sonidos=[]
        for i in range(len(lista_notas)):
            if lista_notas[i]:
                sonidos.append(self.sonidos.devolver_posicion(i))
        return sonidos

    def _reproducir(self,lista_tiempos,segundos=-1):
        """El metodo reproduce una lista de marcas de tiempos por una cantidad
        de segundos dada por parametro.
        Si la cantidad de segundos no entra como parametro, la misma toma el
        valor de '-1', de esta manera no se tiene en cuenta el tiempo de
        reproduccion.
        Pre:
            lista_tiempos (list): Es una lista que contiene objetos de
            la clase MarcasTiempo.
            segundos (float): Es la cantidad de segundos que deben reproducirce.
            Si parametro no es indicado entonces se reproduce toda la lista_tiempos
            sin limitacion."""
        sp=pysounds.SoundPlayer(len(self.sonidos))
        a_reproducir=[]
        if segundos==-1:
            for t in lista_tiempos:
                notas=self.obtener_sonidos(t)
                tiempo=t.obtener_tiempo()
                a_reproducir.append((notas,tiempo))
        else:
            tiempo_acumulado=0
            for t in lista_tiempos:
                notas=self.obtener_sonidos(t)
                tiempo=t.obtener_tiempo()
                if tiempo_acumulado+tiempo<=segundos:
                    a_reproducir.append((notas,tiempo))
                    tiempo_acumulado+=tiempo
                    continue
                a_reproducir.append((notas,segundos-tiempo_acumulado))
                break

        for nota,tiempo in a_reproducir:
            sp.play_sounds(nota,tiempo)

        sp.close()

    def reproducir(self,cant_tiempos=-1,segundos=-1):
        '''Toma como parametro una cantidad de marcas de tiempos y una cantidad
        de segundos a reproducir, crea una lista de tiempos y  con ella
        llama a la funcion _reproducir.
        Si cantidad de marcas de tiempos no entra como parametro, tomara el
        valor '-1' que indica que la cantidad de marcas de tiempos a reproducir
        es el total de marcas en la cancion.
        Si la cantidad de segundos no entra como parametro, tomara el valor '-1'
        indicandole a la funcion _reproducir que no se eligio una cantidad de
        segundos para reproducir.'''
        segundos=float(segundos)
        if cant_tiempos==-1:
            self._reproducir(self.tiempos,segundos)
            return
        lista_tiempos=[]
        flag=False #El flag permite agregar a lista_tiempos aquellos que estan
                    # ubicados a partir de la posicion actual del cursor
        contador=0
        marca_actual=self.iterador.actual()
        for t in self.tiempos:
            if t is marca_actual:
                lista_tiempos.append(t)
                contador+=1
                flag=True
                continue
            if flag and contador<cant_tiempos:
                lista_tiempos.append(t)
                contador+=1
        self._reproducir(lista_tiempos,segundos)

#--------------------MANEJO DE MARCAS DE TIEMPO-------------------------#

    def avanzar(self,x=1):
        '''Toma como parametro un numero 'x' y avanza 'x' marcas de tiempo
        respecto a la posicion actual. En caso que no haya una marca siguiente
        a la actual levanta un IndexError.'''
        for iteracion in range(int(x)):
            self.iterador.next()

    def retroceder(self,x=1):
        '''Toma como parametro un numero 'x' y retrocede 'x' marcas de tiempo
        respecto a la posicion actual. En caso que no haya una marca anterior
        a la actual levanta un IndexError.
        Pre: x debe ser un numero int'''
        for iteracion in range(int(x)):
            self.iterador.prev()

    def anadir_marca(self,duracion):
        """Añade un tiempo de duracion dada como parametro al atributo
        tiempos de la clase.
        Pre:
            duracion (float): debe indicar la duracion del tiempo a
            añadir."""
        self.anadir_marca_prev(duracion)
        self.retroceder()

    def anadir_marca_next(self,duracion):
        """Añade un tiempo de duracion dada como parametro al atributo
        tiempos de la clase.
        Pre:
            duracion (float): debe indicar la duracion del tiempo a
            añadir."""
        tiempo=MarcaTiempo(duracion)
        for iteracion in range(len(self.sonidos)):
            tiempo.agregar_estado(False)
        self.iterador.insertar_elem_despues(tiempo)

    def anadir_marca_prev(self,duracion):
        """Añade un tiempo de duracion dada como parametro al atributo
        tiempos de la clase.
        Pre:
            duracion (float): debe indicar la duracion del tiempo a
            añadir."""
        tiempo=MarcaTiempo(duracion)
        for iteracion in range(len(self.sonidos)):
            tiempo.agregar_estado(False)
        self.iterador.insertar_elem_antes(tiempo)
        posicion=self.tiempos.index(self.iterador.actual())
        if self.tiempos.index(self.iterador.actual())==0:
            self.tiempos.insert(posicion,tiempo)



#-------------------------MANEJO DE NOTAS----------------------------#
    def agregar_nota(self,tipo,frecuencia,volumen):
        '''Toma como parametro un tipo de onda, una frequencia y un volumen
        para crear un nuevo sonido y agregar una nueva nota. Modifica el
        objeto_sonido.'''
        self.sonidos_str.append([tipo,frecuencia,volumen])
        sonido_nuevo=self.convertir_a_objeto_sonido([tipo,frecuencia,volumen])
        for t in self.tiempos:
            if t is self.iterador.actual():
                t.agregar_estado(True)
                continue
            t.agregar_estado(False)
        self.sonidos.append(sonido_nuevo)

    def quitar_nota(self,pos):
        '''Toma como parametro una posicion y quita la nota en dicha posicion.
        Pre: pos debe ser un numero int'''
        self.sonidos_str.pop(pos)
        self.sonidos.pop(pos)
        for t in self.tiempos:
            t.quitar_estado(pos)

    def cambiar_estado(self,pos,estado):
        '''Toma como parametro una posicion y un booleano. Cambia el estado de
        la nota en dicha posicion al booleano pasado como parametro.'''
        marca_actual=self.iterador.actual()
        marca_actual.cambiar_estado(pos,estado)
