# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 11:46:02 2021

@author: nicolas
"""
from numpy import *

list_users={}
names_players=[]
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

table= users_and_points(list_users,names_players) #tabla donde se grardaran los nombres y puntuaciones de usuarios
list_users=table[0]##diccionario con jugadores
print(table[0])#diccionario con jugadores
names_players=table[1]


print("how many pairs of numbers you want to play with?")
pair_of_cards=int(input()) #pares de cartas que debe haber en el juego

board_and_numbers=[]

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

coord_and_numbers= board(pair_of_cards)


numbers=coord_and_numbers[0]



def game(board_coor,board_num,dictionary,names,turn):
    
    print('\n','\n',"It's " ,names[turn],' , turn, actual score:',dictionary[names[turn]],'\n')
    
    print(board_coor[0],'\n',board_coor[1])
    
    print('\n',"write the coordenates of the card you want to turn in the form 'a,b' ")
    
    

    coordenate_entered1=input()
    
    coordenate_entered1=coordenate_entered1.split(',')
    
    row_coordenate_entered1=int(coordenate_entered1[0])
    column_coordenate_entered1=int(coordenate_entered1[1])
    
    c1=(int(coordenate_entered1[0]), int(coordenate_entered1[1]))
    board_coor[row_coordenate_entered1][board_coor[row_coordenate_entered1].index((row_coordenate_entered1,column_coordenate_entered1))]=str(board_num[row_coordenate_entered1][column_coordenate_entered1])
    
    r1= board_coor[row_coordenate_entered1][board_coor[row_coordenate_entered1].index((str(board_num[row_coordenate_entered1][column_coordenate_entered1])))]
    
    
    ###############parte 1 turno################
    print('\n','\n')
    
    print(board_coor[0],'\n',board_coor[1])
    
    print('\n',"write the second coordenate of the card you want to turn in the form 'a,b' ")    
    
    coordenate_entered2=input()
    coordenate_entered2=coordenate_entered2.split(',')
    while coordenate_entered2==coordenate_entered1:
        print("you already selectioned this coordenate, please write one that has not been selected")
        coordenate_entered2=input()
        coordenate_entered2=coordenate_entered2.split(',')
                              #
        
        
    
    
    
    
    
    row_coordenate_entered2=int(coordenate_entered2[0])
    column_coordenate_entered2=int(coordenate_entered2[1])
    c2=(int(coordenate_entered2[0]), int(coordenate_entered2[1]))
    board_coor[row_coordenate_entered2][board_coor[row_coordenate_entered2].index((row_coordenate_entered2,column_coordenate_entered2))]=str(board_num[row_coordenate_entered2][column_coordenate_entered2])
    r2=board_coor[row_coordenate_entered2][board_coor[row_coordenate_entered2].index((str(board_num[row_coordenate_entered2][column_coordenate_entered2])))]
    
    print('\n',board_coor[0],'\n',board_coor[1],'\n')
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
            print("congratulations, you've foud the pair of ",r1,' you win an extra turn ',names[turn],', actual score: ',dictionary[names[turn]],'\n')
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
        
        print("you have not found a pair, your turn is over")
          
        board_coor[row_coordenate_entered1][board_coor[row_coordenate_entered1].index(r1)]= c1            
        board_coor[row_coordenate_entered2][board_coor[row_coordenate_entered2].index(r2)]= c2
           
         
        
        if turn==0:
            turn=1
        elif turn==1:
            turn=0
            
            
        x=game(coord_and_numbers[1],numbers,list_users,names_players,turn)
            
            
    
    return 1

x= game(coord_and_numbers[1],numbers,list_users,names_players,0)

























