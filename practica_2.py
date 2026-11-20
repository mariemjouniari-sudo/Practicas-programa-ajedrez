#practica 2

#para ael archivo .txt
import os
#para el archivo .csv
import csv

# CLASES
class Pieza:
    """Una pieza de ajedrez."""
    def __init__(self, color: str, simbolo: str, nombre: str) -> None:
        self.color: str = color
        self.simbolo: str = simbolo
        self.nombre: str = nombre

    def __str__(self) -> str:
        """Texto que se muestra al hacer print del objeto."""
        return self.nombre + " " + self.color

    def es_del_color(self, color: str) -> bool:
        """Devuelve True si la pieza es del color indicado."""
        return self.color == color

    # metodo para comprobar movimientos (es_movimiento_valido)
    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int],   #ponemos las comillas en "Tablero" porque la clase tablero aun no está definida
                             destino: tuple[int, int]) -> bool:
        """Cada tipo de pieza redefine este método con sus reglas"""
        return False

class Torre(Pieza):
    """La subclase de pieza torre"""
    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo: str = "♖"
        else:
            simbolo: str = "♜"
        super().__init__(color, simbolo, "torre")

    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int],
                             destino: tuple[int, int]) -> bool:
        """En línea recta (fila o columna) y sin piezas en medio."""
        if origen[0] != destino[0] and origen[1] != destino[1]:       # el movimiento es valido solo si fila o columna de origen y destino son iguales (va en recto(horizontal y vertical))
            return False
        return tablero.camino_libre(origen, destino)             # la torre no puede saltar pieza, así que comprobamos si el camino está libre
          


class Alfil(Pieza):
    """La subclase de pieza alfil"""
    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo: str = "♗"
        else:
            simbolo: str = "♝"
        super().__init__(color, simbolo, "alfil")

    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int], 
                             destino: tuple[int, int]) -> bool:
        """En diagonal: se avanza lo mismo en filas que en columnas."""
        dif_fila: int = abs(destino[0] - origen[0])
        dif_columna: int = abs(destino[1] - origen[1])
        if dif_fila != dif_columna:
            return False
        return tablero.camino_libre(origen, destino)        #hay que comprobar si hay alguna pieza de origen a destino


class Caballo(Pieza):
    """La subclase de pieza caballo"""
    def __init__(self, color: str) -> None:
            if color == "blanca":
                simbolo: str = "♘"
            else:
                simbolo: str = "♞"
            super().__init__(color, simbolo, "caballo")

    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int], 
                                 destino: tuple[int, int]) -> bool:
        """En L: se mueve en forma de L."""
        dif_fila: int = abs(destino[0] - origen[0])
        dif_columna: int = abs(destino[1] - origen[1])
        return (dif_fila == 2 and dif_columna == 1) or (dif_fila == 1 and dif_columna == 2) # para que sea movimiento en L, solo hay dos opciones:
                                                                                            # que la avanze en dos filas y una columna (L vertical)
                                                                                            # que avanze en una fila y dos columnas (L horizontal)


class Dama(Pieza):
    """La subclase de pieza dama"""
    def __init__(self, color: str) -> None:
                if color == "blanca":
                    simbolo: str = "♕"
                else:
                    simbolo: str = "♛"
                super().__init__(color, simbolo, "dama")

    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int], 
                                 destino: tuple[int, int]) -> bool:
        """movimiento torre o alfil (en recto o en diagonal)"""
        dif_fila: int = abs(destino[0] - origen[0])             # hacemos lo mismo que hemos hecho con torre y alfíl
        dif_columna: int = abs(destino[1] - origen[1])
        en_recta: bool = dif_fila == 0 or dif_columna == 0
        en_diagonal: bool = dif_fila == dif_columna
        if not en_recta and not en_diagonal:
            return False
        return tablero.camino_libre(origen, destino) 



