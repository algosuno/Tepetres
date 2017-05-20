from archivo import Archivo
from editor import Editor
import cmd
class Shell(cmd.Cmd, object):
    intro='Bienvenido a mi programa'
    prompt='*>>'
    def do_ABRIR(self,archivo):
        a= Archivo(archivo)
        tiempos,sonidos,canales,escena=a.leer().obtener_datos()
        editor=Editor(tiempos,sonidos,canales,escena)
        editor.representar_cancion()
    def do_STORE(self,archivo):
        editor.guardar(archivo)
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




Shell().cmdloop()
