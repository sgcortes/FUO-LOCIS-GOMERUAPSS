#!/usr/bin/env python
# coding: utf-8

# <table style="width:100%">
#   <tr>
#     <td><img src="./img/logo_EPM_UNIOVI_CabeceroWEB.gif" width="211" height="69" alt="Uniovi & EP Mieres logos" title="Uniovi & EP Mieres logos" /></td>
#     <td><font color=brown>Procesamiento de imágenes <br> de Sensores Aerotransportados y Satélite<br></font>
#     <font color=green>Universidad de Oviedo. <br>Ingeniería en Geomática</font> <br><br>sgcortes@uniovi.es</td>
#   </tr>
# </table>

# ## Registro de imágenes térmicas y visibles proyecto FUO LOCIS-GOMERU APPS

# In[46]:


import skimage
import skimage.io as io
import exifread
import matplotlib.pyplot as plt


# ### Imagen Térmica

# In[30]:


# Open image file for reading (binary mode)
f = open('./matching/3casas.jpg', 'rb')
tags = exifread.process_file(f)
# print(tags)


# In[31]:


th = io.imread('./matching/3casas.jpg')
print(th.shape)
print(th.dtype)
print(th.max())
print(th.min())
# print(tags['Image FocalLength']) #/ mm
# print(tags.keys())
io.imshow(th);


# ### Imagen visible

# In[47]:


# Open image file for reading (binary mode)
f = open('./matching/3casasRGB.jpg', 'rb')
tagsRGB = exifread.process_file(f)
# print(tagsRGB)


# In[33]:


rgb = io.imread('./matching/3casasRGB.jpg')
print(rgb.shape)
print(rgb.dtype)
print(tagsRGB['EXIF FocalLength'])
io.imshow(rgb);


# In[34]:


frgb = 5# mm
Ps_rgb = 1.34 # micras Pixel Size	1.34µm x 1.34µm

w_rgb = Ps_rgb*rgb.shape[1]/1000
h_rgb = Ps_rgb*rgb.shape[0]/1000
print('Sensor Size RGB (mm):',w_rgb,h_rgb)
# http://www.camera-module.com/product/mipicameramodule/16mp-mipi-camera-module-sony-imx206-sensor.html
# http://www.foxeer.com/legend1.html


# ## Solución simple superposición

# Separación entre centros de cámaras:

# In[35]:


fact_conv = 158/522 # mm/pixel
dpix_centros = 161 # pixels
dmm_centros = dpix_centros * fact_conv
print(dmm_centros)


# Tamaño ancho sensor Térmico:

# In[36]:


fth = 13 # mm
Ps_th = 17 # micras
w_th = Ps_th * th.shape[1]/1000
h_th = Ps_th * th.shape[0]/1000
print(w_th,h_th) # mm


# In[37]:


h_th_equiv = h_th * frgb/fth
print(h_th_equiv) # mm


# In[38]:


Altura_TH_pix = h_th_equiv/(Ps_rgb/1000)
print(Altura_TH_pix)


# El rango de píxeles en altura que ocuiparía sobre el sensor RGB la iamgen térmica sería de:

# In[39]:


hpixmax = int(rgb.shape[0]/2+Altura_TH_pix/2)
hpixmin = int(rgb.shape[0]/2-Altura_TH_pix/2)
print(hpixmax,hpixmin)


# In[40]:


print(hpixmax-hpixmin)


# Es necesario ahora reescalar (sopbremuestrear) la imagen térmica

# In[41]:


scale = Altura_TH_pix/th.shape[0]
th_sc = skimage.transform.rescale(th, scale,multichannel=True)
print(th_sc.shape)
print(th_sc.max())
print(th_sc.min())
io.imshow(th_sc);


# Repetimos el cálculo en horizontal:

# In[42]:


wpixmax = int(rgb.shape[1]/2+th_sc.shape[1]/2)+36
wpixmin = int(rgb.shape[1]/2-th_sc.shape[1]/2)+36
print(wpixmax,wpixmin)


# Superponemos las imágenes

# In[43]:


rgb_th = skimage.img_as_float(rgb)
th_sc = skimage.img_as_float(th_sc, force_copy=False)
rgb_th[hpixmin:hpixmax-1,wpixmin:wpixmax,:]=th_sc
io.imshow(rgb_th);


# Corrección horizontal por el deplazamiento entre ejes de cámaras. La distancia medida entre ejes de cámaras es de 161 píxeles y 
# la que está acotada es de 158 mm para 522 pixeles

# In[45]:


Axisdist = 161*158/522 # mm
Axisdistpix = Axisdist/Ps_rgb # num pixels
print(Axisdistpix)


# In[ ]:




