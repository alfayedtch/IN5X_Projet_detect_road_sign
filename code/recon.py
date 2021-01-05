# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:28:28 2021

@author: Coyot STARK
"""
from yolov3_camera import yolov3_webcam

class web:
    def __init__(self):
        self.moi = True
        
    def start(self):
        self.moi = True
        while self.moi:
            yolov3_webcam(self)
    
    def stop(self):
        self.moi = False
        