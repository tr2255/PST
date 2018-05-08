# -*- coding: utf-8 -*-
"""
Created on Sat May  5 18:24:32 2018

@author: Adalberto
"""

from functions import *
import functions as P
from Weighted_Graph import *

def Prims(filename, Initial_Vertex):
    
    G = Weighted_Graph(filename)
    VT = {Initial_Vertex} 
    ET = [] 
    MST = (VT, ET) 
    V = G.vertex_set()
    
    cost_min_edge=P.cost(G,P.min_incident_edge(G,MST))
    
   ###PRIMS ALGORITHM
    while MST[0] != V:
        min_edge = P.min_incident_edge(G,MST)
        new_vertex = {min_edge[0], min_edge[1]}
        ET.append(min_edge)
        MST =[new_vertex.union(MST[0]),ET]
    print('MST:',MST, '\n')
       
    
    total_cost = 0
    for e in MST[0]:
        total_cost += cost_min_edge
    print ('\n', 'Total cost of MST:', total_cost, '\n')
        
       
    print ('Minimum Spanning Tree SubGraph:')
    G.draw_subgraph(MST)
