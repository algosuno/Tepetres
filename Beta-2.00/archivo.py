class Archivo:
    def __init__(self,archivo):
        self.archivo=archivo
        self.tiempos=[]
        self.sonidos=[]
        self.canales=0
        self.repr=[]
    def leer(self):
        contador_tiempos=0
        with open(self.archivo) as plp:
            linea=plp.readline()
            linea=linea.rstrip('\n').split(',')
            while len(linea)>1:

                if linea[0].upper()=='C':
                    self.canales=linea[1]

                if linea[0].upper()=='S':
                    self.sonidos.append(linea[1].split('|'))

                if linea[0].upper()=='T':
                    self.tiempos.append(linea[1])
                    tiempos.append([])
                    linea=plp.readline()
                    linea=linea.rstrip('\n').split(',')
                    while linea[0].upper()=='N':
                        lista=[]
                        for c in linea[1]:
                            lista.append(c=='#')
                        self.tiempos[contador_tiempos+1].append(lista)
                        linea=plp.readline()
                        linea=linea.rstrip('\n').split(',')
                    contador_tiempos+=2
                    continue
                linea=plp.readline()
                linea=linea.rstrip('\n').split(',')
    def reproducir(self):
        sp=pysounds.SoundPlayer(int(self.canales))
        melodia_final=[]
        objeto_sonidos=[]
        for s in self.sonidos:
            frequency=float(s[1])
            volume=float(s[2])
            if s[0][0:2]=='SQ':
                objeto_sonidos.append(pysounds.SoundFactory.get_square_sound(frequency, volume))
            if s[0]=='TRIA':
                objeto_sonidos.append(pysounds.SoundFactory.get_triangular_sound(frequency,volume))
            else:
                objeto_sonidos.append(pysounds.SoundFactory.get_sine_sound(frequency, volume))

        for t in range(0,len(self.tiempos),2):
            tiempo=float(self.tiempos[t])
            for nota in self.tiempos[t+1]:
                for n in nota:
                    nota_obj=[]
                    nota2=[]
                    if n:
                        nota_obj.append(objeto_sonidos[nota.index(n)])
                        nota2.append(objeto_sonidos[nota.index(n)])
                    else:
                        nota2.append(False)
                    melodia_final.append((nota_obj,tiempo))
                    self.repr.append(tiempo)
                    self.repr.append(nota2)
        for nota,tiempo in melodia_final:
            sp.play_sounds(nota,tiempo)
        sp.close()
    def obtener_datos(self):
        return self.tiempos,self.sonidos,self.canales,self.repr
