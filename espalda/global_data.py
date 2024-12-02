class Global_data():
    def __init__(self):
        self.aemet()
        self.cte_gpx()

    def aemet(self):
        self.url_prediccion_h_municipio = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/horaria/"
        self.url_prediccion_h_municipio_1 = "https://opendata.aemet.es/opendata/api/prediccion/especifica/montaña/pasada/area/"
        self.url_prediccion_h_municipio_2 = "/dia/"

    def cte_gpx(self):
        self.t_max_kotic = {
            'Castores': 2,
            'Lobatos': 3,
            'Tropa': 4,
            'Pios': 6,
            'Clan': 6,
        }

        self.t_max_exp = {
            'Castores': 3,
            'Lobatos': 5,
            'Tropa': 7,
            'Pios': 9,
            'Clan': 10,
        }

        self.t_extra = {
            'Castores': 0.7,
            'Lobatos': 0.55,
            'Tropa': 0.35,
            'Pios': 0.25,
            'Clan': 0.2,
        }

        self.t_mochila = {
            'Si': 0,
            'No': -0.1,
        }
