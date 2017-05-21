class Editor:
    def __init__(self,tiempos,sonidos,canales):
        self.tiempos=tiempos
        self.sonidos=sonidos
        self.canales=canales
        self.pos_t=0
    def representar_cancion(self):
        for t in self.tiempos:
            posicion=self.tiempos.index(t)
            if self.pos_t==posicion:
                print('>>',t.obtener_tiempo(),'<<', end='\t')
            else:
                print(t.obtener_tiempo(), end='\t')
        for x in range(len(t.obtener_nota())):
            print(x, end='\t')
            for t in self.tiempos:

                lista_notas=t.obtener_nota()
                nota=lista_notas[x]
                if nota: #La idea es que el usuario vea que notas estan activas
                    print('[X]', end='\t')
                else:
                    print('[ ]', end='\t')
    def guardar(self,archivo):
        with open(archivo,'w') as plp:
            """Quedo medio raro, mas que nada la parte de los tiempos
            pero me parece que funciona"""
            plp.write('C,{}'.format(self.canales))
            for s in self.sonidos:
                tipo=s[0]
                frecuencia=[1]
                volumen=[2]
                plp.write('S,{}|{}|{}'.format(tipo,frecuencia,volumen))
            tiempo=0
            for t in self.tiempos:
                tiempo_nuevo=t.obtener_tiempo()
                if tiempo!=tiempo_nuevo:
                    plp.write('T,{}'.format(tiempo_nuevo))
                cadena=''
                for elem in t.obtener_nota:
                    if elem:
                        cadena+='#'
                    else:
                        cadena+='·'
                plp.write('N,{}',format(cadena))
                tiempo=tiempo_nuevo
        print('El archivo se ha guardado con el nombre ',archivo)
    def avanzar(self,x=1):
        self.pos_t+=x
    def retroceder(self,x=1):
        self.pos_t-=x
