# -----------------------------------------------------------------------------
# Script para OBS Studio
# Descripción:
# Este script muestra la hora actual en una fuente de texto GDI en OBS Studio,
# permitiendo personalizar el formato de hora, la zona horaria (seleccionable
# desde una lista desplegable), y añadir información como GMT, continente y ciudad.
#
# Autor: SirFrancisDrakesTV
# Fecha: [26/11/2024]
# Versión: 1.0
# -----------------------------------------------------------------------------

import obspython as obs
from datetime import datetime
import pytz

# Variables globales
fuente_texto = ""
zona_horaria = "Europe/Madrid"  # Zona horaria predeterminada
prefijo = "Hora: "  # Texto que aparece antes de la hora
mostrar_gmt = True  # Mostrar GMT
mostrar_continente_ciudad = True  # Mostrar continente y ciudad
formato_24_horas = True  # Usar formato de 24 horas

def obtener_gmt(zona_horaria):
    """Obtiene el GMT correspondiente a la zona horaria."""
    ahora = datetime.now(pytz.timezone(zona_horaria))
    offset = ahora.utcoffset().total_seconds() / 3600  # Convertir a horas
    gmt = f"GMT{'+' if offset >= 0 else ''}{int(offset)}"
    return gmt

def actualizar_hora():
    """Actualiza el texto de la fuente con la hora actual y opciones configuradas."""
    global fuente_texto, zona_horaria, prefijo, mostrar_gmt, mostrar_continente_ciudad, formato_24_horas

    if fuente_texto:
        # Obtiene la fuente de texto
        fuente = obs.obs_get_source_by_name(fuente_texto)
        if fuente:
            # Obtiene la hora actual en la zona horaria especificada
            ahora = datetime.now(pytz.timezone(zona_horaria))
            formato_hora = "%H:%M:%S" if formato_24_horas else "%I:%M:%S %p"
            hora_actual = ahora.strftime(formato_hora)

            # Construye el texto final
            texto_final = f"{prefijo}{hora_actual}"

            # Añade GMT si está activado
            if mostrar_gmt:
                gmt = obtener_gmt(zona_horaria)
                texto_final += f" | {gmt}"

            # Añade continente y ciudad si está activado
            if mostrar_continente_ciudad:
                try:
                    continente, ciudad = zona_horaria.split("/")
                except ValueError:
                    continente, ciudad = "Desconocido", "Desconocido"
                texto_final += f" | {continente}/{ciudad}"

            # Actualiza el texto de la fuente
            settings = obs.obs_data_create()
            obs.obs_data_set_string(settings, "text", texto_final)
            obs.obs_source_update(fuente, settings)
            obs.obs_data_release(settings)
            obs.obs_source_release(fuente)

def script_update(settings):
    """Actualiza las variables cuando cambian en el script."""
    global fuente_texto, zona_horaria, prefijo, mostrar_gmt, mostrar_continente_ciudad, formato_24_horas
    fuente_texto = obs.obs_data_get_string(settings, "fuente_texto")
    zona_horaria = obs.obs_data_get_string(settings, "zona_horaria")
    prefijo = obs.obs_data_get_string(settings, "prefijo")
    mostrar_gmt = obs.obs_data_get_bool(settings, "mostrar_gmt")
    mostrar_continente_ciudad = obs.obs_data_get_bool(settings, "mostrar_continente_ciudad")
    formato_24_horas = obs.obs_data_get_bool(settings, "formato_24_horas")

def script_properties():
    """Crea las propiedades que aparecen en el panel de configuración del script."""
    props = obs.obs_properties_create()

    # Propiedad para seleccionar la fuente de texto
    obs.obs_properties_add_text(props, "fuente_texto", "Fuente de Texto GDI", obs.OBS_TEXT_DEFAULT)

    # Propiedad para configurar la zona horaria
    prop_zona_horaria = obs.obs_properties_add_list(
        props, "zona_horaria", "Zona Horaria (País/Región)",
        obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING
    )

    # Agrega las zonas horarias disponibles en pytz
    for tz in pytz.all_timezones:
        obs.obs_property_list_add_string(prop_zona_horaria, tz, tz)

    # Propiedad para configurar el prefijo antes de la hora
    obs.obs_properties_add_text(props, "prefijo", "Texto antes de la hora", obs.OBS_TEXT_DEFAULT)

    # Propiedad para habilitar o deshabilitar GMT
    obs.obs_properties_add_bool(props, "mostrar_gmt", "Mostrar GMT")

    # Propiedad para habilitar o deshabilitar continente y ciudad
    obs.obs_properties_add_bool(props, "mostrar_continente_ciudad", "Mostrar Continente/Ciudad")

    # Propiedad para elegir entre formato de 24 o 12 horas
    obs.obs_properties_add_bool(props, "formato_24_horas", "Formato 24 Horas (Desactiva para 12 horas)")

    return props

def script_load(settings):
    """Configura un temporizador que actualiza la hora cada segundo."""
    obs.timer_add(actualizar_hora, 1000)

def script_unload():
    """Elimina el temporizador cuando el script se descarga."""
    obs.timer_remove(actualizar_hora)

# -----------------------------------------------------------------------------
# Este script fue creado por SirFrancisDrakesTV
# -----------------------------------------------------------------------------
