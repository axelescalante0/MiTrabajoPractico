
import peaje as pj
import csv #Abro el archivo y lo cargo a una tabla

path = 'Transito Febrero 2023.csv'
with open(path,"r", encoding='utf-8')as archivo:
    lectura=csv.reader(archivo, delimiter=";")
    encabezado=next(archivo)
    
    tabla=[]
    
    for linea in lectura:
        if linea[0] != '' and linea[0]!='Total general':
            linea[0]=linea[0].split("/") 
            tabla.append(linea[:8])

# 1

print('======================================')
print('Se muestra un listado de los distintos tipos de categorias vehicular que se encuentran en el archivo:\n')
lista_vehiculos = pj.listado_categoria_vehiculo(tabla)
for x in lista_vehiculos:
    print(x,end=', ')
print('======================================\n')


print('======================================')
print('Lista de los peajes disponibles en el archivo, ID(peaje)')

listado_de_peajes = pj.listador_peajes(tabla)
for x in listado_de_peajes:
    print(x,end=', ')
print('======================================')
    
    #2- los registros correspondientes a categori­a ingresada
print('\n======================================')

cat=input('ingrese categoria de vehiculo del cual desea saber sus registros: ')
while cat not in lista_vehiculos:
    print('\nCategoria ingresada no valida. Por favor intente de nuevo.')
    cat=input('ingrese categoria de vehiculo del cual desea saber su registro: ')
    
lista_categoria = pj.listado_registros(tabla, cat)
for x in lista_categoria:
    print(x)

print('======================================')

#3-Ingresar un dia del mes de febrero.
print('\n======================================')
dia=int(input('Ingrese el dia de febrero del cual desea saber sus registros: '))
while dia <1 or dia > 28:
    print('\nDia ingresado no valido. Por favor intente de nuevo')
    dia=int(input('Ingrese el dia defebrero del cual desea saber sus registros: '))
    
registro_Dia = pj.dia_febrero(tabla, dia)
for x in registro_Dia:
    print(x)

print('======================================\n')


#4 ingresar fecha
print('======================================\n')
print('A continucion generaremos una tabla en donde se mostraran para cada hora en los distintos peajes la circulacion de vehiculos en relacion fecha-sentido. Por favor ingrese los siguientes datos: \n')
fecha=input('ingrese fecha (dd/mm/aaaa) : ')
sentido=input('Ingrese sentido de circulacion.(Centro/Provincia): ')
tabla_generada = pj.registro_por_hora_peaje(tabla, fecha, sentido, listado_de_peajes)


for x in listado_de_peajes:
    print(x,'',end='')
print('')

for indice, contenido in enumerate(tabla_generada):
    print(indice,contenido)


 
print('======================================\n')
            


#5
print('======================================\n')
print('Por ultimo, generaremos un nuevo archio csv en relacion IDpeaje-fecha. Por favor ingrese los siguientes datos.\n')
print('Peajes disponibles:',listado_de_peajes)
tabla_sentido_Centro = [[0]*len(lista_vehiculos) for i in range(24)]
tabla_sentido_Provincia = [[0]*len(lista_vehiculos) for i in range(24)]

ID_peaje = input('\nIngrese peaje : ')
Fecha_Peaje = input('ingrese fecha(dd/mm/aaaa):')
fecha = int(Fecha_Peaje.split('/')[0])

for registro in tabla:
    
    dia = int(registro[0][0])
    if  dia==fecha and registro[3]==ID_peaje.upper():
        if registro[5]=="Centro":
            tabla_sentido_Centro[int(registro[1])][lista_vehiculos.index(registro[2])]+=int(registro[7].replace('.',''))
        else:
            tabla_sentido_Provincia[int(registro[1])][lista_vehiculos.index(registro[2])]+=int(registro[7].replace('.','')) 
            
tabla_dos_sentidos=[list(zip(fila1, fila2)) for fila1, fila2 in zip(tabla_sentido_Centro,tabla_sentido_Provincia)]

  # FlujoVehicular_ddmmaaaa_CodPeaje.csv
  
nombre = 'FlujoVehicular_'+Fecha_Peaje.replace('/','')+'_'+ID_peaje+'.csv'  
with open(nombre,'w',newline='')as arch:
    escritor=csv.writer(arch, delimiter=';')
    texto=['Pases de vehiculos para el peaje:','','',ID_peaje]
    escritor.writerow(texto)
    texto2=['Fecha',Fecha_Peaje]
    escritor.writerow(texto2)
    
    lista_nueva=['Categoria:']
    for x in lista_vehiculos:
        lista_nueva.append(x)
        lista_nueva.append('')
    escritor.writerow(lista_nueva)#escribo categorias de vehiculos
    
    sentidos=['Centro','Provincia']*len(lista_vehiculos) #Creo una list contendra los sentidos, y multiplico el contenido por el len de la lista de vehiculos, luego escribo esa lista    
    listamod2=['Hora']+sentidos
    escritor.writerow(listamod2)
    
    
    for indice,linea in enumerate( tabla_dos_sentidos):
        fila=[]
        for tupla in linea:
            fila.extend(tupla)
        escritor.writerow([str(indice)]+fila)

        
print('\nArchivo generado con exito!.')
print('\nFin del programa.')