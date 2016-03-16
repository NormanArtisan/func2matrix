# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 14:35:41 2016

@author: Norman.Artisan
"""
print '\f'

from func2matrix_v1 import func2matrix

fin = 'function.txt'
fout = 'MatrixA.txt'
fid_X = 'MatrixX.txt'
MatrixX = ['w', 'x', 'y', 'z', '1']
with open(fid_X,'r') as fid_in:
    line = fid_in.readline()
line = line.replace(' ','')
MatrixX = line.split(',')

with open(fin,'r') as fid_in:
    lines = fid_in.readlines()

fid_out = open(fout, 'w')

for line in lines:
    func = line.replace('\n','')
    MatrixA, MatrixX, MatrixB = func2matrix(func, MatrixX)
    
    OutLine = []
    for ii in range(len(MatrixA)):
        if ii == 0:
            OutLine = MatrixA[ii]
        else:
            OutLine = OutLine+', '+MatrixA[ii]
    fid_out.write(OutLine+'\n')
fid_out.close()


