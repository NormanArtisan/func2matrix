# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 14:35:41 2016

@author: Norman.Artisan
"""
print '\f'

from func2matrix_v2 import *

fin = 'function.txt'
fout = 'MatrixA.txt'
fid_X = 'MatrixX.txt'

with open(fid_X,'r') as fid_in:
    line = fid_in.readline()
line = line.replace(' ','')
MatrixX = line.split(',')

with open(fin,'r') as fid_in:
    lines = fid_in.readlines()


mA = []
for line in lines:
    func = line.replace('\n','')
    MatrixA, MatrixX, MatrixB = func2matrix(func, MatrixX)
    mA.append(MatrixA)

lines = func2matrix_IO('matlab', mA)

with open(fout, 'w') as fid:
    for line in lines:
        fid.write(line+'\n')



