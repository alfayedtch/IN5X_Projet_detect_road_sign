# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:22:42 2020

@author: Coyot STARK
"""
import tkinter
import sys,pygame, pygame.mixer
from tkinter import filedialog
from pygame.locals import *
from yolov3_image import detectionim
from yolov3_video import yolov3_video
from yolov3_camera import yolov3_webcam
from recon import web

pygame.init()

taille = width, height = 620,480



screen = pygame.display.set_mode(taille)
"""les boutons"""
btnimage = pygame.image.load('btnimage.png')
btnimage = pygame.transform.scale(btnimage, (200,53))
btnvideo = pygame.image.load('btnvideo.png')
btnvideo = pygame.transform.scale(btnvideo, (200,53))
btnwebcam = pygame.image.load('btnWeb.png')
btnwebcam = pygame.transform.scale(btnwebcam, (200,53))



screen.blit(btnimage,(200,200))
screen.blit(btnvideo,(200,300))
screen.blit(btnwebcam,(200,400))


pygame.display.flip()

new = web()
while 1:
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try:
                pygame.quit()
                sys.exit(0)
            except Exception as e:
                raise e
        elif (event.type == MOUSEBUTTONDOWN and mx>=200 and mx<=400 and my >= 200 and my <=253):
            root = tkinter.Tk()
            root.wm_withdraw()
            try:
                filename = filedialog.askopenfilename(filetypes =(("Image", "*.png .jpg"),("All Files","*.*")))
            except:
                print("choisir un bon fichier")
            if str(filename) !="":
                detectionim(str(filename))
            
        elif (event.type == MOUSEBUTTONDOWN and mx>=200 and mx<=400 and my >= 300 and my <=353):
            root = tkinter.Tk()
            root.wm_withdraw()
            try:
                filename = filedialog.askopenfilename(filetypes =(("Video", "*.mp4"),("All Files","*.*")))
            except:
                print("choisir un bon fichier")
            if str(filename) !="":
                yolov3_video(str(filename))
        elif (event.type == MOUSEBUTTONDOWN and mx>=200 and mx<=400 and my >= 400 and my <=453):
            try:
                   new.start()
            except Exception as E:
                raise E
                print("slt")
        
