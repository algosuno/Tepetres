class Archivo:
    def __init__(self,archivo):
        self.archivo=archivo
        self.tiempos=[]
        self.sonidos=[]
        self.canales=0
    def leer(self):
        with open(self.archivo) as plp:
            linea=plp.readline()
            linea=linea.rstrip('\n').split(',')
            while len(linea)>1:

                if linea[0].upper()=='C':
                    self.canales=linea[1]

                if linea[0].upper()=='S':
                    self.sonidos.append(linea[1].split('|'))

                if linea[0].upper()=='T':
                    duracion= float(linea[1])
                    linea=plp.readline()
                    linea=linea.rstrip('\n').split(',')
                    while linea[0].upper()=='N':
                        t=Tiempo(duracion)
                        lista=[]
                        for c in linea[1]:
                            lista.append(c=='#')
                        t.agregar_nota(lista)
                        self.tiempos.append(t)
                        linea=plp.readline()
                        linea=linea.rstrip('\n').split(',')
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

        for t in self.tiempos:
            nota=t.obtener_nota()
            for n in nota:
                if n:
                    t.agregar_nota_obj(objeto_sonidos[nota.index(n)])
                #else:
                    #t.agregar_nota_obj(None) - Este codigo esta comentado porque no se si va
        for t in self.tiempos: #me parece que esta implementacion va a tardar
                              # Si tarda creamos una funcion que obtenga la nota y el tiempo antes
            sp.play_sounds(t.obtener_nota_obj,t.obtener_tiempo)
        sp.close()
    def obtener_datos(self):
        return self.tiempos,self.sonidos,self.canales
