from archivo import Archivo
from editor import Editor
import cmd

#--------------------------------------------------------------------#

class Shell(cmd.Cmd, object):
    '''Crea la interfaz del programa la cual manejara el usuario y va mostrando el progreso
    de la edicion del archivo.'''
    intro='Bienvenido al reproductor, ? para ver comandos, help COMANDO para obtener ayuda'
    prompt='*>>'
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.archivo=None
        self.editor=None
        
#-----------------------MANEJO DE ARCHIVOS---------------------------#

    def do_REPRODUCIR(self,archivo):
        '''Toma como parametro un archivo y lo reproduce'''
        self.archivo=Archivo(archivo)
        self.archivo.leer()
        self.archivo.conversion()
        self.archivo.agregar_objeto()
        self.archivo.reproducir()

    def do_ABRIR(self,archivo):
        '''Toma como parametro un archivo y lo abre en consola'''
        self.archivo=Archivo(archivo)
        self.archivo.leer()
        self.archivo.conversion()
        self.archivo.agregar_objeto()
        self.editor=Editor(self.archivo)
        self.editor.representar_cancion()

    def do_STORE(self,archivo):
        '''Toma como parametro un archivo y lo guarda'''
        self.editor.guardar(archivo)
        
#-----------------------MOVIMIENTO SOBRE TIEMPOS---------------------------#

    def do_STEP(self,x):
        '''Avanza una marca de tiempo'''
        self.editor.avanzar()
        self.editor.representar_cancion()

    def do_BACK(self,x):
        '''Retrodece una marca de tiempo'''
        self.editor.retroceder()
        self.editor.representar_cancion()

    def do_STEPM(self,x):
        '''Toma como parametro un numero 'x' y avanza 'x' marcas de tiempo.
        Pre: 'x' en un numero int'''        
        self.editor.avanzar(x)
        self.editor.representar_cancion()

    def do_BACKM(self,x):
        '''Toma como parametro un numero 'x' y retrocede 'x' marcas de tiempo.
        Pre: 'x' en un numero int''' 
        editor.retroceder(x)
        editor.representar_cancion()
        
#-----------------------ADICION Y REMOCION DE SONIDOS---------------------------#

    def do_TRACKADD(self,parametros): #te parece mas descriptivo ponerle sonido al parametro?
        '''Toma como parametro 'parametros' y agrega un nuevo track.
        Pre: -'parametros' debe ser una lista que contenga tres partes
             -'parametros' debe estar compuesta por digitos'''
        linea=parametros.split()
        tipo=linea[0]
        frecuencia=linea[1]
        volumen=linea[2]
        self.editor.agregar_nota(tipo,volumen,frecuencia)
        self.editor.representar_cancion()

    def do_TRACKDEL(self,pos):
        '''Dada una posicion 'pos' elimina el track en dicha posicion'''
        self.editor.quitar_nota(int(pos))
        self.editor.representar_cancion()
        
#-----------------------------REPRODUCCION---------------------------------#

    def do_PLAYALL(self,x):
        '''Reproduce todo el archivo desde el comienzo'''
        self.editor.reproducir()

    def do_PLAY(self,x):
        '''Reproduce la marca en la que se encuentra el cursor actualmente''' #chequear desp
        self.editor.reproducir_tiempos(1)

    def do_PLAYMARKS(self,x):
        '''Reproduce las marcas de tiempo dadas'''
        self.editor.reproducir_tiempos(int(x))

    def do_PLAYSECONDS(self,segundos):
        '''Toma como parmetro una cantidad de segundos y los reproduce.
        Pre: -'segundos' debe ser un numero'''
        self.editor.reproducir_tiempos(False,float(segundos))

    def do_SALIR(self):
        '''Demasiado dificil de explicar en tan solo unas lineas. Para entender
        el funcionamiento de esto metodo se requiere aprobar las materias: 67.01/68.09/61.23/64.05 
        y tener la tesis de ingenieria nuclear'''
        return 2//0






Shell().cmdloop()
