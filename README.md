# Script OBS: Hora Personalizable en Texto GDI+

Este script para **OBS Studio** permite mostrar la hora actual en una fuente de texto GDI, con múltiples opciones de personalización. Perfecto para transmisiones en vivo que necesiten incluir la hora local o de cualquier parte del mundo.

## Características

- **Fácil configuración**: Todas las opciones se ajustan desde el panel de scripts de OBS.
- **Lista desplegable de zonas horarias**: Selecciona entre más de 500 regiones usando el estándar de `pytz`.
- **Formato de hora personalizable**: Cambia entre formato de 24 horas y 12 horas con AM/PM.
- **Opciones avanzadas**:
  - Mostrar GMT (zona horaria relativa a UTC).
  - Mostrar continente y ciudad (extraído de la zona horaria seleccionada).
- **Prefijo personalizable**: Agrega un texto antes de la hora, como "Hora:".
- **Actualización automática**: El texto se actualiza cada segundo para reflejar la hora actual.

## Requisitos

1. OBS Studio 30.0 o superior.
2. Python 3.6 configurado en OBS Studio.
3. Biblioteca `pytz` instalada:
   ```bash
   pip install pytz

Instalación
Descarga el script: Descarga el archivo hora_personalizable.py desde este repositorio.
Carga el script en OBS:
Abre OBS Studio.
Ve a Herramientas > Scripts.
Haz clic en el botón + y selecciona el archivo del script.
Configura las opciones:
Selecciona la fuente de texto GDI donde deseas mostrar la hora.
Elige la zona horaria desde la lista desplegable.
Personaliza las demás opciones como prefieras.
A continuación, puedes ver cómo cargar el script en OBS y configurar sus opciones:

Configuración del Script


Configuración de la Fuente de Texto


Configuración
El script ofrece las siguientes opciones de personalización:

Fuente de Texto GDI: Selecciona la fuente de texto en OBS donde se mostrará la hora.
Zona Horaria: Elige entre más de 500 zonas horarias disponibles.
Formato de Hora: Usa formato de 24 horas o 12 horas con AM/PM.
Mostrar GMT: Activa o desactiva la visualización de GMT.
Mostrar Continente/Ciudad: Incluye o excluye el continente y la ciudad de la zona horaria.
Prefijo: Personaliza el texto que aparece antes de la hora, por ejemplo, "Hora:".
Ejemplo de Salida
El texto en OBS puede configurarse para mostrar, por ejemplo:
https://github.com/SirFrancisDrakesTV/TIME_OBS/blob/main/Captura%20de%20pantalla%202024-11-26%20082903.png
Hora: 14:35:12 | GMT+1 | Europe/Madrid
O, con menos opciones activadas:
14:35:12
Capturas de Pantalla
A continuación, se muestran algunas capturas de pantalla del script en acción:
https://github.com/SirFrancisDrakesTV/TIME_OBS/blob/main/Captura%20de%20pantalla%202024-11-26%20082800.png


Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes ideas para mejorar este script, no dudes en abrir un issue o un pull request.

Autor
Este script fue desarrollado por SirFrancisDrakesTV para facilitar la visualización de la hora en transmisiones en vivo. Puedes usarlo, modificarlo y compartirlo libremente, pero no olvides dar crédito al creador. 🚀

Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
