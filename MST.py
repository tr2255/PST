# -*- coding: utf-8 -*-
"""
Created on Sun April 29 12:51:00 2018

@author: Adalberto
"""

from prims import Prims


filename = input(str('What is the name of the file: '))
Initial_Vertex = int(input('Enter the vertex where you wish to begin: '))


Prims(filename, Initial_Vertex)
