# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:51:00 2018

@author: Adalberto
"""

from prims import Prims
from functions import G


Initial_Vertex = int(input('At which vertex would you like to start: '))


Prims(G,Initial_Vertex)