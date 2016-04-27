# -*- coding: utf-8 -*-
#The MIT License (MIT)
#Copyright (c) 2016 Stephen Goveia
##################################
##############################
#
#    target_mode_service
#
##############################


##############################
#
#    imports
#
##############################
from data_structures import *
from search_service import *
import random


##############################
#
#    queen_target_mode
#
##############################
def queen_target_mode(data, target, opposition , path):
    intial_location = data[1]
    goal = target[1]
    print "Shortest path from {} to {}".format(intial_location, goal)
    print "{}".format(path)
    for i in range(0, len(path)):
        if(path[i] in opposition):
            print "Black Queen captures White Pawn at {}!\n".format(path[i])
            break
    print "\n"


##############################
#
#    rook_target_mode
#
##############################
def rook_target_mode(data, target, opposition, path):
    intial_location = data[1]
    goal = target[1]
    print "Shortest path from {} to {}".format(intial_location, goal)
    print "{}".format(path)
    for i in range(0, len(path)):
        if(path[i] in opposition):
            print "Black Rook captures White Pawn at {}!\n".format(path[i])
            break
    print "\n"


##############################
#
#    knight_target_mode
#
##############################
def knight_target_mode(data, target, opposition, path):
    intial_location = data[1]
    goal = target[1]
    print "Shortest path from {} to {}".format(intial_location, goal)
    print "{}".format(path)
    for i in range(0, len(path)):
        if(path[i] in opposition):
            print "Black Knight captures White Pawn at {}!\n".format(path[i])
            break
    print "\n"


##############################
#
#    target_mode_service Init
#
#
##############################
def target_mode_service_init():
    build_queen_graph()
    build_rook_graph()


##############################
#
#    find_furthest
#
##############################
def find_furthest(coord):
    if(coord in Q1):
        return ['Q1', 'h8']
    if(coord in Q2):
        return ['Q2', 'h1']
    if(coord in Q3):
        return ['Q3', 'a8']
    if(coord in Q4):
        return ['Q4', 'a1']


##############
#
#    get_random_pieces
#
############
def get_random_pieces(start_coord):
    #Copy list
    new_list = board_coords[:]

    # Remove element
    new_list.remove(start_coord)

    #create randomized list
    random.shuffle(new_list)

    # Take the first 8 elements of the now randomized list
    return new_list[0:8]


##############################
#
#    target_mode_service Run
#
##############################
def target_mode_service_run(data):
    target = find_furthest(data[1])
    print "Initial Postion: {}    ".format(data[1]),
    print "Target Position: {} ".format(target[1])
    opposition = get_random_pieces(data[1])
    print opposition
    if(data[0] == 'queen'):
        s_path = shortest_path(queen_graph, data[1], target[1])
        queen_target_mode(data, target, opposition , s_path)
    if(data[0] == 'rook'):
        s_path = shortest_path(rook_graph, data[1], target[1])
        rook_target_mode(data, target, opposition , s_path)
    if(data[0] == 'knight'):
        s_path = shortest_path(knight_graph, data[1], target[1])
        knight_target_mode(data, target, opposition , s_path)
