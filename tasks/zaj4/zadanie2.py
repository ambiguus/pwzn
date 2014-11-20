# -*- coding: utf-8 -*-

import numpy as np

from itertools import chain, permutations, product


def calculate_neighbours(board):

    """

    Funkcja zwraca tablicę która w polu N[R, C] zwraca ilość sąsiadów którą 
    ma komórka Board[R, C]. Za sąsiada uznajemy obszazoną komórkę po bokach lub
    na ukos od danej komórki, komórka nie jest swoim sąsiatem, zatem maksymalna
    ilość sąsiadów danej komórki wynosi 8.

    Funkcja ta powinna być zwektoryzowana, tj ilość operacji w bytekodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.

    :param np.ndarray board: Dwuwymiarowa tablica zmiennych logicznych która
    obrazuje aktualny stan game of life. Jeśli w danym polu jest True (lub 1)
    oznacza to że dana komórka jest obsadzona


    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczymy ilość sąsiadów
    prawych itp.

    Podpowiedź II: Proszę uważać na komówki na bokach i rogach planszy.
    """
    neighbour = np.zeros(board.shape)
    x = board.shape[0]
    y = board.shape[1]
    neighbour[:x-1,:] += board[1:x,:]
    neighbour[1:x,:] += board[:x-1,:]
    neighbour[:,:y-1] += board[:,1:y]
    neighbour[:,1:y] += board[:,:y-1]
    neighbour[:x-1,:y-1] += board[1:x,1:y]
    neighbour[1:x,1:y] += board[:x-1,:y-1]
    neighbour[:x-1,1:y] += board[1:x,:y-1]
    neighbour[1:x,:y-1] += board[:x-1,1:y]
    return neighbour


def iterate(board):

    """

    Funkcja pobiera planszę game of life i zwraca jej następną iterację.

    Zasady Game of life są takie:

    1. Komórka może być albo żywa albo martwa.
    2. Jeśli komórka jest martwa i ma trzech sąsiadóœ to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadóœ również umiera. W przeciwnym wypadku
       (dwóch lub trzech sąsiadów) to żyje dalej.

    :param np.ndarray board: Dwuwymiarowa tablica zmiennych logicznych która
    obrazuje aktualny stan game of life. Jeśli w danym polu jest True (lub 1)
    oznacza to że dana komórka jest obsadzona

    """
    nn = calculate_neighbours(board)
    next= np.zeros(board.shape)
    next[np.logical_or(np.logical_and(nn == 3, board == False), np.logical_and(board == True, np.logical_or(nn==2, nn==3)))] = True
    return next.astype(bool)