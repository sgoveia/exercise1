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
from target_mode_service import *
from collector_service import *


##############################
#
#    test_service_init
#
##############################
def test_service_init():
    i = 0
    #fill board_matrix with string represintations of coords
    for x in range(0, 8):
        for y in range(0, 8):
            # set each coord(a1,b5, etc) to a location in board_matrix.
            board_matrix[board_coords[i]] = [y, x]
            i += 1


##############################
#
#    test_service_standard_mode_run
#
##############################
def test_service_standard_mode_run():
    # Run Queen Test
    for piece in board_coords:
        rules_service_queen(['queen', piece])
    # Run Rook Test
    for piece in board_coords:
        rules_service_rook(['rook', piece])
    # Run Knight Test
    for piece in board_coords:
        rules_service_knight(['knight', piece])


##############################
#
#    test_service_target_mode_run
#
##############################
def test_service_target_mode_run():
    # Run Queen Test
    for piece in board_coords:
        target_mode_service_run(['queen', piece])
    # Run Rook Test
    for piece in board_coords:
        target_mode_service_run(['rook', piece])
    # Run Knight Test
    for piece in board_coords:
        target_mode_service_run(['knight', piece])


##############################
#
#    test_service_collector_mode_run
#
##############################
def test_service_collector_mode_run():
    # Run Queen Test
    for piece in board_coords:
        collector_service_run(['queen', piece])
    # Run Rook Test
    for piece in board_coords:
        collector_service_run(['rook', piece])
    # Run Knight Test
    for piece in board_coords:
        collector_service_run(['knight', piece])
