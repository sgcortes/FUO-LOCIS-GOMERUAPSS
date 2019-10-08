# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:28:26 2019

@author: Usuario
"""
import skimage
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
import math
import glob
import os

 # %% Focales y píxeles
        
f_th = 13.25 # mm
f_rgb = 4.5 # mm
     
Ps_rgb = 1.34 # micras
Ps_th = 17. # micras
        
x_foc = f_rgb/f_th
x_pix = Ps_th/Ps_rgb

# Correcciones vertrical y horizontal
Cv = 110
Ch =-20
        
# %% IMAGEN TERMICA

termicas = glob.glob(".\Termica\*.jpg")
visibles = glob.glob(".\RGB\*.jpg")
for rt in zip(visibles, termicas):
        
        th = io.imread(rt[1])
        plt.figure(figsize=(20,20))
        plt.subplot(131)
        plt.imshow(th);
        plt.title(rt[1])
        plt.axis('off')
        
        # %% IMAGEN VISIBLE
        rgb = io.imread(rt[0])   
        plt.subplot(132)
        plt.imshow(rgb);
        plt.title(rt[0])
        plt.axis('off')
       
        # %% COBERTURA SENSOR TERMICO sobre senor RGB
        
        size_th = th.shape[0:2] # pixeles termicos
        sizeTh_rgb = np.floor(np.float32(size_th) * x_foc *x_pix)
                
        # %% IMAGEN TÉRMICA ESCALADA
        scale = sizeTh_rgb[0]/th.shape[0]
        th_sc = skimage.transform.rescale(th, scale,multichannel=True)
        
        # %% limites de intervalos pixeles
        rgb_center = np.float32(rgb.shape[0:2])/2.
        # indice del pixel central
        rgb_center = [round(rgb_center[0]),round(rgb_center[1])]
                
        # límites en coords pixel de la ventana térmica sobre la RGB
        if sizeTh_rgb[0] % 2 == 0:
            Dh = sizeTh_rgb[0] / 2 
            botpixfil = rgb_center[0]-Dh
        elif sizeTh_rgb[0] % 2 != 0:
            Dh = math.floor(sizeTh_rgb[0] / 2) 
            botpixfil = rgb_center[0]-(Dh+1)    
        
        if sizeTh_rgb[1] % 2 == 0:
            Dw = np.floor(sizeTh_rgb[1] / 2) 
            leftpixcol = rgb_center[1]-Dw
        elif sizeTh_rgb[1] % 2 != 0:
            Dw = math.floor(sizeTh_rgb[1] / 2) 
            leftpixcol = rgb_center[1]-(Dw+1)
            
        # Correcciones horizontal y vertical
        # Tienen en cuenta el desplazamiento en vertical y horizontal de los
        # ejes çopticos de las cámaras. Las unidades son píxels de la RGB
        # dividir entre 1.34 micras para pasar a uds abosultas.
        
        botpixfil -= Cv
        leftpixcol += Ch 
        #
        # %% SUPERPOSICION IMAGENES
        rgb_th=skimage.img_as_float(rgb.copy())
        rgb_th[int(botpixfil):int(botpixfil)+th_sc.shape[0],int(leftpixcol):int(leftpixcol)+th_sc.shape[1],:]=th_sc
        
        plt.subplot(133)
        plt.imshow(rgb_th)
        plt.axis('off')
        plt.show()
        
        # %% Grabar imagen visible-termica superpuesta
        # nombre termica
        headth, tailth = os.path.split(rt[1])
        id = tailth.find(".")
        tailth = tailth[0:id]
        headrgb, tailrgb = os.path.split(rt[0])
        filename = ["./superimposed/"+ tailth + tailrgb]
        print(filename[0])
        io.imsave(filename[0], skimage.img_as_ubyte(rgb_th))
        