class Rey(Pieza):
    """la subclase de pieza rey"""
    def __init__(self, color: str) -> None:
                     if color == "blanca":
                         simbolo: str = "♔"
                     else:
                         simbolo: str = "♚"
                     super().__init__(color, simbolo, "rey")

    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int], 
                                     destino: tuple[int, int]) -> bool:
        """movimiento en cuadrado"""
        dif_fila: int = abs(destino[0] - origen[0])     # hacemos la diferencia entre la fila del origen y la del destino
        dif_columna: int = abs(destino[1] - origen[1])  # lo mismo aquí pero con las columnas
        return max(dif_fila, dif_columna) == 1          # la diferencia máxima tiene que ser uno, ya que se mueve por el cuadrado alrededor suyo y solo puede avanzar en uno (no puede avanzar dos casillas a la vez por ejemplo)
     


class Peon(Pieza):
    """La subclase de pieza peon"""
    def __init__(self, color: str) -> None:
                     if color == "blanca":
                         simbolo: str = "♙"
                     else:
                         simbolo: str = "♟"
                     super().__init__(color, simbolo, "peon")

    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int], 
                                     destino: tuple[int, int]) -> bool:
                """movimiento avanzando en 1 (el primer movimiento 2) y en diagonal en uno solo si hay pieza rival"""
                #hay que distingir entre peones blancos y peones negros, 
                #ya que el origen inicial es diferente y avanzan de arriba a abajo o de abajo a ariba dependiendo del color
                if self.color == "blanca":
                     direccion: int = 1
                     fila_inicial: int = 1
                else:
                     direccion: int = -1 
                     fila_inicial: int = 6

                # la variable avance es para comprobar con la diferencia de la fila origen y destino si avanza en 1 o en 2
                avance: int = destino[0] - origen[0]
                dif_columna: int = abs(destino[1] - origen[1])          #para saber si se mueve en diagonal o en recto
                pieza_destino: Pieza | None = tablero.obtener(destino[0], destino[1])  #para comprobar si en la casilla destino hay pieza o está vacía

                if dif_columna == 0:
                     #avanza recto, el destino debe estar vacío
                    if avance == direccion:
                        return pieza_destino is None
                    if avance == 2 * direccion and origen[0] == fila_inicial:           #comprobamos si el movimiento en dos se hace cuando el peón está en la fila inicial
                        return pieza_destino is None and tablero.camino_libre(origen, destino)      #comprobamos si está libre la casilla destino con el método camino libre
                    return False

                if dif_columna == 1 and avance == direccion:
                    # Captura en diagonal: solo si hay una pieza rival
                    return pieza_destino is not None and pieza_destino.color != self.color      #comprobamos si hay pieza y que no sea del mismo color

                return False



