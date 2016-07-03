# -*- coding: utf-8 -*-
"""
Created on Sat Jul 2 13:12:42 2016

@author: Pedro
"""
import numpy as np
import cv2

imagemArray = cv2.imread('Creepy.jpg', 0)

gamma = 1.5
gammaCorrectionValue = 1.0 / gamma

def buildLookUpTable(imgArray, gammaValue):
	LUT = np.arange(0, 256)
	lutIndex = 0;
	for i in range(0, len(imgArray)):
		for j in range(0, len(imgArray[i])):
			normalizedPixel = imgArray[i][j] / 255.0
			correctedPixel = pow(normalizedPixel, gammaValue) * 255
			correctedPixel = pixelLimitValue(correctedPixel)
			LUT[lutIndex] = correctedPixel
			lutIndex = lutIndex + 1
	return LUT

def gammaCorrection(imgArray, gammaValue):
	imgArray = imgArray/255.0
	imgArray = cv2.pow(imgArray, gammaValue)
	return imgArray

def pixelLimitValue(value):
    if (value < 0):
        value = 0;
    if (value > 255):
        value = 255;
    return value

LUT = buildLookUpTable(imagemArray, gammaCorrectionValue)
print LUT

imagemArray = gammaCorrection(imagemArray, gammaCorrectionValue)

#cv2.imshow('Resultado Gamma Correction', imagemArray)
#cv2.imwrite('outputGammaCorrection.jpg', imagemArray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
