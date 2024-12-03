import gpxpy
import tkinter as tk
from tkinter import filedialog
from geopy.distance import geodesic
from global_data import *

class Gpx_process:
    def __init__(self):
        self.global_data = Global_data()

    
    def procesar_archivo(self, file_path):
        """
        Procesa un archivo GPX y calcula la distancia total, el ascenso acumulado y el descenso acumulado
        para cada segmento de la pista.
        Args:
            file_path (str): La ruta del archivo GPX a procesar.
        Returns:
            list: Una lista de diccionarios, cada uno representando un segmento con las siguientes claves:
            - 'distancia' (float): La distancia total del segmento en kilómetros.
            - 'ascenso_acumulado' (float): El ascenso acumulado del segmento en metros.
            - 'descenso_acumulado' (float): El descenso acumulado del segmento en metros.
        """
        with open(file_path, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)

            segmentos = []

            for track in gpx.tracks:
                for segment in track.segments:
                    distancia_segmento = 0
                    ascenso_acumulado = 0
                    descenso_acumulado = 0
                    segmento_puntos = []

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

                    segmentos.append({
                        'distancia': distancia_segmento/1000,
                        'ascenso_acumulado': ascenso_acumulado,
                        'descenso_acumulado': descenso_acumulado
                    })

            return segmentos

    def calculo_segmento(self, rama, segmento, camino, mochila):
        """
        Calculate the segment details based on the given parameters.
        
        Returns:
            dict: The updated segment dictionary with additional keys:
                - 't_mide': The calculated median time.
                - 't_extra': The calculated extra time.
                - 'val_kotic': Boolean indicating if the segment is valid according to KOTIC criteria.
                - 'val_exp': Boolean indicating if the segment is valid according to EXP criteria.
        """

        if camino == 'Pista':
            v = 5
        elif camino == 'Sendero':
            v = 4
        else:
            v = 3
        
        t_h = segmento["distancia"]/v
        t_v = segmento["ascenso_acumulado"]/400 + segmento["descenso_acumulado"]/600
        if t_h > t_v:
            t_mide = t_h + t_v/2
        else:
            t_mide = t_v + t_h/2

        t_extra = t_mide * (1 + (self.global_data.t_extra[rama] + self.global_data.t_mochila[mochila]))

        if t_mide > self.global_data.t_max_kotic[rama]:
            val_kotic = False
        else:
            val_kotic = True

        if t_extra > self.global_data.t_max_exp[rama]:
            val_exp = False
        else:
            val_exp = True

        segmento['t_mide'] = t_mide
        segmento['t_extra'] = t_extra
        segmento['val_kotic'] = val_kotic
        segmento['val_exp'] = val_exp

        return segmento
        
