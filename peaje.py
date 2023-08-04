'''Modulo Peaje. Contiene todas las funcionalidades para procesar
peajes
'''

def listado_categoria_vehiculo(tabla):   
    """Esta funcion devuelve un listado con los distintos tipos de categoria vehicular,
       de una tabla, sea tabla parametro de la funcion """
    listado_Cat_Vehiculos=[]
     
    for x in tabla:
        categoria = x[2]
        if categoria not in listado_Cat_Vehiculos:
            listado_Cat_Vehiculos.append(categoria)
    return listado_Cat_Vehiculos

def listador_peajes(tabla):
    """Esta funcion genera un listado con los distintos tipos de peajes que se 
       presentan en la tabla, sea tabla un parametro de la funcion. """
    listado_Peaje=[]
    for x in tabla:
        peaje=x[3]
        if peaje not in listado_Peaje:
            listado_Peaje.append(peaje)
    return listado_Peaje

def listado_registros(tabla,categoria):
    """Esta funcion devuelve un listado de registros por categori­a. Sea categoria
    un parametro ingresado por consola."""
    listado_categoria=[]
    for x in tabla:
        if x[2]==categoria:
            listado_categoria.append(x)
            
    return listado_categoria

def dia_febrero(tabla,dia):
    "Esta funcion devuelve los registros del dia de febrero ingresado."
    listado_DIA=[]
    for x in tabla:
        dia_archivo=int(x[0][0])
        if dia_archivo == dia:
            listado_DIA.append(x)
    return listado_DIA

def registro_por_hora_peaje(tabla,fecha,sentido,listado_peajes):
    """Esta funcion devuelve una tabla que registra la circulacin de vehiculos
       por hora, en la fecha y sentido especificados, en los distintos peajes.
    """
    lista_hora_peaje = [[0]*len(listado_peajes) for i in range(24)]
    fecha = int(fecha.split('/')[0])
    for registro in tabla:
        dia = int(registro[0][0])
        if dia == fecha and registro[5] == sentido.capitalize():
            lista_hora_peaje[int(registro[1])][listado_peajes.index(registro[3])] += int(registro[7].replace('.',''))
    return lista_hora_peaje
