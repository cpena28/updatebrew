# Script de Actualización y Limpieza de Homebrew

Este script automatiza el proceso de actualización de Homebrew, actualización de los paquetes instalados y limpieza de archivos y paquetes no necesarios. Asegura que tu instalación de Homebrew se mantenga actualizada y libre de desorden.

## Requisitos

- Homebrew debe estar instalado en tu sistema. Si no tienes Homebrew instalado, puedes obtenerlo desde [el sitio web oficial de Homebrew](https://brew.sh/).
- Python 3.x debe estar instalado en tu sistema.

## Detalles del Script

El script realiza las siguientes tareas:
1. Actualiza Homebrew.
2. Actualiza todos los paquetes instalados.
3. Limpia las versiones antiguas de los paquetes instalados.
4. Elimina las dependencias no necesarias.

## Uso

1. **Clonar el Repositorio**

   Clona el repositorio que contiene este script en tu máquina local:

   ```sh
   git clone https://github.com/tu-repo/homebrew-update-cleanup.git
   cd homebrew-update-cleanup
   ```

2. **Estructura del Script**

   La estructura del script es la siguiente:
   
   - `updatebrew.py`: El script principal para actualizar y limpiar Homebrew.
   - `utils/interface.py`: Un script de utilidad para propósitos de registro.

3. **Ejecutar el Script**

   Para ejecutar el script, ejecuta el siguiente comando en tu terminal:

   ```sh
   python3 updatebrew.py
   ```

## Explicación del Script

Aquí hay una explicación detallada del script:

```python
import subprocess
import os
import sys

# Obtener el directorio del script actual (updatebrew.py)
script_dir = os.path.dirname(os.path.abspath(__file__))
# Obtener el directorio padre del directorio del script
parent_dir = os.path.dirname(script_dir)
# Añadir el directorio 'utils' al path de Python
utils_dir = os.path.join(parent_dir, 'utils')
sys.path.append(utils_dir)

from interface import log_info, log_warn, input_yn, log_done, bcolors

log_info("Iniciando actualización de Homebrew...")

# Ejecutar 'brew update' y capturar la salida
update_output = subprocess.run(['brew', 'update'], capture_output=True, text=True).stdout

# Verificar si la salida contiene "Already up-to-date."
if "Already up-to-date." in update_output:
    log_done("Tu Homebrew ya está actualizado. No hay actualizaciones disponibles.")
else:
    log_info("Actualizaciones disponibles. Procediendo con el proceso de actualización y limpieza.")

    log_info("Ejecutando: brew upgrade")
    subprocess.run(['brew', 'upgrade'])
    log_done("Actualización de paquetes completada.")

    log_info("Ejecutando: brew cleanup")
    subprocess.run(['brew', 'cleanup'])
    log_done("Limpieza completada.")

    log_info("Ejecutando: brew autoremove")
    subprocess.run(['brew', 'autoremove'])
    log_done("Eliminación automática de paquetes innecesarios completada.")

log_done("Todos los procesos de Homebrew han finalizado.")
```

### Pasos

1. **Configurar Rutas**:
   - El script configura dinámicamente las rutas para asegurarse de que puede encontrar los módulos de utilidades necesarios.

2. **Importar Funciones de Utilidad**:
   - El script importa funciones de registro del módulo `interface` ubicado en el directorio `utils`.

3. **Actualizar Homebrew**:
   - Ejecuta `brew update` para obtener la lista más reciente de paquetes disponibles y actualizaciones.

4. **Verificar el Estado de la Actualización**:
   - Si Homebrew ya está actualizado, lo registra y sale. De lo contrario, procede con el proceso de actualización y limpieza.

5. **Actualizar Paquetes**:
   - Ejecuta `brew upgrade` para actualizar todos los paquetes instalados a sus últimas versiones.

6. **Limpieza**:
   - Ejecuta `brew cleanup` para eliminar versiones obsoletas de los paquetes.
   - Ejecuta `brew autoremove` para eliminar dependencias no necesarias.

7. **Registrar Finalización**:
   - Registra la finalización de todos los procesos de Homebrew.

## Funciones de Utilidad

Las funciones de utilidad para el registro están definidas en `utils/interface.py`. Asegúrate de que este archivo esté disponible y contenga las funciones necesarias para el registro.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

- [Homebrew](https://brew.sh/)
- Módulo subprocess de Python

Siéntete libre de personalizar este archivo README y el script según tus necesidades específicas.
