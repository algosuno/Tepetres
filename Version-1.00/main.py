from archivo import Archivo
from editor import Editor
import cmd
class Shell(cmd.Cmd, object):
    intro='Bienvenido a mi programa'
    prompt='*>>'
#-----------------------MANEJO DE ARCHIVOS---------------------------#
    def do_REPRODUCIR(self,archivo):
        a=Archivo(archivo)
        a.leer()
        a.conversion()
        a.agregar_objeto()
        a.reproducir()

    def do_ABRIR(self,archivo):
        a= Archivo(archivo)
        a.leer()
        editor=Editor(a)
        editor.representar_cancion()

    def do_STORE(self,archivo):
        editor.guardar(archivo)
#-----------------------MOVIMIENTO SOBRE TIEMPOS---------------------------#
    def do_STEP(self):
        editor.avanzar()
        editor.representar_cancion()

    def do_BACK(self):
        editor.retroceder()
        editor.representar_cancion()

    def do_STEPM(self,x):
        editor.avanzar(x)
        editor.representar_cancion()

    def do_BACKM(self,x):
        editor.retroceder(x)
        editor.representar_cancion()
#-----------------------ADICION Y REMOCION DE SONIDOS---------------------------#
    def do_TRACKADD(self,type,frequency,volume):
        editor.agregar_nota(type,frequency,volume)

    def do_TRACKDEL(self,pos):
        editor.quitar_nota(self,pos)
#-----------------------------REPRODUCCION---------------------------------#
    def do_PLAYALL(self):
        editor.reproducir()

    def do_SALIR(self):
        return 2//0






Shell().cmdloop()
