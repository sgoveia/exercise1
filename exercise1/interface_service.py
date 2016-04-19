# -*- coding: utf-8 -*-
#The MIT License (MIT)
#Copyright (c) 2016 Stephen Goveia
##################################

##############################
#
#    interface_service
#
##############################


##############################
#
#    imports
#
##############################
from sys import version_info
from validation_service import *
from test_service import *
from rules_service import *

#Get Python version
py3 = version_info[0] > 2

#List to hold the Chess piece and starting coordinate
data_pair = []
data_pair.append(0)
data_pair.append(0)


##############################
#
#    enter_piece
#
##############################
def enter_piece():
    if py3:
        response = input("1. Please enter chess piece(Queen,Knight,Rook): ")
    else:
        response = raw_input("1. Please enter Piece(Queen,Knight,Rook): ")
    user_input = str(response.lower())
    try:
        check = check_piece(user_input)
        if(check == 'invalid'):
            print '\nSorry not a valid input\n'
            enter_piece()
        else:
            if(user_input == 'q'):
                return user_input
            else:
                if(user_input == 'test'):
                    test_service_run()
                else:
                    data_pair[0] = ''
                    data_pair[1] = ''
                    data_pair[0] = user_input
    except:
        print "\n\nWow somthing went really wrong. Sorry, Goodbye!"
        return 'q'


##############################
#
#    enter_coodinate()
#
##############################
def enter_coodinate():
    if py3:
        response = input("\n2. Please Enter initial Location (a1,h3...): ")
    else:
        response = raw_input("\n2. Please Enter initial Location (a1,h3...): ")
    user_input = str(response.lower())
    try:
        check = check_coodrinate(user_input)
        if(check == 'invalid'):
            print '\nSorry not a valid input\n'
            enter_coodinate()
        else:
            if(user_input == 'q'):
                return user_input
            else:
                if(user_input == 'test'):
                    test_service_run()
                else:
                    data_pair[1] = user_input
                    rules_service_run(data_pair)
    except:
        print "\n\nWow somthing went really wrong. Sorry, Goodbye!"
        return 'q'


##############################
#
#    goodbye_message
#
##############################
def goodbye_message():
    print '\n\nThis was fun! Goodbye!\n\n'
