#generar un codigo que genere curp en base a valores establecidos. 
import unicodedata

#TODO:LIMPIAR DATOS, NO NUMEROS, NO ACENTOS, NO MINISCULAS. 
def borrar_acentos(cadena):
    normalizar = unicodedata.normalize('NFD',cadena) #? Normal Form Decomposed: Separa letras y acentos (é = e +´)
    cadena_sinacentos = ""
    for i in normalizar: 
        if unicodedata.category(i) != 'Mn': #? Categoria de caracteres. Mn Mark Nonspacing. 
            cadena_sinacentos += i
    return cadena_sinacentos

def limpiar_numeros(cadena): 
    nueva_cadena= ""
    for i in cadena: 
        if not i.isdigit():
            nueva_cadena += i
    return nueva_cadena

#TODO: EVALUAR QUE SEA UN NUMERO REAL. 

#TODO: Evaluar que el estado sea valido. 

nombres = borrar_acentos(limpiar_numeros(input("Ingresa Nombres: "))).upper()
apellido_paterno = borrar_acentos(limpiar_numeros(input("Ingresa Apellido Paterno: "))).upper()
apellido_materno = borrar_acentos(limpiar_numeros(input("Ingresa Apellido Materno: "))).upper()

segmentos_curp ={nombres, apellido_paterno, apellido_materno}

print(segmentos_curp)

