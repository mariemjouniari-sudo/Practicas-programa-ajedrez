#Practica1

#definimos las variables
size_tablero: int = 8
coordinadas_columnas: list = ["a", "b", "c", "d", "e", "f", "g", "h"]

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

#construimos una matriz de 8x8 que contiene los nombres de las piezas

tablero_nombres: list[list[str]] = [
    ["torre negra", "caballo negro", "alfíl negro", "dama negra", "rey negro", "alfíl negro", "caballo negro", "torre negra"], 
    ["peón negro", "peón negro", "peón negro", "peón negro", "peón negro", "peón negro", "peón negro", "peón negro"], 
    ["", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", ""], 
    ["torre blanca", "caballo blanco", "alfíl blanco", "dama blanco", "rey blanco", "alfíl blanco", "caballo blanco", "torre blanca"],
    ["peón blanco", "peón blanco", "peón blanco", "peón blanco", "peón blanco", "peón blanco", "peón blanco", "peón blanco"]
]

#construimos el tablero y lo imprimimos en la terminal

#creamos un bucle para mostrar las coordenadas de las columnas (letras de "a" a "h")
encabezado: str = ""
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
        if simbolo == "":                      #creamos una condicion que muestre un simbolo o un punto (vacio) dependiendo de si la celda esta vacia o no
            celda: str = " . "
        else:
            celda: str = " " + simbolo + " "
        linea: str = linea + celda             #unimos las coordenadas de las filas con las celdas
    print(linea)

#aqui vamos a programar  

estado: str = "turno_blancas"

while estado != "salir":
    if estado == "turno_blancas":
        print("turno de las blancas")
        casilla: str = input("Casilla a consultar (o 'salir' para terminar): ")
        if casilla == "salir":
            estado == "salir"