class Tablero:
    """Tablero de 8x8 donde se colocan las piezas de ajedrez y se mueven"""
    def __init__(self) -> None:
        self.casillas: list[list[Pieza | None]] = []
        for fila in range(8):
            fila_vacia: list[Pieza | None] = [None] * 8
            self.casillas.append(fila_vacia)
        self.colocar_posicion_inicial()


    def colocar(self, pieza: Pieza, fila: int, columna: int) -> None:
            """Pone una pieza en una casilla."""
            self.casillas[fila][columna] = pieza


    def colocar_posicion_inicial(self) -> None:
        """Rellana el tablero con la posición inicial estandar de ajedrez"""
        #fila de piezas, de columna a (0) a h (7)
        for columna in range(8):
            if columna == 0 or columna == 7:   # aquí colocamos en cada fila (blancas: fila 0 y negras: fila 7) dos torres, una en la columna 0 y otra en la 7
                self.colocar(Torre("blanca"), 0, columna)
                self.colocar(Torre("negra"), 7, columna)
            elif columna == 1 or columna == 6:  # lo mismo que con la torre, colocamos dos caballos en la fila de las negras y 2 en las blancas
                self.colocar(Caballo("blanca"), 0, columna)
                self.colocar(Caballo("negra"), 7, columna)
            elif columna == 2 or columna == 5:  # el mismo método que con la torre y el caballo
                self.colocar(Alfil("blanca"), 0, columna)
                self.colocar(Alfil("negra"), 7, columna)
            elif columna == 3:                  # aqui solo necesitamos colocar una dama en cada fila, se coloca en la columna 3 (posiciones [0,3] y [7,3])
                self.colocar(Dama("blanca"), 0, columna)
                self.colocar(Dama("negra"), 7, columna)
            else:
                self.colocar(Rey("blanca"), 0, columna)
                self.colocar(Rey("negra"), 7, columna)

            # Ahora solo nos quedan los peones, rellenamos toda la fila 1 con peones blancos y la fila 6 con peones negros 8 veces, que son el num de columnas 
            self.colocar(Peon("blanca"), 1, columna)
            self.colocar(Peon("negra"), 6, columna)

            #hemos rellenado las filas 0, 1, 6 y 7. las filas de 2-5 quedan vacías

    def obtener(self, fila: int, columna: int) -> Pieza | None:
        """Devuelve la pieza de una casilla, o None si está vacía"""
        return self.casillas[fila][columna]


    #este método sirve para torre, alfíl y dama.
    #Avanza casilla a casilla desde el origen 
    #y falla si encuentra una pieza antes de llegar al destino.
    def camino_libre(self, origen: tuple[int, int],
                     destino: tuple[int, int]) -> bool:
        """True si no hay piezas entre origen y destino (ambos excluidos)."""
        paso_fila: int = 0
        if destino[0] > origen[0]:
            paso_fila: int = 1
        elif destino[0] < origen[0]:
            paso_fila: int = -1
        paso_columna: int = 0
        if destino[1] > origen[1]:
            paso_columna: int = 1
        elif destino[1] < origen[1]:
            paso_columna: int = -1

        fila: int = origen[0] + paso_fila
        columna: int = origen[1] + paso_columna
        while (fila, columna) != destino:               # el bucle va avanzando de uno en uno comprobando si hay alguna pieza hasta llegar al destino
            if self.casillas[fila][columna] is not None:
                return False
            fila: int = fila + paso_fila
            columna: int = columna + paso_columna
        return True

         
    def imprimir_tablero(self) -> None:
        """Imprime el tablero (la fila 8 arriba)"""
        print("  a b c d e f g h")      #imprimimos primero el cabecero (índices de columnas)
        for fila in range(7, -1, -1):   # va de 7 a 0, va disminuyendo en uno
            linea: str = str(fila + 1)      #así empieza de 8 y acaba en 1
            for columna in range(8):
                pieza: Pieza | None = self.casillas[fila][columna]
                if pieza is None:
                    linea: str = linea + " ."
                else:
                    linea: str = linea + " " + pieza.simbolo
            print(linea)

    def mover_pieza(self, origen: tuple[int, int], destino: tuple[int, int]) ->   None:
         """Mueve la pieza de origen a destino (ya validado)"""
         pieza: Pieza | None = self.casillas[origen[0]][origen[1]]  # definimos la pieza de origen
         self.casillas[destino[0]][destino[1]] = pieza              # sustuimos la casilla destino por la pieza
         self.casillas[origen[0]][origen[1]] = None                 # vaciamos la casilla origen
         # Coronación: cuando un peón llega a la última fila, se convierte automaticamente en Dama del mismo color.
         # el peón blanco cuando lleha a fila 8 y el peón negro cundo llega a fila 1.
         if pieza.nombre == "peon":
              if (pieza.color == "blanca" and destino[0] == 7) or (pieza.color == "negra" and destino[0] == 0):
                   self.casillas[destino[0]][destino[1]] = Dama(pieza.color)


    def validar_pieza(self, origen: tuple[int, int], destino: tuple[int, int], color: str) -> str:
        """Devuelve el motivo de rachazo de un movimiento, o un return vacío si el movimiento es válido"""
        
        if origen == destino:
            return "El origen y el destino son la misma casilla."

        
        pieza_origen: Pieza | None = self.obtener(origen[0], origen[1])

        if pieza_origen is None:
            return "No hay ninguna pieza en la casilla de origen."

        if pieza_origen.color != color:
            if color == "blanca":
                return "Esa pieza no es tuya: es el turno de las blancas."
            else:
                return "Esa pieza no es tuya: es el turno de las negras."

            
        pieza_destino: Pieza | None = self.obtener(destino[0], destino[1])

        if pieza_destino is not None and pieza_destino.color == color:
            return "La casilla de destino está ocupada por una pieza propia."

        if not pieza_origen.es_movimiento_valido(self, origen, destino):
            return "Movimiento no permitido para esta pieza (" + pieza_origen.nombre + ")."

        # Aquí coprobamos si el movimiento deja el rey en jaque
        # Lo haremos simulando el movimiento (para no coronar)
        self.casillas[destino[0]][destino[1]] = pieza_origen
        self.casillas[origen[0]][origen[1]] = None
        en_jaque: bool = self.esta_en_jaque(color)
        # Restauramos siempre, haya jaque o no
        self.casillas[origen[0]][origen[1]] = pieza_origen
        self.casillas[destino[0]][destino[1]] = pieza_destino

        if en_jaque:
            return "Ese movimiento deja a tu propio rey en jaque"
        return ""

    def buscar_rey(self, color: str) -> tuple[int, int]:
        """recorre las 64 casillas hasta que encuentre a la posicíon del rey del color indicado"""
        for fila in range(8):
            for columna in range(8):
                casilla: Pieza | None = self.casillas[fila][columna]
                if casilla is not None and casilla.nombre == "rey" and casilla.color == color:
                    return (fila, columna)
        return (-1, -1)     # es un valor de reserva por si no encuentra el rey, porque la función promete una tupla. Se usa para evitar incidencias.

    # este método lo utilizaremos sobretodo para ver si e rey está atacado o no (Jaque)
    def casilla_atacada(self, color_atacante: str, casilla: tuple[int, int]) -> bool:
        """Comprueba si la casilla destino puede estar atacada por alguna pieza rival"""
        for fila in range(8):
            for columna in range(8):
                pieza: Pieza | None = self.casillas[fila][columna]
                if pieza is not None and pieza.color == color_atacante:
                    if pieza.es_movimiento_valido(self, (fila, columna), casilla):
                         return True
        return False

    #aquí combinamos los dos métodos de antes (buscar_rey y casilla_atacada) para ver si el rey está en jaque
    def esta_en_jaque(self, color: str) -> bool:
        """busca dónde está el rey y pregunta si esta casilla está atacada por el color contrario"""
        casilla_rey: tuple[int, int] = self.buscar_rey(color)
        if color == "blanca":
             contrario: str = "negra"
        else:
             contrario: str = "blanca"
        return self.casilla_atacada(contrario, casilla_rey)
    

    def hay_movimientos_validos(self, color: str) -> bool:
        """devuelve True si ese color tiene al menos un movimiento válido"""
        for fila_origen in range(8):
            for columna_origen in range(8):
                pieza: Pieza | None = self.casillas[fila_origen][columna_origen]
                if pieza is None or pieza.color != color:       # excluimos las casillas vacias y las de color contrario
                    continue
                for fila_destino in range(8):
                     for columna_destino in range(8):
                        origen: tuple[int, int] = (fila_origen, columna_origen)
                        destino: tuple[int, int] = (fila_destino, columna_destino)
                        if self.validar_pieza(origen, destino, color) == "":
                            return True
        return False
                     

                
                       
        


