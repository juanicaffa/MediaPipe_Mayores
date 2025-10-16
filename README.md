Detección de Caídas en Personas Mayores con MediaPipe y OpenCV
Este proyecto implementa un sistema básico de monitoreo y detección de caídas utilizando la webcam para vigilar a personas, idealmente en entornos de cuidado o para personas mayores.

Requisitos
Asegúrate de tener instaladas las siguientes librerías de Python:

pip install opencv-python mediapipe numpy

Funcionamiento
El sistema opera en tiempo real capturando video de la cámara y procesando la pose del cuerpo con el modelo MediaPipe Pose.

Criterios de Detección 
La alerta de caída se activa cuando se cumplen dos condiciones basadas en los landmarks del cuerpo (hombro y cadera izquierdos):

Inclinación del Torso: El cuerpo está tendido o muy inclinado, con el vector hombro-cadera cerca de la horizontal.
Altura Baja en el Frame: La cadera está en una posición baja en la imagen, indicando que la persona está cerca del suelo.
Si ambas condiciones se cumplen, aparece el mensaje "Persona caida" en la pantalla. 

Uso
Asegúrate de que tu cámara web esté conectada y sea la cámara predeterminada (índice 0).

Ejecuta el script de Python:

python señores.py

Se sale del entorno con "q"

Ajuste de Umbrales
Los umbrales clave se pueden modificar al inicio del script para adaptarlos mejor al entorno o a la altura de la persona:

Angulos: https://docs.google.com/spreadsheets/d/1SHwRfbfFbqvfBpD1j4gfNXQSrb1_cJ7b7nwzVF5U5_g/edit?gid=479813910#gid=479813910

Notas Adicionales
MediaPipe proporciona los landmarks normalizados (valores entre 0 y 1).

La detección se realiza usando el lado izquierdo del cuerpo (LEFT_HIP, LEFT_SHOULDER).
