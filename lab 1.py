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
lista_usuarios=tabla[0]##diccionario con jugadores
print(tabla[0])#diccionario con jugadores
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
    
    
    
    

    lista.append(tablero_cartas) #insertamos los pares de numeros en esta lista
  
    
    
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
numeros=coord_y_numeros[0]



def juego(tablero_coor,tablero_num,diccionario,nombres,turno):
    
    print('\n','\n','es el turno de: ',nombres[turno],' , puntuacion actual:',diccionario[nombres[turno]],'\n')
    
    print(tablero_coor[0],'\n',tablero_coor[1])
    
    print('\n',"escriba la coordenada de la carta que quiera dar vuelta de forma 'a,b' ")
    
    

    coordenada_ingresada1=input()
    
    coordenada_ingresada1=coordenada_ingresada1.split(',')
    
    fila_coordenada_ingresada1=int(coordenada_ingresada1[0])
    columna_coordenada_ingresada1=int(coordenada_ingresada1[1])
    
    c1=tablero_coor[fila_coordenada_ingresada1][columna_coordenada_ingresada1]
    tablero_coor[fila_coordenada_ingresada1][columna_coordenada_ingresada1]=str(tablero_num[fila_coordenada_ingresada1][columna_coordenada_ingresada1])
    r1=tablero_coor[fila_coordenada_ingresada1][columna_coordenada_ingresada1]
    
    
    
    ###############parte 1 turno################
    print('\n','\n','es el turno de: ',nombres[turno],' , puntuacion actual:',diccionario[nombres[turno]],'\n')
    
    print(tablero_coor[0],'\n',tablero_coor[1])
    
    print('\n',"escriba la segunda coordenada de la carta que quiera dar vuelta de forma 'a,b' ")    
    
    coordenada_ingresada2=input()
    coordenada_ingresada2=coordenada_ingresada2.split(',')
    while coordenada_ingresada2==coordenada_ingresada1:
        print("coordenada repetida, escriba una que no este seleccionada")
        coordenada_ingresada2=input()
        coordenada_ingresada2=coordenada_ingresada2.split(',')
                              #
        
        
    
    
    
    
    
    fila_coordenada_ingresada2=int(coordenada_ingresada2[0])
    columna_coordenada_ingresada2=int(coordenada_ingresada2[1])
    c2=tablero_coor[fila_coordenada_ingresada2][columna_coordenada_ingresada2]
    tablero_coor[fila_coordenada_ingresada2][columna_coordenada_ingresada2]=str(tablero_num[fila_coordenada_ingresada2][columna_coordenada_ingresada2])
    r2=tablero_coor[fila_coordenada_ingresada2][columna_coordenada_ingresada2]
    
    print('\n',tablero_coor[0],'\n',tablero_coor[1],'\n')
            ###########parte 2  turno#######
    
    
    
    
    if r1==r2:
        if len(tablero_coor[0])==0:
            if len(tablero_coor[1])==2:
                diccionario[nombres[turno]]+=1
                print('felicidades, has encontrado el par de ',r1,' has terminado el juego',' , puntuaciones finales: ',diccionario,'\n')
                if r1 in tablero_coor[0]==False:
                    tablero_coor[1].remove(r1)
                    tablero_coor[1].remove(r1)
                elif r1 in tablero_coor[1]==False:
                    tablero_coor[0].remove(r1)
                    tablero_coor[0].remove(r1)
                else:
                    tablero_coor[1].remove(r1)
                    tablero_coor[0].remove(r1)
                    
                    
                    
                if diccionario[nombres[0]]>diccionario[nombres[1]]:
                    print('gana jugador',diccionario[nombres[0]])
                    
                    return 1
                
                elif diccionario[nombres[0]]<diccionario[nombres[1]]:
                    print('gana jugador ',diccionario[nombres[1]])
                    
                    return 1
                    
                elif diccionario[nombres[0]]==diccionario[nombres[1]]:
                    print('es un empate')
                    
                    return 1
                    

        
            
        if len(tablero_coor[1])==0:
            if len(tablero_coor[0])==2:
                diccionario[nombres[turno]]+=1
                print('felicidades, has encontrado el par de ',r1,' has terminado el juego',' , puntuaciones finales: ',diccionario,'\n')
                if r1 in tablero_coor[0]==False:
                    tablero_coor[1].remove(r1)
                    tablero_coor[1].remove(r1)
                elif r1 in tablero_coor[1]==False:
                    tablero_coor[0].remove(r1)
                    tablero_coor[0].remove(r1)
                else:
                    tablero_coor[1].remove(r1)
                    tablero_coor[0].remove(r1)
                    
                    
                    
                if diccionario[nombres[0]]>diccionario[nombres[1]]:
                    print('gana jugador',diccionario[nombres[0]])
                    
                    return 1
                    
                elif diccionario[nombres[0]]<diccionario[nombres[1]]:
                    print('gana jugador ',diccionario[nombres[1]])
                    
                    return 1
                    
                elif diccionario[nombres[0]]==diccionario[nombres[1]]:
                    print('es un empate')
                
                    return 1
                
        else:
            diccionario[nombres[turno]]+=1
            print('felicidades, has encontrado el par de ',r1,' ganas un turno extra',nombres[turno],', puntuacion actual:',diccionario[nombres[turno]],'\n')
            if r1 in tablero_coor[0]==False:
                tablero_coor[1].remove(r1)
                tablero_coor[1].remove(r1)
            elif r1 in tablero_coor[1]==False:
                tablero_coor[0].remove(r1)
                tablero_coor[0].remove(r1)
            else:
                tablero_coor[1].remove(r1)
                tablero_coor[0].remove(r1)
                print('\n',tablero_coor[0],'\n',tablero_coor[1],'\n')
        
        x=juego(coord_y_numeros[1],numeros,lista_usuarios,nombres_jugadores,turno)



    else:
        
        print("no haz  encontrado un par,termina tu turno")
          
        tablero_coor[fila_coordenada_ingresada1][columna_coordenada_ingresada1]= c1            
        tablero_coor[fila_coordenada_ingresada2][columna_coordenada_ingresada2]= c2
           
         
        
        if turno==0:
            turno=1
        elif turno==1:
            turno=0
            
            
        x=juego(coord_y_numeros[1],numeros,lista_usuarios,nombres_jugadores,turno)
            
            
    
    return 1

x= juego(coord_y_numeros[1],numeros,lista_usuarios,nombres_jugadores,0)
    

    
    
    









