# FUNCIONES

def es_casilla_valida(casilla: str) -> bool:
    """comprueba si el formato de la casilla es válido (ej: e2)"""
    if (len(casilla)) == 2 and casilla[0] in "abcdefgh" and casilla[1] in "12345678":
        resultado: bool = True
    else:
        resultado: bool = False
    return resultado


def convertir_casilla(casilla: str) -> tuple[int, int]:
    """Convierte la casilla introducida en una tupla (fila, columna) con índices de 0 a 7"""
    columna: int = "abcdefgh".find(casilla[0])      #la funcion find devuelve la posición en la caden ade texto, que es exactamente la posición de la columna.
    fila: int = int(casilla[1]) - 1
    return (fila, columna)


def leer_movimiento(movimiento: str) -> list[str]:
     """Devuelve [origen, destino] ya limpios, o devuelve una lista vacía si la casilla no es valida"""
     partes: list[str] = movimiento.strip().lower().split()
     if len(partes) == 2 and es_casilla_valida(partes[0]) and es_casilla_valida(partes[1]):
          return partes
     else:
          return []


def color_contrario(color: str) -> str:
    """Devuelve 'negra' si el color es 'blanca', y 'blanca' en caso contrario."""
    if color == "blanca":
        return "negra"
    return "blanca"



