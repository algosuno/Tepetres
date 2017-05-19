import soundPlayer as pysounds
class Reproductor:
    def __init__(self,archivo):
        self.archivo=open(archivo)
        self.canales=0
        self.contador=0
        self.contador_tiempos=0
        self.sonidos={}
        self.tiempos=[]
        self.sonidos_final=[]
        self.reproductor=0
    def leer(self):
        linea = self.nueva_linea()
            while len(linea)>1:
                if linea[0].upper()=='C':
                    self.canales=linea[1]
                if linea[0].upper()=='S':
                    sonidos[contador]=linea[1].split('|')
                    self.contador+=1
                if linea[0].upper()=='T':
                    self.tiempos.append(linea[1])
                    self.tiempos.append([])
                    linea=plp.readline()
                    linea=linea.rstrip('\n').split(',')
                    while linea[0].upper()=='N':
                        lista=[]
                        for c in linea[1]:
                            lista.append(c=='#')
                        self.tiempos[self.contador_tiempos+1].append(lista)
                        linea=self.nueva_linea()
                    self.contador_tiempos+=2
                    continue
                linea=self.nueva_linea()
    def nueva_linea(self):
        return self.archivo.readline().rstrip('\n').split(',')
    def limpiar_sonidos(self):
        for i in range(self.contador):
            tipo,frecuencia,volumen=sonido[i]
            frecuencia=float(frecuencia)
            volumen=float(volumen)
            if frecuencia.upper()=='SINE':
                self.sonidos_final.append(pysounds.SoundFactory.get_sine_sound(frecuencia,volumen))
            elif tipo.upper()=='SQR':
                self.sonidos_final.append(pysounds.SoundFactory.get_square_sound(frecuencia,volumen))
            elif tipo.upper()=='TRIANGLE':
                self.sonidos_final.append(pysounds.SoundFactory.get_triangular_sound(frecuencia,volumen))
    def abrir_reproductor(self):
        self.reproductor=pysounds.SoundPlayer(int(self.canales))
    def cerrar_reproductor(self):
        self.reproductor.close()
    def reproducir(self):
        for i in range(0,self.contador_tiempos,2):
            tiempo=float(self.tiempos[i])
            for sonidos in self.tiempos[i+1]:
                for x in sonidos:
                    track=[]
                    if var:
                        track.append(self.sonidos_final[sonidos.index(x)])
                sp.play_sounds(tack,tiempo)
