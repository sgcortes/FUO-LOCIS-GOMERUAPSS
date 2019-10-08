# FUO-LOCIS-GOMERU APPS
Procesado imagen térmica y visible para FUO Locis, Gomeru Apps.

## Bases del proceso
Se trata de escalar la imagen térmica al cuadro de la visible igualando sus resoluiones y superimponiendo ambas teniendo enc eunta que existe un desplazamiento horizontal y (probablemente vertical entre ellas).

![esquema](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/FLIR_THERMAL2.jpg)

### Código
Este código Python se ejecuta sobre las imágenes de las carpetas _Termica_ y _RGB_ y escribe las imágenes compuestas en el directorio _superimposed_.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sgcortes/FUO-LOCIS-GOMERUAPSS/master?filepath=https%3A%2F%2Fgithub.com%2Fsgcortes%2FFUO-LOCIS-GOMERUAPSS%2Fblob%2Fmaster%2FTHERMAL_VISIBLE.ipynb)

https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/THERMAL%26VISIBLE%20(1).html

Ejemplo:

![imagen térmica](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/Termica/20190711_132654_R.jpg)
![imagen RGB](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/RGB/AMBA0331.JPG)
![imagen compuesta](https://github.com/sgcortes/FUO-LOCIS-GOMERUAPSS/blob/master/superimposed/20190711_132654_RAMBA0331.JPG)

