# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:54:15 2016

@author: Pedro
"""
from PIL import Image
import numpy as np

imagem = Image.open('Lenna.jpg')
imagemArray = np.array(imagem)

#####################################################
  ################### FUNCOES ###################
#####################################################

def pontaCabeca():
    upsideDown = imagem.rotate(180)
    upsideDownArray = np.array(upsideDown)
    output = Image.fromarray(upsideDownArray)
    output.save('outputUpsidedown.jpg')

def multTile():
    upsideDown = imagem.rotate(180)
    upsideDownArray = np.array(upsideDown)
    matrixLenna = np.tile(upsideDownArray, (2,3))
    output = Image.fromarray(matrixLenna)
    output.save('outputTiled.jpg')


def contraste(contraste):
    imagemTile = Image.open('outputTiled.jpg')
    imagemArray = np.array(imagemTile)
    fator = (100.0 + contraste)/ 100.0;
    fator *= fator;
    for i in range(0, len(imagemArray)):
        for j in range(0, len(imagemArray[i])):
            novoValor = imagemArray[i][j]                
            novoValor /= 255.0                
            novoValor -= 0.5                
            novoValor *= fator                
            novoValor += 0.5                
            novoValor *= 255.0                
            imagemArray[i][j] = limitaVal(novoValor)
    output = Image.fromarray(imagemArray)
    output.save('outputContraste.jpg')
                        

def gradient(f):
    imagemTile = Image.open('outputTiled.jpg')
    imagemArray = np.array(imagemTile)
    for i in range(0, len(imagemArray)):
        for j in range(0, len(imagemArray[i])):
            novoValor = imagemArray[i][j]
            novoValor -= (i+j)* f;
            imagemArray[i][j] = limitaVal(novoValor)  
    output = Image.fromarray(imagemArray)
    output.save('outputGradient.jpg')

def limitaVal(valor):
    if (valor < 0):
        valor = 0;
    if (valor > 255):
        valor = 255;
    return valor


#####################################################
  ################### CHAMADAS ###################
#####################################################

pontaCabeca()

multTile()

contFator = 100
contraste(contFator)

gradFator = 0.15;
gradient(gradFator)
