# -*- coding: utf-8 -*-
#The MIT License (MIT)
#Copyright (c) 2016 Stephen Goveia
##############################
#
#    imports
#
##############################
from interface_service import *
from rules_service import *


print '''********************************************************************\n
 #####
 #     # #    # ######  ####  #    #
 #       #    # #      #    # #   #
 #       ###### #####  #      ####
 #       #    # #      #      #  #
 #     # #    # #      #    # #   #
  #####  #    # ######  ####  #    #


         #    #  ####  #    # ######
         ##  ## #    # #    # #
         # ## # #    # #    # #####
         #    # #    # #    # #
         #    # #    #  #  #  #
         #    #  ####    ##   ######\n
*****************************************************************************\n
Check Move is an interactive terminal program designed to list all possibile
coordinate postions \"moves\" for a given Chess piece based on an intial
starting coordinate.
\n
Please follow the promt to list of all the potential board positions for
the given piece and coordinate.\n

To run a test of all possible outcomes for Queen, Knight, and Rook, input
\"test\" at  prompt# 1. for example:\n
\"    1. Please enter Piece(Queen,Knight,Rook): test    \"\n
    Input \"q\" to quit
'''
####################################
#
#    init
#
####################################
rules_service_init()

####################################
#
#    main loop
#
####################################
while True:
    piece = enter_piece()
    if (piece == 'q'):
        goodbye_message()
        break
    coordinate = enter_coodinate()
    if (coordinate == 'q'):
        goodbye_message()
        break
