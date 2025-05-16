# este codigo es una implementación de la interfaz grafica para la aplicación de revisión de travesías en local. 
# no es necesario para el funcionamiento de la api y se mantiene aqui como referencia por si acaso para 
# matener otras partes del proyecto
import tkinter as tk
from tkinter import filedialog
import pandas as pd

from gpx_process import *

class Interfaz:
    def __init__(self, root):
        self.gpx_process = Gpx_process()

        self.root = root
        self.root.title("Procesador de archivos GPX")

        self.open_button = tk.Button(self.root, text="Abrir archivo GPX", command=self.mostrar_puntos)
        self.open_button.pack(pady=10)

        self.text_box = tk.Text(self.root, height=20, width=50)
        self.text_box.pack(padx=10, pady=10)

        #  Definir vectores para las opciones de Rama y Tipo de camino
        self.opciones_rama = ["Castores", "Lobatos", "Tropa", "Pios", "Clan"]
        self.opciones_tipo_camino = ["Pista", "Sendero", "Malos caminos"]
        self.opciones_mochila = ["Si", "No"]

        # Botón de cálculo
        self.calcular_button = tk.Button(self.root, text="Calcular", command=self.realizar_calculo)
        self.calcular_button.pack(pady=10)

    def mostrar_puntos(self):
        """
        Abre un cuadro de diálogo para seleccionar un archivo GPX, procesa el archivo y muestra los segmentos en la interfaz gráfica.
        Esta función realiza las siguientes acciones:
        1. Abre un cuadro de diálogo para que el usuario seleccione un archivo GPX.
        2. Procesa el archivo GPX seleccionado y obtiene los segmentos.
        3. Limpia el contenido anterior del cuadro de texto.
        4. Muestra desplegables para seleccionar las variables "Rama" y "Mochila".
        5. Para cada segmento, muestra un desplegable para seleccionar el tipo de camino y lo añade a la interfaz gráfica.
        Variables de instancia:
        - self.segmentos: Lista de segmentos obtenidos del archivo GPX.
        - self.rama_variable: Variable de cadena para el desplegable de "Rama".
        - self.mochila_variable: Variable de cadena para el desplegable de "Mochila".
        - self.tipo_camino_var: Lista de variables de cadena para los desplegables de tipo de camino.
        Dependencias:
        - filedialog: Para abrir el cuadro de diálogo de selección de archivos.
        - tk: Para manipular la interfaz gráfica.
        - self.gpx_process: Objeto que procesa el archivo GPX.
        - self.opciones_rama: Opciones disponibles para el desplegable de "Rama".
        - self.opciones_mochila: Opciones disponibles para el desplegable de "Mochila".
        - self.opciones_tipo_camino: Opciones disponibles para los desplegables de tipo de camino.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Archivos GPX", "*.gpx")])
        if file_path:
            self.segmentos = self.gpx_process.procesar_archivo(file_path)
            # Limpiar el contenido anterior
            self.text_box.delete('1.0', tk.END)

            # Desplegable para seleccionar la variable Rama
            rama_label = tk.Label(self.root, text="Rama:")
            rama_label.pack()
            self.rama_variable = tk.StringVar(self.root)
            rama_dropdown = tk.OptionMenu(self.root, self.rama_variable, *self.opciones_rama)
            rama_dropdown.pack()

            # Desplegable para seleccionar la variable Mochila
            mochila_label = tk.Label(self.root, text="Con mochila grande:")
            mochila_label.pack()
            self.mochila_variable = tk.StringVar(self.root)
            mochila_dropdown = tk.OptionMenu(self.root, self.mochila_variable, *self.opciones_mochila)
            mochila_dropdown.pack()

            self.tipo_camino_var = []
            # Mostrar los segmentos en el cuadro de texto
            for i, segmento in enumerate(self.segmentos, start=1):
                
                # Desplegable para seleccionar el tipo de camino
                tipo_camino_label = tk.Label(self.root, text="Tipo de camino (D"+str(i)+") :")
                tipo_camino_label.pack()
                tipo_camino_variable = tk.StringVar(self.root)
                self.tipo_camino_var.append(tipo_camino_variable)
                tipo_camino_dropdown = tk.OptionMenu(self.root, tipo_camino_variable, *self.opciones_tipo_camino)
                tipo_camino_dropdown.pack()

                # self.text_box.insert(tk.END, '\n')

                

                # Obtener el valor seleccionado en el desplegable de Tipo de camino
                # tipo_camino = tipo_camino_variable.get()
                # self.tipo_camino.append(tipo_camino_variable.get())
                # Escribir los valores seleccionados en el cuadro de texto
                

    def realizar_calculo(self):
        """
        Realiza el cálculo de los segmentos de una ruta y actualiza la interfaz gráfica con los resultados.
        Este método obtiene los valores seleccionados en los desplegables de 'Rama' y 'Mochila', 
        procesa cada segmento de la ruta utilizando estos valores y los parámetros seleccionados 
        para cada segmento, y muestra los resultados en un cuadro de texto.
        También crea un DataFrame con los resultados de los segmentos y evalúa si todos los segmentos 
        son aceptables según dos criterios: Kotic y Experiencia.
        Actualiza el cuadro de texto con la valoración general de la ruta según estos criterios.

        """
        
        
        self.tipo_camino = []

        # Obtener el valor seleccionado en el desplegable de Rama
        self.rama = self.rama_variable.get()
        self.mochila = self.mochila_variable.get()


        self.text_box.insert(tk.END, f'Rama seleccionada: {self.rama}\n')
        self.text_box.insert(tk.END, f'¿Con mochila?: {self.mochila}\n\n')

        for i, segmento in enumerate(self.segmentos, start=1):
            self.tipo_camino.append(self.tipo_camino_var[i-1].get())
            segmento = self.gpx_process.calculo_segmento(self.rama, segmento, self.tipo_camino[i-1], self.mochila)
            
            self.text_box.insert(tk.END, f'Segmento {i}:\n')
            self.text_box.insert(tk.END, f'Distancia: {segmento["distancia"]:.2f} km\n')
            self.text_box.insert(tk.END, f'Ascenso acumulado: {segmento["ascenso_acumulado"]:.2f} metros\n')
            self.text_box.insert(tk.END, f'Descenso acumulado: {segmento["descenso_acumulado"]:.2f} metros\n')
            self.text_box.insert(tk.END, f'Tipo de camino seleccionado para el segmento {i}: {self.tipo_camino[i-1]}\n\n')
            self.text_box.insert(tk.END, f'Tiempo MIDE {i}: {segmento["t_mide"]:.2f}\n')
            self.text_box.insert(tk.END, f'Tiempo real {i}: {segmento["t_extra"]:.2f}\n\n')
            self.text_box.insert(tk.END, f'¿Aceptable según Kotic? {i}: {segmento["val_kotic"]}\n')
            self.text_box.insert(tk.END, f'¿Aceptable según Experiencia? {i}: {segmento["val_exp"]}\n\n')
            self.text_box.insert(tk.END, '\n')

        self.segmentos_df = pd.DataFrame(self.segmentos)
        
        if self.segmentos_df["val_kotic"].sum() == len(self.segmentos_df):
            kotic = True
        else:
            kotic = False

        if self.segmentos_df["val_exp"].sum() == len(self.segmentos_df):
            exp = True
        else:
            exp = False

        self.text_box.insert(tk.END, 'VALORACIÓN GENERAL\n')
        self.text_box.insert(tk.END, f'¿Aceptable según Kotic? {i}: {kotic}\n')
        self.text_box.insert(tk.END, f'¿Aceptable según Experiencia? {i}: {exp}\n\n')

# Crear la ventana principal
root = tk.Tk()
interfaz = Interfaz(root)
root.mainloop()

