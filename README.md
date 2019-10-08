# FUO-LOCIS-GOMERU APPS Procesado imagen térmica y visible para detección de anomlías en líneas de tensión.

## Superimposición imagen térmica y visible
Se trata de escalar la imagen térmica al cuadro de la visible igualando sus resoluiones y superimponiendo ambas teniendo enc eunta que existe un desplazamiento horizontal y (probablemente vertical entre ellas).

![esquema](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/FLIR_THERMAL2.jpg)

### Código
Este código Python se ejecuta sobre las imágenes de las carpetas _Termica_ y _RGB_ y escribe las imágenes compuestas en el directorio _superimposed_.
#### Notebook python ilustrado
https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/md/THERMAL-VISIBLE.md

#### Script Python
https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/CoRegistroTermicaVisibleV2.py

## Detección de Blobs anómalos en imágenes térmicas
Dado que las anomalías pueden tener tamaños diferentes la técnica elegida para detectarla ha sido la de detectores de Blobs basados en LoG, HoG y Dog.
El funcionamiento está comentado en este link:

https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/ThermalBLOBS%20(1).html


#### Ejemplo imagen visible, térmica, superimpuestas y con Blobs detectados marcados:

![imagen térmica](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/Termica/20190711_132654_R.jpg)
![imagen RGB](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/RGB/AMBA0331.JPG)
![imagen compuesta](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/superimposed/20190711_132654_RAMBA0331.JPG)

