# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 11:46:02 2021

@author: nicolas
"""
from numpy import *


def users_and_points(dictionary,listt):
    
    print("write first player's name")
    name=input()
    listt.append(name)
    dictionary [name]=0
    print("write second player's name")
    name=input()
    listt.append(name)
    dictionary [name]=0
    return [dictionary,listt]





def board (number_of_pairs):
    listt=[]
    set1=[]
    board_cards=[]
    for i in range(number_of_pairs):
        set1.append(i+1)
        set1.append(i+1)
    random.shuffle(set1)
    
    board_cards=[set1[0:int(len(set1)/2)],set1[int(len(set1)/2):int(len(set1))]]
    
    
    
    

    listt.append(board_cards) #insertamos los pares de numeros en esta lista
  
    
    
    board_coordenates=[[],[]]
    for i in range(number_of_pairs):
        board_coordenates[0].append(0)
        board_coordenates[1].append(0)
    
    
    
    
    
    for row in range(len(board_coordenates)):
        for column in range(len(board_coordenates[row])):
            board_coordenates[row][column]=(row,column)
    
    
    

    listt.append(board_coordenates)
            
    return listt


def game(board_coor,board_num,dictionary,names,turn): 
    print('\n','\n','\n',"It's " ,names[turn],"'s , turn, actual score:",dictionary[names[turn]],'\n')#dice de quien es el turno
    
    for fgh in board_coor:#imprime tablero
        print('\n')
        for asd in  fgh:
            print(" ",asd,' ',end='')
    print('\n')
    
    print("write the coordenates of the card you want to turn in the form 'a,b' ")#forma de escribir coordenadas
    
    

    coordenate_entered1=input()
    
    coordenate_entered1=coordenate_entered1.split(',')
    
    
    row_coordenate_entered1=int(coordenate_entered1[0])
    column_coordenate_entered1=int(coordenate_entered1[1])#separo filas y columnas
    
    while ((row_coordenate_entered1,column_coordenate_entered1) in board_coor[0])== False and ((row_coordenate_entered1,column_coordenate_entered1) in board_coor[1])== False:#por si se ponen coordenadas no existentes en el tablero
        print('invalid coordenate, please select one that is present on the board')
        for fgh in board_coor:
            print('\n')
            for asd in  fgh:
                print(" ",asd,' ',end='')
        print('\n')
    
        print("write the coordenates of the card you want to turn in the form 'a,b' ")
    
    

        coordenate_entered1=input()
    
        coordenate_entered1=coordenate_entered1.split(',')
    
    
        row_coordenate_entered1=int(coordenate_entered1[0])
        column_coordenate_entered1=int(coordenate_entered1[1])
    
    
    c1=(int(coordenate_entered1[0]), int(coordenate_entered1[1]))#coordenada respuesta 1
    board_coor[row_coordenate_entered1][board_coor[row_coordenate_entered1].index((row_coordenate_entered1,column_coordenate_entered1))]=str(board_num[row_coordenate_entered1][column_coordenate_entered1])
    
    r1= board_coor[row_coordenate_entered1][board_coor[row_coordenate_entered1].index((str(board_num[row_coordenate_entered1][column_coordenate_entered1])))]#numero de primer input
    
    
    ###############parte 1 turno################
    print('\n','\n')
    
    for fgh in board_coor:#imprime tablero
        print('\n')
        for asd in  fgh:
            print(" ",asd,' ',end='')
    print('\n')
    print("write the second coordenate of the card you want to turn in the form 'a,b' ")    
    
    coordenate_entered2=input()
    coordenate_entered2=coordenate_entered2.split(',')
    while coordenate_entered2==coordenate_entered1:#por si las coordenadas se repiten
        print("you already selectioned this coordenate, please write one that has not been selected")
        coordenate_entered2=input()
        coordenate_entered2=coordenate_entered2.split(',')
                              #
        
        
    
    
    
    
    
    row_coordenate_entered2=int(coordenate_entered2[0])
    column_coordenate_entered2=int(coordenate_entered2[1])
    while ((row_coordenate_entered2,column_coordenate_entered2) in board_coor[0])== False and ((row_coordenate_entered2,column_coordenate_entered2) in board_coor[1])== False:#por si seleccionan coordenadas que no existen
        print('invalid coordenate, please select one that is present on the board')
        for fgh in board_coor:
            print('\n')
            for asd in  fgh:
                print(" ",asd,' ',end='')
        print('\n')
    
        print("write the coordenates of the card you want to turn in the form 'a,b' ")
    
    

        coordenate_entered2=input()
    
        coordenate_entered2=coordenate_entered2.split(',')
    
    
        row_coordenate_entered2=int(coordenate_entered2[0])
        column_coordenate_entered2=int(coordenate_entered2[1])#separa filas y columnas del segundo input
    
    
    
    
    
    
    
    
    
    
    c2=(int(coordenate_entered2[0]), int(coordenate_entered2[1]))#coordenada respuesta 2
    board_coor[row_coordenate_entered2][board_coor[row_coordenate_entered2].index((row_coordenate_entered2,column_coordenate_entered2))]=str(board_num[row_coordenate_entered2][column_coordenate_entered2])
    r2=board_coor[row_coordenate_entered2][board_coor[row_coordenate_entered2].index((str(board_num[row_coordenate_entered2][column_coordenate_entered2])))]#numero respuesta2
    
    for fgh in board_coor:
        print('\n')
        for asd in  fgh:
            print(" ",asd,' ',end='')
    print('.','\n')
            ###########parte 2  turno#######
    
    
    
    
    if r1==r2:
        if len(board_coor[0])<=1:
            if len(board_coor[1])<=2:
                dictionary[names[turn]]+=1
                print("congratulations you've found the pair of ",r1,' the game has ended',' ,final scores: ',dictionary,'\n')
                if (str(r1) in board_coor[0])==False:
                    board_coor[1].remove(str(r1))
                    board_coor[1].remove(str(r1))
                elif (str(r1) in board_coor[1])==False:
                    board_coor[0].remove(str(r1))
                    board_coor[0].remove(str(r1))
                else:
                    board_coor[1].remove(str(r1))
                    board_coor[0].remove(str(r1))
                    
                    
                    
                if dictionary[names[0]]>dictionary[names[1]]:
                    print(names[0]," wins")
                    
                    return 1
                
                elif dictionary[names[0]]<dictionary[names[1]]:
                    print(names[1]," wins")
                    
                    return 1
                    
                elif dictionary[names[0]]==dictionary[names[1]]:
                    print("It's a tie")
                    
                    return 1
                    

        
            
        if len(board_coor[1])<=1:
            if len(board_coor[0])<=2:
                dictionary[names[turn]]+=1
                print("congratulations you've found the pair of ",r1,' the game has ended , final scores:  ',dictionary,'\n')
                if(str( r1) in board_coor[0])==False:
                    board_coor[1].remove(str(r1))
                    board_coor[1].remove(str(r1))
                elif (str(r1) in board_coor[1])==False:
                    board_coor[0].remove(str(r1))
                    board_coor[0].remove(str(r1))
                else:
                    board_coor[1].remove(str(r1))
                    board_coor[0].remove(str(r1))
                    
                    
                    
                if dictionary[names[0]]>dictionary[names[1]]:
                    print(names[0]," Wins")
                    
                    return 1
                    
                elif dictionary[names[0]]<dictionary[names[1]]:
                    print(names[1]," Wins")
                    
                    return 1
                    
                elif dictionary[names[0]]==dictionary[names[1]]:
                    print("It's a tie")
                
                    return 1
                
        else:
            dictionary[names[turn]]+=1
            print('\n',"congratulations, you've foud the pair of ",r1,' you win an extra turn ',names[turn],', actual score: ',dictionary[names[turn]],'\n')
            if (str(r1) in board_coor[0])==False:
                board_coor[1].remove(str(r1))
                board_coor[1].remove(str(r1))
            elif (str(r1) in board_coor[1])==False:
                board_coor[0].remove(str(r1))
                board_coor[0].remove(str(r1))
            else:
                board_coor[1].remove(str(r1))
                
                board_coor[0].remove(str(r1))
                
        
        x=game(coord_and_numbers[1],numbers,list_users,names_players,turn)



    else:
        
        print('\n',"you have not found a pair, your turn is over")
          
        board_coor[row_coordenate_entered1][board_coor[row_coordenate_entered1].index(r1)]= c1            
        board_coor[row_coordenate_entered2][board_coor[row_coordenate_entered2].index(r2)]= c2
           
         
        
        if turn==0:
            turn=1
        elif turn==1:
            turn=0
            
            
        x=game(coord_and_numbers[1],numbers,list_users,names_players,turn)
            
            
    
    return 1




list_users={}
names_players=[]


table= users_and_points(list_users,names_players) #tabla donde se grardaran los nombres y puntuaciones de usuarios
list_users=table[0]##diccionario con jugadores
print(table[0])#diccionario con jugadores
names_players=table[1]


print("how many pairs of numbers you want to play with?")
pair_of_cards=int(input()) #pares de cartas que debe haber en el juego

board_and_numbers=[]


coord_and_numbers= board(pair_of_cards)


numbers=coord_and_numbers[0]





x= game(coord_and_numbers[1],numbers,list_users,names_players,0)

























