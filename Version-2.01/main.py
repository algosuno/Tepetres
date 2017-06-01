from archivo import Archivo
from editor import Editor
import cmd
class Shell(cmd.Cmd, object):
    intro='Bienvenido al reproductor, ? para ver comandos, help COMANDO para obtener ayuda'
    prompt='*>>'
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.archivo=None
        self.editor=None
#-----------------------MANEJO DE ARCHIVOS---------------------------#
    def do_REPRODUCIR(self,archivo):

        self.archivo=Archivo(archivo)
        self.archivo.leer()
        self.archivo.conversion()
        self.archivo.agregar_objeto()
        self.archivo.reproducir()

    def do_ABRIR(self,archivo):
        self.archivo=Archivo(archivo)
        self.archivo.leer()
        self.archivo.conversion()
        self.archivo.agregar_objeto()
        self.editor=Editor(self.archivo)
        self.editor.representar_cancion()

    def do_STORE(self,archivo):
        self.editor.guardar(archivo)
#-----------------------MOVIMIENTO SOBRE TIEMPOS---------------------------#
    def do_STEP(self,x):
        self.editor.avanzar()
        self.editor.representar_cancion()

    def do_BACK(self,x):
        self.editor.retroceder()
        self.editor.representar_cancion()

    def do_STEPM(self,x):
        self.editor.avanzar(x)
        self.editor.representar_cancion()

    def do_BACKM(self,x):
        editor.retroceder(x)
        editor.representar_cancion()
#-----------------------ADICION Y REMOCION DE SONIDOS------------------------#
    def do_TRACKADD(self,parametros):
        linea=parametros.split()
        tipo=linea[0]
        frecuencia=linea[1]
        volumen=linea[2]
        self.editor.agregar_nota(tipo,frecuencia,volumen)
        self.editor.representar_cancion()

    def do_TRACKDEL(self,pos):
        self.editor.quitar_nota(int(pos))
        self.editor.representar_cancion()

#----------------------ACTIVAR Y DESACTIVAR SONIDOS--------------------------#
    def do_TRACKON(self,pos):
        self.editor.activar_nota(int(pos))
        self.editor.representar_cancion()

    def do_TRACKOFF(self,pos):
        self.editor.desactivar_nota(int(pos))
        self.editor.representar_cancion()

#-----------------------------REPRODUCCION---------------------------------#
    def do_PLAYALL(self,x):
        self.editor.reproducir()

    def do_PLAY(self,x):
        self.editor.reproducir_tiempos(1)

    def do_PLAYMARKS(self,x):
        self.editor.reproducir_tiempos(int(x))

    def do_PLAYSECONDS(self,segundos):
        self.editor.reproducir_tiempos(False,float(segundos))

    def do_MARKADD(self,duracion):
        return
    def do_MARCKADDNEXT(self,duracion):
        return
    def do_MARCKADDPREV(self,duracion):
        return
    def do_SALIR(self):
        return 2//0






Shell().cmdloop()