def guardar_historial(movimientos: list[str], ruta: str) -> None:
    """Guarda la lista de mivimientos en un fichero, uno por línea"""
    with open(ruta, "w") as fichero:
        for movimiento in movimientos:
            fichero.write(movimiento + "\n")




def cargar_historial(ruta: str) -> list[str]:
    """Carga el historial de movimientos desde un fichero, si existe"""
    movimientos: list[str] = []
    if os.path.exists(ruta) :
        with open(ruta, "r") as fichero:
            for linea in fichero:
                movimiento: str = linea.strip()
                if movimiento != "":
                    movimientos: list[str] = movimientos + [movimiento]
    return movimientos


def exportar_historial_csv(movimientos: list[str], ruta: str) -> None:
    """Exporta el historial con numero, turno, origen y destino a un CSV."""
    with open(ruta, "w", newline="") as fichero:
        escritor = csv.writer(fichero)
        escritor.writerow(["numero", "turno", "origen", "destino"])
        for indice in range(len(movimientos)):
            partes: list[str] = movimientos[indice].split()     # aqui separamos el origen de destino en movimientos con split()
            numero: int = indice + 1            # aquí ponemos más 1 para que la primera linea ponga 1 y no 0.
            if indice % 2 == 0:                 # para saber si es el turno de blancas o negras, comprobamos si el índice es par o impar
                turno: str = "blancas"          # si el indice es par, es el turno de blancas
            else:
                turno: str = "negras"           # si el indice es impar, es el turno de negras
            escritor.writerow([numero, turno, partes[0], partes[1]])

# vamos a utilizar esta función para aplicar los movimientos de una partida cargada, porque no poedemos con la función jugar_turno ya que pide un input
def aplicar_movimiento(tablero: Tablero, texto: str, color: str) -> str:
    """Valida y aplica un movimiento escrito con texto. Devuelve el motivo del rechazo, o un texto vacio si se ha aplicado"""
    partes: list[str] = leer_movimiento(texto)
    if partes == []:
        return "Formato no válido"
    origen: tuple[int, int] = convertir_casilla(partes[0])
    destino: tuple[int, int] = convertir_casilla(partes[1])
    motivo: str = tablero.validar_pieza(origen, destino, color)
    if motivo == "":
        tablero.mover_pieza(origen, destino)
    return motivo


