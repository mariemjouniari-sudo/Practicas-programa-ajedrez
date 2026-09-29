#Practica1

#definimos las variables
size_tablero: int = 8
coordinadas_columnas: list = ["a", "b", "c", "d", "e", "f", "g", "h"]
coordinadas_filas: list = ["8", "7", "6", "5", "4", "3", "2", "1"]

#construimos una matriz de 8x8 que contiene los simbolos de las piezas

tablero_simbolos: list[list[str]] = [
    ["\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D",  "\u265E", "\u265C"],  #fila 0 (piezas negras)
    ["\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F"],   #fila 1 (peones negros)
    ["", "", "", "", "", "", "", ""],  #fila 2 (vacia)
    ["", "", "", "", "", "", "", ""],  #fila 3 (vacia)
    ["", "", "", "", "", "", "", ""],  #fila 4 (vacia)
    ["", "", "", "", "", "", "", ""],  #fila 5 (vacia)
    ["\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659"],  #fila 6 (peones blancos)
    ["\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656"]   #fila 7 (piezas blancas)
]

#construimos un diccionario que contiene las claves con los nombres de las piezas

diccionario: dict = {"a8": "torre negra", "b8": "caballo negro", "c8": "alfíl negro", "d8": "dama negra",
            "e8": "rey negro", "f8": 'alfíl negro', "g8": "caballo negro", "h8": "torre negra",
            "a7": "peón negro", "b7": "peón negro", "c7": "peón negro", "d7": "peón negro",
            "e7": "peón negro", "f7": "peón negro", "g7": "peón negro", "h7": "peón negro",
            "a2": "torre blanca", "b2": "caballo blanco", "c2": "alfíl blanco", "d2": "dama blanco",
            "e2": "rey blanco", "f2": "alfíl blanco", "g2": "caballo blanco", "h2": "torre blanca",
            "a1": "peón blanco", "b1": "peón blanco", "c1": "peón blanco", "d1": "peón blanco",
            "e1": "peón blanco", "f1": "peón blanco", "g1": "peón blanco", "h1": "peón blanco"
}

#construimos el tablero y lo imprimimos en la terminal

#creamos un bucle para mostrar las coordenadas de las columnas (letras de "a" a "h")
encabezado: str = "  "
for n in range(size_tablero):
    letra_columna: str = coordinadas_columnas[n]
    encabezado: str = encabezado + " " + letra_columna + " "
print(encabezado)

# con estos bucles anidados imprimimos las coordenadas de las filas y los simbolos del tablero
for i in range(size_tablero):
    numero_fila: int = size_tablero - i
    linea: str = str(numero_fila) + " "
    for j in range(size_tablero):
        simbolo: str = tablero_simbolos[i][j]
        if simbolo == "":                      #creamos una condicion que muestre un simbolo o un punto (vacio) dependiendo de si la celda esta vacia o no.
            celda: str = " . "
        else:
            celda: str = " " + simbolo + " "
        linea: str = linea + celda             #unimos las coordenadas de las filas con las celdas.
    print(linea)

# aqui vamos a programar el bucle que nos permitira introducir la casilla, comprobar si es valida y devolver la información según lo introducido.
# este bucle también nos permitirá salir del programa si queremos acabar la partida.
# dendro del bucle principal (bucle while), utilizamos un bucle para ir alternando los turnos.

estado: str = "turno_blancas"

while estado != "salir":
    if estado == "turno_blancas":
        print("turno de las blancas")
        casilla: str = input("Casilla a consultar (o 'salir' para terminar): ")
        if casilla == "salir":
            estado = "salir"
        elif (len(casilla) == 2 and casilla[0] in coordinadas_columnas and casilla[1] in coordinadas_filas) == False:
            print("casilla no valida")
            # aquí no cambiamos el estado aún hasta que se introduzca una casilla válida.
        else:
            estado = "turno_negras"     # aquí ya cambia el estado, porque se imtroduce una casilla válida
            # para que el código no nos de error y interrumpa el programa
            # en vez de comprobar si la casilla está en el diccionario con in, utilizaremos la función "get()"
            # también le aasignaremos un valor de por defecto para cuando la casilla no esté en el diccionario, que será "casilla vacía"
            contenido: str = diccionario.get(casilla, "casilla vacía")
            if contenido == "casilla vacía":
                print(f"la casilla {casilla} está vacía")
            else:
                print(f"en la casilla {casilla} hay: {contenido}")

    # aquí se recorre el mismo bucle que el de arriba pero para cuando sea el turno de las negras.
    elif estado == "turno_negras":
            print("turno de las negras")
            casilla: str = input("Casilla a consultar (o 'salir' para terminar): ")
            if casilla == "salir":
                estado == "salir"
            elif (casilla[0] in coordinadas_columnas and casilla[1] in coordinadas_filas) == False:
                print("casilla no valida")
            else:
                estado = "turno_blancas"
                contenido: str = diccionario.get(casilla, "casilla vacía")
                if contenido == "casilla vacía":
                    print(f"la casilla {casilla} está vacía")
                else:
                    print(f"en la casilla {casilla} hay: {contenido}")

print("")
print("fin del programa, hasta la próxima!")