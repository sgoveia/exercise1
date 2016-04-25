# -*- coding: utf-8 -*-
#The MIT License (MIT)
#Copyright (c) 2016 Stephen Goveia
##################################
##############################
#
#    validation_service
#
##############################


##############################
#
#    imports
#
##############################
from data_structures import *


##############################
#
#    check_mode()
#
##############################
def check_mode(input):
    user_input = input
    if(not user_input in valid_modes):
        return 'invalid'
    else:
        return user_input


##############################
#
#    check_piece()
#
##############################
def check_piece(input):
    user_input = input
    if(not user_input in valid_pieces):
        return 'invalid'
    else:
        return user_input


##############################
#
#    check_coodrinate()
#
##############################
def check_coodrinate(input):
    user_input = input
    if(not user_input in valid_coords):
        return 'invalid'
    else:
        return user_input