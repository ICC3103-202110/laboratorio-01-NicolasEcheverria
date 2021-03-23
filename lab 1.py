# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 11:46:02 2021

@author: nicolas
"""
from numpy import *

lista_usuarios={}
nombres_jugadores=[]
def usuarios_y_puntuaciones(diccionario,lista):
    print("escriba nombre de jugador")
    nombre=input()
    lista.append(nombre)
    diccionario [nombre]=0
    print("escriba nombre de segundo jugador")
    nombre=input()
    lista.append(nombre)
    diccionario [nombre]=0
    return [diccionario,lista]

tabla= usuarios_y_puntuaciones(lista_usuarios,nombres_jugadores) #tabla donde se grardaran los nombres y puntuaciones de usuarios
lista_usuarios=tabla[0]
print(tabla)
nombres_jugadores=tabla[1]


print("cuantos pares de cartas debe haber?")
pares_de_cartas=int(input()) #pares de cartas que debe haber en el juego

tablero_y_numeros=[]

def tablero (numero_de_pares):
    lista=[]
    set1=[]
    tablero_cartas=[]
    for i in range(numero_de_pares):
        set1.append(i+1)
        set1.append(i+1)
    random.shuffle(set1)
    
    tablero_cartas=[set1[0:int(len(set1)/2)],set1[int(len(set1)/2):int(len(set1))]]
    
    mat_tablero_cartas=matrix(tablero_cartas)
    
    

    lista.append(mat_tablero_cartas) #insertamos los pares de numeros en esta lista en forma de matriz de dimensiones (2,numero de pares)
  
    
    
    tablero_coordenadas=[[],[]]
    for i in range(numero_de_pares):
        tablero_coordenadas[0].append(0)
        tablero_coordenadas[1].append(0)
    
    
    
    
    
    for fila in range(len(tablero_coordenadas)):
        for columna in range(len(tablero_coordenadas[fila])):
            tablero_coordenadas[fila][columna]=(fila,columna)
    
    
    

    lista.append(tablero_coordenadas)
            
    return lista

coord_y_numeros= tablero(pares_de_cartas)

print(coord_y_numeros)


def juego(tablero_coor,tablero_num,diccionario,nombres):
    print('es el turno de: ',nombres[0],' , puntuacion actual:',diccionario[nombres[0]],'\n')
    
    print(tablero_coor)
    
    return 1

x= juego(coord_y_numeros[1],coord_y_numeros[0],lista_usuarios,nombres_jugadores)
    

    
    
    









