def jugar_turno(tablero: Tablero, color: str, historial: list[str]) -> str:
    """Procesa un turno. Devuelve 'aplicado', 'rechazado' o 'salir'."""
    if color == "blanca":
        print("turno de las BLANCAS")
    else:
        print("turno de las NEGRAS")
    
    movimiento: str = input("Movimiento, 'exportar' o 'salir': ")
    orden: str = movimiento.strip().lower()
    if orden == "salir":
        return "salir"
    if orden == "exportar":
        exportar_historial_csv(historial, "partida.csv")
        print("Historial exportado a partida.csv.")
        return "rechazado"          # el turno no cambia

    
    partes: list[str] = leer_movimiento(movimiento)
    if partes == []:
        print("casilla no válida. Escribe origen y destino, por ejemplo: e2 e4")
        return "rechazado"

    origen: tuple[int, int] = convertir_casilla(partes[0])
    destino: tuple[int, int] = convertir_casilla(partes[1])

    motivo: str = tablero.validar_pieza(origen, destino, color)
    if motivo != "":
        print("Movimiento rechazado: ", motivo)
        return "rechazado"

    tablero.mover_pieza(origen, destino)
    historial.append(partes[0] + " " + partes[1])
    guardar_historial(historial, "partida.txt")
    print("Movimiento aplicado:", partes[0], "->", partes[1])
    tablero.imprimir_tablero()

    #Aquí comprobamos Jaque mate y rey ahogado
    contrario: str = color_contrario(color)
    en_jaque: bool = tablero.esta_en_jaque(contrario)
    if not tablero.hay_movimientos_validos(contrario):      #primero comprobamos si existe alguna pieza que puede moverse a esa casilla
        if en_jaque:                                        #si no hay mas movimientos y el rey está en jaque, es jaque mate y pierden los contrarios
            print("Jaque mate. Ganan las " + color + "s.")
        else:                                               #si no hay movimientos pero el rey no está en jaque, es rey ahogado y acaba la partida
            print("rey ahogado, tablas.")
        return "fin"
    if en_jaque:                                            #aquí se comprueba si está en jaque el color contrario después del movimiento del otro color
         print("Jaque a las " + contrario + "s.")
    return "aplicado"

    




# MAQUINA DE ESTADOS

# Definimos las variables tablero, historial, y estado
tablero: Tablero = Tablero()
historial: list[str] = []
estado: str = "turno_blancas"


#Antes de comenzar la partida, comprobamos si ya existe un fichero de una partida antigua y preguntamos si se quiere seguir o no.
ruta: str = "partida.txt"
if os.path.exists(ruta):
    respuesta: str = input("Quiere continuar la partida guardada? (s/n) ")
    if respuesta.lower().strip() == "s":
        movimientos: list[str] = cargar_historial(ruta)

        tablero_cargado: Tablero = Tablero()    # tablero nuevo solo para probar si los movimientos guardados son válidos o no y otras comprobaciones
        valido: bool = True
        for indice in range(len(movimientos)):
            if indice % 2 == 0:
                color: str = "blanca"
            else:
                color: str = "negra"
            resultado: str = aplicar_movimiento(tablero_cargado,movimientos[indice], color)
            if resultado != "":
                valido: bool = False
                break

        if not valido:
            print("El archivo guardado no es válido. Se empieza una nueva partida")
        else:
            if len(movimientos) % 2 == 0:
                turno: str = "turno_blancas"
                color_turno: str = "blanca"
            else:
                turno: str = "turno_negras"
                color_turno: str = "negra"
            if not tablero_cargado.hay_movimientos_validos(color_turno):
                print("La partida guardada ya había terninado. Se empieza una partida nueva.")
            else:
                tablero: Tablero = tablero_cargado      # Ahora que hemos comprobado todo y está bien, lo sustituimos por las variables principales
                historial: list[str] = movimientos
                estado: str = turno

#Imprimimos el tablero con las posicione iniciales
tablero.imprimir_tablero()  


while estado != "fin_partida":
    if estado == "turno_blancas":
        resultado: str = jugar_turno(tablero, "blanca", historial)
        if resultado == "aplicado":
            estado: str = "turno_negras"
        elif resultado == "salir":
            estado: str = "fin_partida"
        elif resultado == "fin":
            estado: str = "fin_partida"
    elif estado == "turno_negras":
        resultado: str = jugar_turno(tablero, "negra", historial)
        if resultado == "aplicado":
            estado: str = "turno_blancas"
        elif resultado == "salir":
            estado: str = "fin_partida"
        elif resultado == "fin":
             estado: str = "fin_partida"

print("FIN DE LA PARTIDA")