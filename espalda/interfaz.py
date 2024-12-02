import pandas as pd
from geopy.distance import geodesic
from gpx_process import Gpx_process

# Ramas: Castores: 0, Lobatos: 1, Tropa: 2, Pios: 3, Clan: 4
# Tipos de camino: Pista: 0, Sendero: 1, Malos caminos: 2
# Mochila: Si: 1, No: 0

ramas = ['Castores', 'Lobatos', 'Tropa', 'Pios', 'Clan']
tipos_camino = ['Pista', 'Sendero', 'Malos caminos']
mochila = ['No', 'Si']

def procesar_gpx(gpx_content, rama_id, tipos_camino_id, mochila_id):
    """
    adaptacion de 'procesar_archivo' de gpx_process.py
    """
    segmentos = []
    gpx_processor = Gpx_process()  # Instantiate the Gpx_process class
    
    iSeg = 0 # OJO: esta implementacion no distingue de que track es cada segmento, len(tipos_camino_id) = suma segmentos de todos los tracks
    for track in gpx_content.tracks:
        for segment in track.segments:
            distancia_segmento = 0
            ascenso_acumulado = 0
            descenso_acumulado = 0

            prev_point = None
            for point in segment.points:
                # Guardar el primer punto del segmento
                if prev_point is None:
                    prev_point = point
                    continue

                # Calcular distancia entre puntos utilizando geopy
                distancia_puntos = geodesic((prev_point.latitude, prev_point.longitude), (point.latitude, point.longitude)).meters
                distancia_segmento += distancia_puntos

                # Calcular ascenso y descenso
                elevacion_diff = point.elevation - prev_point.elevation
                if elevacion_diff > 0:
                    ascenso_acumulado += elevacion_diff
                else:
                    descenso_acumulado += abs(elevacion_diff)

                # Guardar punto para futuras referencias
                prev_point = point

            segmento = {
                'distancia': distancia_segmento/1000,
                'ascenso_acumulado': ascenso_acumulado,
                'descenso_acumulado': descenso_acumulado
            }

            segmento = gpx_processor.calculo_segmento(ramas[rama_id], segmento, tipos_camino[tipos_camino_id[iSeg]], mochila[mochila_id]) 

            segmentos.append(segmento)
            iSeg += 1 # para acceder al tipo_camino del siguiente segmento en el gpx

    return segmentos