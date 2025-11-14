import random

def ha_comido_serpiente(serpiente: list[tuple[int, int]], posicion_comida: tuple[int, int]) -> bool:
    '''
    Comprueba si la cabeza de la serpiente está en la misma posición que la comida.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    posicion_comida: Tupla representando la posición de la comida (columna, fila).

    Devuelve:
    True si la cabeza de la serpiente está en la misma posición que la comida, False en caso contrario.
    '''
    if serpiente[0] == posicion_comida:
        return True
    else:
        return False

def comprueba_choque(serpiente: list[tuple[int, int]], paredes: list[list[tuple[int, int]]]) -> bool:
    '''
    Comprueba si la serpiente se ha chocado consigo misma o con las paredes. Tenga en cuenta
    que la serpiente avanza siempre por su cabeza, que está situada en la 
    primera posición de la lista.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de cada segmento de la serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.

    Devuelve:
    True si la serpiente se ha chocado consigo misma o con las paredes, False en caso contrario.
    '''
    for i in range(len(paredes)):
        for j in range(len(paredes[i])):
            if paredes[i][j] == serpiente[0]:
                return True
    for i in range(1,len(serpiente)):
        if serpiente[0] == serpiente[i]:
            return True
    else:
        return False    

    

def crece_serpiente(serpiente: list[tuple[int, int]]) -> None:
    '''
    Hace crecer la serpiente añadiendo duplicando la posición de la cola

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    '''
    serpiente.append(serpiente[-1])

def genera_comida_aleatoria(serpiente: list[tuple[int, int]], paredes: list[list[tuple[int, int]]], filas: int, columnas: int) -> tuple[int, int]:
    '''
    Genera una posición aleatoria para la comida que no esté en la misma posición que la serpiente o las paredes.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.
    filas: Número de filas en el tablero de juego.
    columnas: Número de columnas en el tablero de juego.

    Devuelve:
    Posición aleatoria para la comida (columna, fila).
    '''
    posicion_xy_valida = False
    while posicion_xy_valida == False:
        x = random.randint(0,columnas-1)
        y = random.randint(0, filas-1)
        tuple = (x,y)
        for i in range(len(paredes)):
            if (tuple not in serpiente) and (tuple not in paredes[i]):
                posicion_xy_valida = True
            else:
                posicion_xy_valida = False
    return tuple                
    

def mueve_serpiente(serpiente: list[tuple[int, int]], direccion: str, filas: int, columnas: int) -> None:
    '''
    Mueve la serpiente en el tablero según la dirección dada. El tablero es circular, lo que significa
    que si la serpiente se sale por la derecha, debe aparecer por la izquierda, y viceversa (y lo 
    mismo si se sale por arriba o por abajo).

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    direccion: Dirección en la que se debe mover la serpiente ('Left', 'Right', 'Down', 'Up').
    filas: Número de filas en el tablero de juego.
    columnas: Número de columnas en el tablero de juego.
    '''
    x, y = serpiente[0]
    f = filas
    c = columnas
    if direccion == "Left" :
        cabeza_izquierda = ((x-1)%c, y) 
        serpiente.insert(0, cabeza_izquierda)
        serpiente.pop() 
        return serpiente
    elif direccion == "Right":
        cabeza_derecha = ((x+1)%c, y)      
        serpiente.insert(0, cabeza_derecha)
        serpiente.pop()
        return serpiente
    elif direccion == "Up":
        cabeza_arriba = (x, (y-1)%f)
        serpiente.insert(0, cabeza_arriba)
        serpiente.pop()
        return serpiente
    elif direccion == "Down":
        cabeza_abajo = (x, (y+1)%f) 
        serpiente.insert( 0, cabeza_abajo)
        serpiente.pop()   
        return serpiente
    else:
        return None






