# Laboratorio 2 - Seguridad en Redes

Este repositorio contiene los archivos correspondientes al Laboratorio 2 sobre Seguridad en Redes. A continuación, se detallan los archivos incluidos y su propósito.

## Descripción

Este laboratorio está enfocado en el uso de herramientas de seguridad para realizar pruebas de penetración y análisis de vulnerabilidades. Se han utilizado herramientas como **Burp Suite**, **cURL**, y **Hydra** para examinar distintos escenarios de seguridad en el entorno de pruebas proporcionado por **DVWA** (Damn Vulnerable Web Application).

## Estructura del Proyecto

- `Laboratorio_2_Renato_Contreras.pdf`: Informe completo del Laboratorio 2, que incluye los resultados, análisis y conclusiones obtenidos a partir de las pruebas realizadas.
- `docker-compose.yml`: Archivo de configuración para desplegar el entorno de pruebas utilizando Docker, incluyendo la configuración para DVWA.
- `attack.py`: Script Python utilizado para interactuar con el formulario de inicio de sesión de DVWA.
- `john.txt`: Archivo de texto que contiene las contraseñas utilizadas en el ataque de fuerza bruta.
- `users.txt`: Archivo de texto con los nombres de usuarios probados durante las pruebas.
- `cURL-valido.html`: Archivo HTML generado por la herramienta **cURL** al enviar credenciales válidas.
- `cURL-invalido.html`: Archivo HTML generado por **cURL** al enviar credenciales inválidas.

### Carpetas de Imágenes y Capturas de Tráfico

- `Packets/`: Carpeta que contiene capturas de los paquetes obtenidos en **Wireshark**, que documentan el tráfico generado por **cURL**, **Burp Suite**, e **Hydra**.
- `img-Burp/`: Carpeta que contiene capturas de pantalla de las pruebas realizadas con **Burp Suite**.
- `img-cURL/`: Carpeta que contiene capturas de pantalla de las pruebas realizadas con **cURL**.
- `img-Hydra/`: Carpeta que contiene capturas de pantalla de las pruebas realizadas con **Hydra**.
- `img-python/`: Carpeta que contiene capturas de pantalla relacionadas con el script Python utilizado.

## Contacto

Para cualquier duda o consulta relacionada con este laboratorio, puedes contactarme a través del siguiente correo electrónico:

**Renato Óscar Benjamín Contreras Carvajal**  
Email: renato.contreras@mail.udp.cl
