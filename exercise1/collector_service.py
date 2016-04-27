# -*- coding: utf-8 -*-
#The MIT License (MIT)
#Copyright (c) 2016 Stephen Goveia
##################################
##############################
#
#    search_service
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
#    gormandizing "to eat greedily or ravenously."
#
##############################
def gormandizing(start, graph, opponents):
    weight_dict = {}
    new_graph = {}
    new_key = 0

    # Build a dict with shortest path for all opponents from start coord
    for opp_piece in opponents:
        new_graph[opp_piece] = shortest_path(graph, start, opp_piece)

    # get weight of edges in new_graph
    for k, v in new_graph.items():
        weight_dict[k] = len(v)

    # sort weight_dict from shorest to longest path by weight
    for key, value in sorted(weight_dict.iteritems(), key=lambda (k, v) : (v, k)):
        #key with smallest weight becomes new_key
        new_key = key
        break

    #get path from previous start to new point
    path = shortest_path(graph, start, new_key)
    if(path is not None):
        full_path.append((len(path) - 1))
    if(path is None):
        # Sum full_path to display moves
        moves = [sum(full_path[:i]) for i in range(1, len(full_path) + 1)]
        print "Got'em all in {} moves! Boom!\n".format(moves[-1])
        #clear full_path and moves lists
        del full_path[:]
        del moves[:]
    else:
        print "{} -> {} : {}".format(start, new_key, path)
        #Remove current key from opponents, and recursivley gormandize
        #opponents pieces
        if new_key in opponents:
            opponents.remove(new_key)
            gormandizing(new_key, graph, opponents)


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
#    collector_service Run
#
##############################
def collector_service_run(data):
    print "Initial Postion: {} : {}   ".format(data[0], data[1])
    print ("Your opponent has pieces at:")
    opposition = get_random_pieces(data[1])
    print opposition
    if(data[0] == 'queen'):
        gormandizing(data[1], queen_graph, opposition)
    if(data[0] == 'rook'):
        gormandizing(data[1], rook_graph, opposition)
    if(data[0] == 'knight'):
        gormandizing(data[1], knight_graph, opposition)


##############################
#
#    collector_service Init
#
#
##############################
def collector_service_init():
    build_queen_graph()
    build_rook_graph()