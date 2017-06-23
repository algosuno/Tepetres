from editor import Editor
import cmd

class Shell(cmd.Cmd, object):
    '''Crea la interfaz del programa la cual manejara el usuario
    y muestra el progreso de la edicion del archivo.'''
    intro='''Bienvenido al reproductor,
     ? para ver comandos, help COMANDO para obtener ayuda'''
    prompt='*>>'
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.editor=None
#-----------------------MANEJO DE ARCHIVOS---------------------------#
    def do_REPRODUCIR(self,archivo):
        '''Este comando reproduce el archivo dado como parametro.
        Utilizacion: *>>REPRODUCIR nombre_del_archivo.plp'''
        try:
            self.editor=Editor(archivo)
            self.editor.preparar_reproduccion(-1)
        except IOError:
            print('No se puede encontrar el archivo.')

    def do_ABRIR(self,archivo):
        '''Este comando abre el archivo dado como parametro y lo
        prepara para edicion.
        Utilizacion: *>>ABRIR nombre_del_archivo.plp'''
        try:
            self.editor=Editor(archivo)
            self.editor.representar_cancion()
        except IOError:
            print('No se puede ubicar el archivo.')

    def do_STORE(self,archivo):
        '''Guarda el archivo en edicion actual con el nombre dado
        como parametro.
        Utilizacion: *>>STORE nombre_del_archivo.plp'''
        self.editor.guardar(archivo)
#-----------------------MOVIMIENTO SOBRE TIEMPOS---------------------------#
    def do_STEP(self,x):
        '''Avanza en una posicion sobre las marcas de tiempo.
        Utilizacion: *>>STEP'''
        try:
            self.editor.avanzar()
        except IndexError:
            print('No puede avanzar, se encuentra en la ultima marca de tiempo')
        finally:
            self.editor.representar_cancion()

    def do_BACK(self,x):
        '''Retrocede en una posicion sobre las marcas de tiempo.
        Utilizacion: *>>BACK'''
        try:
            self.editor.retroceder()
        except IndexError:
            print('No puede retroceder, se encuentra en la primer marca de tiempo')
        finally:
            self.editor.representar_cancion()

    def do_STEPM(self,x):
        '''Avanza en 'x' posiciones sobre las marcas de tiempo.
        Utilizacion: *>>STEPM x
        Donde x es un numero entero que indica la cantidad de movimiento.'''
        try:
            self.editor.avanzar(x)
        except IndexError:
            print('No puede avanzar tantas marcas de tiempo')
        finally:
            self.editor.representar_cancion()

    def do_BACKM(self,x):
        '''Retrocede en 'x' posiciones sobre las marcas de tiempo.
        Utilizacion: *>>BACKM x
        Donde x es un numero entero que indica la cantidad de movimiento.'''
        try:
            self.editor.retroceder(x)
        except IndexError:
            print('No puede retroceder tantas marcas de tiempo')
        finally:
            self.editor.representar_cancion()
#-----------------------ADICION Y REMOCION DE SONIDOS------------------------#
    def do_TRACKADD(self,sonido):
        '''Añade un sonido para todos los tiempos, activandolo en el
        tiempo actual.
        Utilizacion: *>>TRACKADD TIPO FRECUENCIA VOLUMEN'''
        linea=sonido.split()
        tipo=linea[0]
        frecuencia=linea[1]
        volumen=linea[2]
        self.editor.agregar_nota(tipo,frecuencia,volumen)
        self.editor.representar_cancion()

    def do_TRACKDEL(self,pos):
        '''Elimina el sonido en la posicion indicada. Lo elimina para
        todas las marcas de tiempo.
        Utilizacion: *>>TRACKDEL x
        Donde x es un numero entero que indica la posicion del sonido.'''
        try:
            self.editor.quitar_nota(int(pos))
        except IndexError:
            print('Indique un numero de track valido.')
        finally:
            self.editor.representar_cancion()



#----------------------ACTIVAR Y DESACTIVAR SONIDOS--------------------------#
    def do_TRACKON(self,pos):
        '''Activa el sonido en la posicion indicada.
        Utilizacion: *>>TRACKON x
        Donde x es un numero entero que indica la posicion del sonido.'''
        try:
            self.editor.cambiar_estado(int(pos),True)
        except ValueError:
            print('El track seleccionado ya se encuentra activado.')
        except IndexError:
            print('Por favor, indique un track dentro de los existentes.')
        finally:
            self.editor.representar_cancion()

    def do_TRACKOFF(self,pos):
        '''Desactiva el sonido en la posicion indicada.
        Utilizacion: *>>TRACKOFF x
        Donde x es un numero entero que indica la posicion del sonido.'''
        try:
            self.editor.cambiar_estado(int(pos),False)
        except ValueError:
            print('El track seleccionado ya se encuentra desactivado.')
        except IndexError:
            print('Por favor, indique un track dentro de los existentes.')
        finally:
            self.editor.representar_cancion()

#-----------------------------REPRODUCCION---------------------------------#
    def do_PLAYALL(self,*args):#Si bien no se va a utilizar, el shell siempre
                                # recibe parametros.
        '''Reproduce el archivo en edicion actual.
        Utilizacion: *>>PLAYALL'''
        self.editor.reproducir(-1)

    def do_PLAY(self,*args):
        '''Reproduce la marca de tiempo actual.
        Utilizacion: *>>PLAY
        Donde x es un numero entero que indica la posicion del sonido.'''
        self.editor.reproducir(1)

    def do_PLAYMARKS(self,x):
        '''Reproduce las siguientes 'x' marcas de tiempo.
        Utilizacion: *>>PLAYMARKS x
        Donde x es un numero entero que indica la cantidad de tiempos.'''
        self.editor.reproducir(int(x))

    def do_PLAYSECONDS(self,segundos):
        '''Reproduce 'x' segundos a partir de la marca de tiempo actual.
        Utilizacion: *>>PLAYSECONDS x
        Donde x es un numero que indica la cantidad de segundos.'''
        self.editor.reproducir(-1,segundos)


#-----------------ADICION Y REMOCION DE MARCAS DE TIEMPO--------------------#

    def do_MARKADD(self,duracion):
        '''Añade una marca de tiempo de duracion 'x' segundos en la posicion
        actual del cursor. Todos los sonidos estaran desactivados.
        Utilizacion: *>>MARKADD x
        Donde x es un numero que indica la duracion en segundos.'''
        self.editor.anadir_marca(float(duracion))
        self.editor.representar_cancion()

    def do_MARKADDNEXT(self,duracion):
        '''Añade una marca de tiempo de duracion 'x' segundos a la
        derecha de la posicion actual del cursor. Todos los sonidos
        estaran desactivados.
        Utilizacion: *>>MARKADDNEXT x
        Donde x es un numero que indica la duracion en segundos.'''
        self.editor.anadir_marca_next(float(duracion))
        self.editor.representar_cancion()

    def do_MARKADDPREV(self,duracion):
        '''Añade una marca de tiempo de duracion 'x' segundos a la
        izquierda de la posicion actual del cursor. Todos los sonidos
        estaran desactivados.
        Utilizacion: *>>MARKADDPREV x
        Donde x es un numero que indica la duracion en segundos.'''
        self.editor.anadir_marca_prev(float(duracion))
        self.editor.representar_cancion()

    def do_SALIR(self,*args):
        """Permite salir del programa.
        Utilizacion: *>>SALIR"""
        return True







Shell().cmdloop()
