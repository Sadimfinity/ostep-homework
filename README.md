
# Overview

Este es el README para el simulador virtual de `ffs.py`, un simulador de políticas de asignación 
FFS. Úsalo para aprehender más a profundidad los conceptos relacionados al FFS bajo diferentes 
archivos y escenarios de creación.

La herramienta usa Tkinter para desplegar un entorno virtual donde poder cargar y generar archivos,
para usarlo, necesitarás correr la vista principal así:

Una vez hayas clonado el repositorio has:

```sh
cd /ostep-homework/file-ffs
python3 ./view/main.py
```

El proyecto también cuenta con algunos archivos de ejemplo para probar el funcionamiento del 
simulador.

Por ejemplo el archivo  `in.example1` ubicado en la carpeta `assets` consiste de los siguientes 
comandos:

```sh
dir /a
dir /b
file /a/c 2
file /a/d 2
file /a/e 2
file /b/f 2
```
Una vez el archivo sea cargado y se accione el botón `Crear archivos/directorios`el simulador 
creará dos directorios (/a y /b) y cuatro archivos (/a/c, /a/d, /a/e, and /b/f). El directorio 
root es creado por defecto.

Se podrá explorar la salida del simulador en diferentes formatos, uno de ellos es el simil de:

```
Cilindros Inodos     Data
          0 /--------- /--------- ---------- ----------
          1 acde------ accddee--- ---------- ----------
          2 bf-------- bff------- ---------- ----------
          3 ---------- ---------- ---------- ----------
          4 ---------- ---------- ---------- ----------
          5 ---------- ---------- ---------- ----------
          6 ---------- ---------- ---------- ----------
          7 ---------- ---------- ---------- ----------
          8 ---------- ---------- ---------- ----------
          9 ---------- ---------- ---------- ----------

```

En este caso, hemos creado un sistema de archivos con 10 grupos, cada uno con
10 inodos y 30 bloques de datos. Cada grupo solo muestra los indos y los 
bloques de datos, y como están asignados. Si están libres, un - es mostrado;
in otro caso, un símbolo difente es mostrado por archivo.

Una vez generado el sistema de archivos también se pueden acceder a otras
visualizaciones de la información.

Por ejemplo, al accionar el botón `Mostrar mapa de símbolos` (una vez se 
haya generado el FFS), es como si en shell se ejecutara la línea de
comando:

```sh
prompt> ./ffs.py -f in.example1 -c -M
```
En este caso verás algo similar a:

```sh
Símbolo    Inodo     Nombre del archivo Tipo de archivo
      /            0     /            Directorio
      a           10     /a           Directorio
      c           11     /a/c           Archivo
      d           12     /a/d           Archivo
      e           13     /a/e           Archivo
      b           20     /b           Directorio
      f           21     /b/f           Archivo
```
Aquí podemos ver al directorio representado por un símbolo de /, al archivo
/a por el símbolo a, etc.

Si miras la salida, puedes notar algunas cosas interesantes:

- El inodo root está en la primera ranura de la pieza del Grupo 0 de la tabla de inodo
- El bloque de datos root se encuentra en el primer bloque de datos asignado (Grupo 0)
- El directorio /a fue ubicado en el Grupo 1, el directorio /b en el Grupo 2
- Los archivos (inodos y datos) para cada archivo regular se encuentran en
  el mismo grupo que sus inodos padres (según FFS)


