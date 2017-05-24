from ListaEnlazada import ListaEnlazada
import soundPlayer as pysounds
from tiempo import Tiempo
class Archivo:
    def __init__(self,archivo):
        self.archivo=archivo
        self.tiempos=ListaEnlazada()
        self.sonidos=ListaEnlazada()
        self.canales=0
        self.objeto_sonidos=ListaEnlazada()
#---------------------------------------------------------------------#
    def leer(self):
        with open(self.archivo) as plp:
            linea=plp.readline()
            linea=linea.rstrip('\n').split(',')
            while len(linea)>1:

                if linea[0].upper()=='C':
                    self.canales=linea[1]

                if linea[0].upper()=='S':
                    lista=linea[1].split('|')
                    self.sonidos.append(lista)

                if linea[0].upper()=='T':
                    duracion= float(linea[1])
                    linea=plp.readline()
                    linea=linea.rstrip('\n').split(',')
                    while linea[0].upper()=='N':
                        t=Tiempo(duracion)
                        for c in linea[1]:
                            t.agregar_nota(c=='#')
                        self.tiempos.append(t)
                        linea=plp.readline()
                        linea=linea.rstrip('\n').split(',')
                    continue
                linea=plp.readline()
                linea=linea.rstrip('\n').split(',')
#---------------------------------------------------------------------#
    def convertir_objeto(self, lista):
        frequency=float(lista[1])
        volume=float(lista[2])
        funciones={'SQ':pysounds.SoundFactory.get_square_sound,
                   'TR':pysounds.SoundFactory.get_square_sound,
                   'SI':pysounds.SoundFactory.get_square_sound,
                   'NO':pysounds.SoundFactory.get_square_sound}
        return funciones[lista[0][0:2]](frequency,volume)
#---------------------------------------------------------------------#
    def conversion(self):
        for s in self.sonidos:
            sonido=self.convertir_objeto(s)
            self.objeto_sonidos.append(sonido)
#---------------------------------------------------------------------#
    def agregar_objeto(self):
        lista=list(self.objeto_sonidos)
        for t in self.tiempos:
            nota=t.obtener_nota()
            contador=0
            for n in nota:

                if n:
                    t.agregar_nota_obj(lista[nota.index(n)+contador])
                    nota.pop(nota.index(n))
                    contador+=1
                #else:
                    #t.agregar_nota_obj(None) - Este codigo esta comentado porque no se si va
#---------------------------------------------------------------------#
    def reproducir(self):
        sp=pysounds.SoundPlayer(2)
        a_reproducir=[]
        for t in self.tiempos: #me parece que esta implementacion va a tardar
                              # Si tarda creamos una funcion que obtenga la nota y el tiempo antes
            notas=t.obtener_nota_obj()
            tiempo=t.obtener_tiempo()
            a_reproducir.append((notas,tiempo))
        for nota,tiempo in a_reproducir:

            sp.play_sounds(nota,tiempo)

        sp.close()
#---------------------------------------------------------------------#
    def obtener_datos(self):
        return self.tiempos,self.sonidos,self.canales
