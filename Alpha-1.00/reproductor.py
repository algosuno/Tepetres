import soundPlayer as pysounds
def leer_archivo(archivo):
    sonidos={}
    tiempos=[]
    cant_canales=0
    contador=0
    contador_tiempos=0
    with open(archivo) as plp:
        linea2=plp.readline()
        linea=linea2.rstrip('\n').split(',')
        while linea2:

            if linea[0].upper()=='C':
                cant_canales=linea[1]

            if linea[0].upper()=='S':
                sonidos[contador]=linea[1].split('|')
                contador+=1

            if linea[0].upper()=='T':
                print(tiempos)
                tiempos.append(linea[1])
                tiempos.append([])
                linea=plp.readline()
                linea=linea.rstrip('\n').split(',')
                while linea[0].upper()=='N':
                    lista=[]
                    for c in linea[1]:
                        lista.append(c=='#')
                    tiempos[contador_tiempos+1].append(lista)
                    linea2=plp.readline()
                    linea=linea2.rstrip('\n').split(',')
                contador_tiempos+=2
                continue
            linea2=plp.readline()
            linea=linea2.rstrip('\n').split(',')
        return tiempos,cant_canales,contador_tiempos,contador,sonidos

def reproducir(tiempos,cant_canales,contador_tiempos,contador,sonidos):
    sp=pysounds.SoundPlayer(int(cant_canales))
    sonidos_final=[]
    print(tiempos)
    for x in range(0,contador):
        tipo,frecuencia,volumen=sonidos[x]
        sonidos_final.append(pysounds.SoundFactory.get_sine_sound(int(frecuencia),float(volumen)))
    for i in range(0,contador_tiempos,2):
        tiempo=float(tiempos[i])
        for sounds in tiempos[i+1]:
            for var in sounds:
                sonorata=[]
                if var:
                    sonorata.append(sonidos_final[sounds.index(var)])
            sp.play_sounds(sonorata,tiempo)
tiempos,cant_canales,contador_tiempos,contador,sonidos=leer_archivo('musica2.plp')
reproducir(tiempos,cant_canales,contador_tiempos,contador,sonidos)
