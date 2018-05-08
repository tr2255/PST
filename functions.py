# -*- coding: utf-8 -*-
"""
Created on Sat April 28 14:31:22 2018

@author: Adalberto
"""

def cost(G, e): #Determines the cost for Edges
    return G.edge_dict()[e]


def incident_edges(G, T):
    temp_edges = []
    E = G.edge_set()
    for e in E:
        for v in T[0]:
            if v in e and e not in T[1]:
                temp_edges.append(e)
    return temp_edges


def valid_incident_edges(G, T):
    temp_edges = []
    possible_edges = incident_edges(G, T)
    for e in possible_edges:
        if e[0] not in T [0] or e[1] not in T[0]:
            temp_edges.append(e)
    return temp_edges
   
def min_incident_edge(G, T):
    temp_edges = valid_incident_edges(G,T)
    min_edge = temp_edges[0]
    
    for e in temp_edges:
        if cost(G,e) < cost(G, min_edge):
            min_edge = e
    return min_edge
