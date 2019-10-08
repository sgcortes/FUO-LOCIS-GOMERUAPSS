# FUO-LOCIS-GOMERU APPS Procesado imagen térmica y visible para detección de anomlías en líneas de tensión.
Se presentan aquí algunos algoritmos de proceso de imagen térmica y visible para conseguir los sigueintes objetivos:

1. Superimposición de imagen térmica sobre visible
2. Detección de anomalías en imágenes térmicas
3. Utilidad auxiliar: Lectura de información de cabeceros EXIF de imágenes

## 1. Superimposición imagen térmica y visible
Se trata de escalar la imagen térmica al cuadro de la visible igualando sus resoluiones y superimponiendo ambas teniendo en cuenta que existe un desplazamiento horizontal y (probablemente vertical entre ellas).

#### python notebook
https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/md/THERMAL-VISIBLE.md

#### Script Python
https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/CoRegistroTermicaVisibleV2.py

## 2. Detección de anomalías en imágenes térmicas
Dado que las anomalías pueden tener tamaños diferentes la técnica elegida para detectarla ha sido la de detectores de Blobs basados en LoG, HoG y Dog.
El funcionamiento está comentado en este link:
#### python notebook
https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/ThermalBLOBS.md
#### Script Python
https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/ThermalBLOBS.py

### 3. Utilidad auxiliar: Lectura de información de cabeceros EXIF de imágenes

#### python notebook
https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/RegistroExif/RegistroExif.m
#### Script Python
https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/RegistroExif.py
#### Ejemplo imagen visible, térmica, superimpuestas y con Blobs detectados marcados:

![imagen térmica](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/Termica/20190711_132654_R.jpg)
![imagen RGB](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/RGB/AMBA0331.JPG)
![imagen compuesta](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/superimposed/20190711_132654_RAMBA0331.JPG)

