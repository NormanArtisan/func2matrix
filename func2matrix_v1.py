# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 14:34:12 2016

@author: Norman.Artisan
"""
print '\f'

import re


def func2matrix(func, MatrixX):
    
    ''''
    1. delete blank and insert the '+' into the first section
    '''
    func = func.replace(' ', '')
    
    '''
    ===============================================================================
    2. find +,-,= and (,)
    '''
    local_AddMinus = [[xi.start(), xi.end()] for xi in re.finditer('[\+\-]', func)]
    local_Equal = re.search('=', func).start()
    local_RightBracket = [xi.start() for xi in re.finditer('[(]', func)]
    local_LeftBracket = [xi.start() for xi in re.finditer('[)]', func)]
    
    '''
    ===============================================================================
    3. check the number of (,) is right
    '''
    if len(local_RightBracket)>len(local_LeftBracket):
        print 'The ( more than )!!'
    elif len(local_RightBracket)<len(local_LeftBracket):
        print 'The ) more than (!!'
    
    '''
    ===============================================================================
    4. Define the head, foot and remove the location which in bracket.
    '''
    local_block = []
    for ii in local_AddMinus:
        local_block.append(ii[0])
        local_block.append(ii[1])
        
    # the foot
    tmpDelete = []
    for ii in local_block:
        if ii >=local_Equal:
            tmpDelete.append(ii)
    for ii in tmpDelete:
        local_block.remove(ii)
    local_block.append(local_Equal)
    
    # the head
    if not local_block[0]==0:
        local_block.insert(0, 0)
    
    # remove bracket
    tmpDelete = []
    for ii in range(len(local_RightBracket)):
        for xx in local_block:
            if xx>local_RightBracket[ii] and xx< local_LeftBracket[ii]:
                tmpDelete.append(xx)
    for ii in tmpDelete:
        local_block.remove(ii)
    
    del tmpDelete
    
    '''
    ===============================================================================
    4. Select the section and put into the block
    '''
    MatrixA = [];
    for ii in MatrixX:
        MatrixA.append('0')
    for ii in range(len(local_block)/2):
        Flag = False
        position_from = local_block[2*ii]-1
        position_to = local_block[2*ii+1]
        if position_from<0: position_from=0
        Block = func[position_from:position_to:1]
    
        for ii in range(len(MatrixX)): # find *x, +x or -x
            KEY = re.findall('[\*\+\-]'+MatrixX[ii], Block)
            if KEY:
                if KEY[0][0]=='*':
                    element = Block.replace(KEY[0], '')
                elif KEY[0][0]=='+' or KEY[0][0]=='-':
                    element = Block.replace(KEY[0][1:], '')
                    element = Block[0]+'1'
                MatrixA[ii] = element
                Flag = True
                break
            elif Block==MatrixX[ii]:
            # if the element is in the first of function like x+...
                MatrixA[ii] = '1'
                Flag = True
                break
        if not Flag:
            MatrixA[MatrixX.index('1')] = Block
    
    '''
    ===============================================================================
    4. Output Matrix B
    '''
    MatrixB = func[local_Equal+1:]
    
    
    return MatrixA, MatrixX, MatrixB
    
