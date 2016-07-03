# -*- coding: utf-8 -*-
"""
Created on Sun Jul 3 18:13:12 2016

@author: Pedro
"""
import numpy as np
import cv2
import statistics

imagemArray = cv2.imread('Creepy.jpg', 0)
lastIndex = len(imagemArray)*2 - 1
minValue = 0
maxValue = 255

def threshold(imgArray):
	thresholdValue = np.median(imgArray)
	print "Threshold Value =", thresholdValue
	for i in range (imgArray.shape[0]):
		for j in range (imgArray.shape[1]):
			if (imgArray[i][j] > thresholdValue):
				imgArray[i][j] = maxValue
			else:
				imgArray[i][j] = minValue
	return imgArray

imagemArray = threshold(imagemArray)

cv2.imshow('Threshold', imagemArray)
cv2.waitKey(0)
cv2.destroyAllWindows()
