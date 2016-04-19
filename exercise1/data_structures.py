# -*- coding: utf-8 -*-
#The MIT License (MIT)
#Copyright (c) 2016 Stephen Goveia
##################################
##############################
#
#    data_structures
#
##############################


# main 8x8 matrix represented as a dictionary  with lists as values
board_matrix = {}

# final key list for rook
store_rook = []

# final key list for knight
store_knight = []

board_coords = [
'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']

board_pieces = ['queen', 'knight', 'rook']

valid_coords = ['q',
'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']

valid_pieces = ['q', 'test', 'queen', 'knight', 'rook']


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
