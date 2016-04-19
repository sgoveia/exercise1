# -*- coding: utf-8 -*-
#The MIT License (MIT)
#Copyright (c) 2016 Stephen Goveia
##################################
##############################
#
#    test_service
#
##############################


##############################
#
#    imports
#
##############################
from data_structures import *
from rules_service import *


def test_service_init():
    i = 0
    #fill board_matrix with string represintations of coords
    for x in range(0, 8):
        for y in range(0, 8):
            # set each coord(a1,b5, etc) to a location in board_matrix.
            board_matrix[board_coords[i]] = [y, x]
            i += 1


def test_service_run():
    # Run Queen Test
    for piece in board_coords:
        rules_service_queen(['queen', piece])
    # Run Rook Test
    for piece in board_coords:
        rules_service_rook(['rook', piece])
    # Run Knight Test
    for piece in board_coords:
        rules_service_knight(['knight', piece])

