# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:18:45 2019

@author: james
"""

import time

import cv2
import mss
import numpy
import pytesseract


mon = {'top': 170, 'left': 40, 'width': 100, 'height': 70}

with mss.mss() as sct:
#    while True:
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(im)
        print(text)

        cv2.imshow('Image', im)
#
#        # Press "q" to quit
#        if cv2.waitKey(25) & 0xFF == ord('q'):
#            cv2.destroyAllWindows()
#            exit()#break

        # One screenshot per second
 #       time.sleep(1)
        