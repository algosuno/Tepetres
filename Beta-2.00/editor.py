class Editor:
    __init__(self,tiempos,sonidos,canales,escena):
        self.tiempos=tiempos
        self.sonidos=sonidos
        self.canales=canales
        self.escena=escena
        self.pos_t=0
    def representar_cancion(self):
        for t in range(0,len(self.escena),2):
            posicion=t//2
            if self.pos_t==posicion:
                print('>>',self.escena[t],'<<', end='\t')
            else:
                print(self.escena[t], end='\t')
        for x in range(len(self.escena[1])):
            for nota in range(1,len(self.escena),2):
                note=self.escena[nota][x]
                if note:
                    print(note, end='\t')
                else:
                    print('\t', end='\t')
    def guardar(self,archivo):
        with open(archivo,'w') as plp:
            plp.write('C,{}'.format(self.canales))
            for s in self.sonidos:
                tipo=s[0]
                frecuencia=[1]
                volumen=[2]
                plp.write('S,{}|{}|{}'.format(tipo,frecuencia,volumen))
            for t in range(0,len(self.tiempos),2):
                tiempo=self.tiempos[t]
                lista_notas=self.tiempos[t+1]
                plp.write('T,{}'.format(tiempo))
                for nota in lista_notas:
                    cadena=''
                    for c in nota:
                        if c:
                            cadena +='#'
                        else:
                            cadena +='·'
                    plp.write('N,{}'.format(cadena))
        print('El archivo se ha guardado con el nombre ',archivo)
    def avanzar(self,x=0):
        self.pos_t+=x
    def retroceder(self,x=0):
        self.pos_t-=x
