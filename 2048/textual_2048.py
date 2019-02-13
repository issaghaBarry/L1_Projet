#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_

:date: 2017, march

"""

from game_2048 import *

commands = { "U" : "up", "L" : "left", "R" : "right", "D" : "down", "S":"S" }
themes = {"C": "chimie", "E": "entier"}
start= {"N", "L"}

def read_next_move():
    """
    read a new move

    :UC: none
    """
    while True: 
        entre=input ('Your Move ? ((U)p, (D)own, (L)eft, (R)ight, (S)ave ')
        try:
            assert entre.upper() in commands
            return entre.upper()
        except AssertionError:
            pass

        
def read_theme():
    """
    read a new theme with you play

    UC: none
    """
    while True: 
        theme=input ('Your theme ? ((C)himie, (E)entier) ')
        if theme=='':
            return 'E'
        try:
            assert theme.upper() in themes
            return theme.upper()
        except AssertionError:
            pass          

def read_open():
    """
    read if the player want to play a new game or the last backup game

    UC: none
    """
    while True:
        entre = input ('(N)ew game , (L)oad ')
        try:
            assert entre.upper() in start
            if entre.upper()== "L":
                nom= input('Your Name ?')
                password= input('Your password ?')
                contenue= grid_load(nom.lower()+password+'.txt')
                return contenue
            if entre.upper()== "N":
                break
        except AssertionError:
            pass
        except FileNotFoundError:
            print( '!!! ohh are you sure you have a backup?')
            print('!!!! Play a new game lucky please!!!!!')
            break
def read_close():
    """
    """
    while True: 
        entre=input (' Do you want to continue a game?(Y)es, (N)o ')
        try:
            assert entre.upper() in ["Y", "N"]
            return entre.upper()
        except AssertionError:
            pass

    

def play():
    """
    main game procedure
    
    """
    grid= read_open()
    theme=read_theme()
    if grid== None:
        grid = grid_init()
    grid_print(grid, themes[theme])
    while not is_grid_over(grid) and grid_get_max_value(grid) < 2048:
        move = read_next_move()
        if move== "S":
            name= input('your Name please!!!')
            password= input('Your password please!!!')
            grid_save(grid, name+password+'.txt')
            sortie= read_close()
            if sortie== "N":
                exit(1)
            elif sortie== "Y":
                continue
        else:
            grid = grid_move(grid, commands[move])
            grid_add_new_tile(grid)
        grid_print(grid, themes[theme])
        print("Votre Score:", grid_score(grid))
    if grid_get_max_value(grid) == 2048:
        print("You Won !!")
    else:
        print("You Lose ;-(")


def usage():
    print('Usage : {:s}'.format(sys.argv[0]))
    exit(1)

if __name__ == '__main__':
    import sys

    play()
    exit(0)
