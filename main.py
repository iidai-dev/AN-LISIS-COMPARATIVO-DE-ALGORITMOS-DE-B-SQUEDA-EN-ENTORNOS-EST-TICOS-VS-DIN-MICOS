import time
import heapq
import random
from collections import deque

# Mapa
grid = [
    [0,0,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0],
    [1,0,0,0,0],
    [0,0,1,0,0]
]

inicio = (0,0)
meta = (4,4)

filas = len(grid)
columnas = len(grid[0])

movimientos = [(1,0),(-1,0),(0,1),(0,-1)]


def vecinos(nodo):
    x,y = nodo
    resultado = []
    for dx,dy in movimientos:
        nx,ny = x+dx,y+dy
        if 0 <= nx < filas and 0 <= ny < columnas and grid[nx][ny] == 0:
            resultado.append((nx,ny))
    return resultado


# ---------------- DFS ----------------
def dfs():
    stack = [(inicio,[inicio])]
    visitados = set()

    while stack:
        nodo,camino = stack.pop()

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in vecinos(nodo):
                stack.append((vecino,camino+[vecino]))

    return None


# ---------------- BFS ----------------
def bfs():
    cola = deque([(inicio,[inicio])])
    visitados = set()

    while cola:
        nodo,camino = cola.popleft()

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in vecinos(nodo):
                cola.append((vecino,camino+[vecino]))

    return None


# ---------------- A* ----------------
def heuristica(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star():
    heap = [(0,inicio,[inicio])]
    visitados = set()

    while heap:
        costo,nodo,camino = heapq.heappop(heap)

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in vecinos(nodo):
                prioridad = len(camino) + heuristica(vecino,meta)
                heapq.heappush(heap,(prioridad,vecino,camino+[vecino]))

    return None


# ---------------- Algoritmo Genético ----------------
def genetic():
    mejor_camino = None

    for _ in range(100):
        camino = [inicio]
        actual = inicio

        for _ in range(20):
            posibles = vecinos(actual)

            if not posibles:
                break

            actual = random.choice(posibles)
            camino.append(actual)

            if actual == meta:
                return camino

        if mejor_camino is None or len(camino) < len(mejor_camino):
            mejor_camino = camino

    return mejor_camino


# ---------------- Medición ----------------
algoritmos = {
    "DFS": dfs,
    "BFS": bfs,
    "A*": a_star,
    "Genético": genetic
}

for nombre, algoritmo in algoritmos.items():
    inicio_tiempo = time.time()
    ruta = algoritmo()
    fin_tiempo = time.time()

    print(f"\nAlgoritmo: {nombre}")
    print("Ruta encontrada:", ruta)
    print("Longitud:", len(ruta) if ruta else "No encontrada")
    print("Tiempo:", round(fin_tiempo - inicio_tiempo,6), "segundos")