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
Check Move is an interactive terminal program, have fun!

    Input \"q\" to quit

'''
####################################
#
#    init
#
####################################
rules_service_init()
target_mode_service_init()
####################################
#
#    main loop
#
####################################
while True:
    mode = enter_mode()
    if (mode == 'q'):
        goodbye_message()
        break
    piece = enter_piece()
    if (piece == 'q'):
        goodbye_message()
        break
    coordinate = enter_coodinate()
    if (coordinate == 'q'):
        goodbye_message()
        break
