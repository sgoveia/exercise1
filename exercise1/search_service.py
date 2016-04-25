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
from collections import deque
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
#    breadth-first search
#
##############################
def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])


##############################
#
#    shortest_path
#
##############################
def shortest_path(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return  None


