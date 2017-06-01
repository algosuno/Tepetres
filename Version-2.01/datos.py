def pedir_datos():
    a=verificar(input('Coloque algo: '))
    b=verificar(input('Coloque algo: '))
    c=verificar(input('Coloque algo: '))
    return a,b,c
def verificar(cadena):
    if cadena != '':
        return cadena
    print('Por favor ingrese un numero valido')
    return pedir_datos()