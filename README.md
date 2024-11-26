# TIME_OBS
Este script para OBS Studio permite mostrar la hora actual en una fuente de texto GDI, con múltiples opciones de personalización


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



Script OBS: Hora Personalizable en Texto GDI+
Este script para OBS Studio permite mostrar la hora actual en una fuente de texto GDI, con múltiples opciones de personalización:

Selección de zona horaria desde una lista desplegable.
Formato de hora configurable (24 horas o 12 horas con AM/PM).
Opciones para mostrar:
GMT (zona horaria relativa a UTC).
Continente y ciudad (basados en la zona horaria seleccionada).
Prefijo personalizable para el texto (por ejemplo: "Hora:").
Actualización automática cada segundo.
Características
Fácil configuración: Todas las opciones se pueden ajustar desde el panel de scripts de OBS.
Lista desplegable de zonas horarias: Más de 500 regiones disponibles, utilizando el estándar de zonas horarias de pytz.
Soporte para formato 12/24 horas: Cambia fácilmente entre ambos formatos según tu preferencia.
Texto dinámico: El script actualiza automáticamente el texto para reflejar la hora actual en la zona horaria seleccionada.
Adaptación automática a GMT y horarios de verano/invierno.
Requisitos
OBS Studio 30.0 o superior.
Python 3.6.x configurado en OBS.
Biblioteca pytz instalada. Si no la tienes, puedes instalarla ejecutando:
bash
Copiar código
pip install pytz
Cómo usarlo
Descarga el script y cárgalo en OBS Studio desde el menú Herramientas > Scripts.
Configura las opciones en el panel del script:
Selecciona la fuente de texto GDI donde deseas mostrar la hora.
Elige la zona horaria desde el listado.
Personaliza las opciones de formato, GMT y continente/ciudad.
Observa cómo el texto en OBS se actualiza automáticamente con la hora actual.
Ejemplo de salida
"Hora: 14:35:12 | GMT+1 | Europe/Madrid"

Autor
Este script fue desarrollado por SirFrancisDrakesTV para facilitar la visualización de la hora en OBS Studio, con total flexibilidad y personalización.

Notas
Si tienes sugerencias, problemas o deseas contribuir, no dudes en abrir un issue o pull request en este repositorio. ¡Gracias por usar el script!
