# -*- coding: utf-8 -*-
"""
Created on Sat Aug 2 13:12:42 2016

@author: Pedro
"""
import numpy as np
import cv2

imgArray = cv2.imread('imagem.png', 0)

numDescs = int(input("Numero de descritores > "))

allEdges = cv2.Canny(imgArray, imgArray.shape[0], imgArray.shape[1])
objEdges = np.where(allEdges == 255)

complexEdges = np.zeros(len(objEdges), dtype = np.complex_)
complexEdges = objEdges[0] + (objEdges[1] * 1j)

descResult = np.complex_(np.zeros(len(complexEdges)))

for i in range(numDescs):
    dft = np.fft.fft(complexEdges)
    descResult += dft

descResult = descResult/numDescs
output = np.fft.ifft(descResult)

blackBgImg = np.zeros(imgArray.shape)
blackBgImg[np.uint8(output.real), np.uint8(output.imag)] = 255

blackBgImg = np.uint8(blackBgImg)

windowName = "Output " + str(numDescs) + " Descritores" 
cv2.imshow(windowName, blackBgImg)
#cv2.imwrite('outputFourier.jpg', blackBgImg)
cv2.waitKey(0)
cv2.destroyAllWindows()