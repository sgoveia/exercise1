# -*- coding: utf-8 -*-
#The MIT License (MIT)
#Copyright (c) 2016 Stephen Goveia
##################################
##############################
#
#    rules_service
#
##############################


##############################
#
#    imports
#
##############################
from data_structures import *


##############
#
#    utility method to return key of
#    dictrionary value
#
############
def get_key(dic, value):
    for key in dic:
        if (dic[key] == value):
            return key


##############################
#
#    queen rules
#
##############################
def rules_service_queen(data):
    intial_location = data[1]
    temp_list = []
    for key, value in board_matrix.items():
        if key not in intial_location:
            temp_list.append(key)
    print(data)
    print ', '.join(temp_list) + "\n"


##############################
#
#    rook rules
#
##############################
def rook_up(data):
    col = 7
    intial_location = data[1]
    pair = board_matrix.get(intial_location)
    x = pair[0]
    y = pair[1]
    for i in range(0, col - y):
        y += 1
        store_rook.append(get_key(board_matrix, [x, y]))


def rook_down(data):
    intial_location = data[1]
    pair = board_matrix.get(intial_location)
    x = pair[0]
    y = pair[1]
    for i in range(0, y):
        y -= 1
        store_rook.append(get_key(board_matrix, [x, y]))


def rook_left(data):
    intial_location = data[1]
    pair = board_matrix.get(intial_location)
    x = pair[0]
    y = pair[1]
    for i in range(0, x):
        x -= 1
        store_rook.append(get_key(board_matrix, [x, y]))


def rook_right(data):
    col = 7
    intial_location = data[1]
    pair = board_matrix.get(intial_location)
    x = pair[0]
    y = pair[1]
    for i in range(0, (col - x)):
        x += 1
        store_rook.append(get_key(board_matrix, [x, y]))


###############################
def rules_service_rook(data):
    # clear list
    del store_rook[:]
    #run rules
    try:
        rook_up(data)
        rook_down(data)
        rook_left(data)
        rook_right(data)
        if(len(store_rook) == 0):
            print("\nSorry no valid moves from that location\n")
        else:
            print(data)
            print ', '.join(store_rook) + "\n"
    except:
        print ("\nNo valid moves availible from that location\n")


##############################
#
#     knight  rules
#
##############################
def knight_up(data):
    intial_location = data[1]
    pair = board_matrix.get(intial_location)
    x = pair[0]
    y = pair[1]
    y += 2
    x += 1
    k = get_key(board_matrix, [x, y])
    if(k is not None):
        store_knight.append(k)
    x -= 2
    k = get_key(board_matrix, [x, y])
    if(k is not None):
        store_knight.append(k)


def knight_down(data):
    intial_location = data[1]
    pair = board_matrix.get(intial_location)
    x = pair[0]
    y = pair[1]
    y -= 2
    x += 1
    k = get_key(board_matrix, [x, y])
    if(k is not None):
        store_knight.append(k)
    x -= 2
    k = get_key(board_matrix, [x, y])
    if(k is not None):
        store_knight.append(k)


def knight_left(data):
    intial_location = data[1]
    pair = board_matrix.get(intial_location)
    x = pair[0]
    y = pair[1]
    x -= 2
    y += 1
    k = get_key(board_matrix, [x, y])
    if(k is not None):
        store_knight.append(k)
    y -= 2
    k = get_key(board_matrix, [x, y])
    if(k is not None):
        store_knight.append(k)


def knight_right(data):
    intial_location = data[1]
    pair = board_matrix.get(intial_location)
    x = pair[0]
    y = pair[1]
    x += 2
    y += 1
    k = get_key(board_matrix, [x, y])
    if(k is not None):
        store_knight.append(k)
    y -= 2
    k = get_key(board_matrix, [x, y])
    if(k is not None):
        store_knight.append(k)


###############################
def rules_service_knight(data):
    # clear list
    del store_knight[:]
    #run rules
    try:
        knight_up(data)
        knight_down(data)
        knight_left(data)
        knight_right(data)
        if(len(store_knight) == 0):
            print("\nSorry no valid moves from that location\n")
        else:
            print(data)
            print ', '.join(store_knight) + "\n"
    except:
        print ("\nNo valid moves availible from that location\n")


##############################
#
#    rules_service Init
#
#
#    fill list with board locations
##############################
def rules_service_init():
    i = 0
    #fill board_matrix with string represintations of coords
    for x in range(0, 8):
        for y in range(0, 8):
            # set each coord(a1,b5, etc) to a location in board_matrix.
            board_matrix[board_coords[i]] = [y, x]
            i += 1


##############################
#
#    rules_service Run
#
##############################
def rules_service_run(data):
    if(data[0] == 'queen'):
        rules_service_queen(data)
    if(data[0] == 'rook'):
        rules_service_rook(data)
    if(data[0] == 'knight'):
        rules_service_knight(data)

