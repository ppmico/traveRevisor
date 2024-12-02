from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from interfaz import procesar_gpx
from fastapi.middleware.cors import CORSMiddleware
import gpxpy


app = FastAPI()

app.add_middleware( # para que el navegador no bloquee la respuesta (le mete cabecera)
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of origins or use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods like GET, POST, etc.
    allow_headers=["*"],  # Allow all headers
)


def parse_seg_info(segmentos):
    output = ''

    for i, segmento in enumerate(segmentos, start=1):
        output += f'Segmento {i}:\n'
        output += f'Distancia: {segmento["distancia"]:.2f} km\n'
        output += f'Ascenso acumulado: {segmento["ascenso_acumulado"]:.2f} metros\n'
        output += f'Descenso acumulado: {segmento["descenso_acumulado"]:.2f} metros\n'
        # output += f'Tipo de camino seleccionado para el segmento {i}: {self.tipo_camino[i-1]}\n\n'
        output += f'Tiempo MIDE {i}: {segmento["t_mide"]:.2f}\n'
        output += f'Tiempo real {i}: {segmento["t_extra"]:.2f}\n\n'
        output += f'¿Aceptable según Kotic? {i}: {segmento["val_kotic"]}\n'
        output += f'¿Aceptable según Experiencia? {i}: {segmento["val_exp"]}\n\n'
        output += '\n'

    # si todos los segmentos son aceptables según Kotic y Experiencia, entonces la ruta es aceptable
    kotic = all(segmento["val_kotic"] for segmento in segmentos)
    exp = all(segmento["val_exp"] for segmento in segmentos)

    output += 'VALORACIÓN GENERAL\n'
    output += f'¿Aceptable según Kotic? {i}: {kotic}\n'
    output += f'¿Aceptable según Experiencia? {i}: {exp}\n\n'
    
    return output

# this is a get query really but we are using post to allow file uploads, so a file can be used as a parameter
@app.post("/query-gpx/")
async def query_gpx(
    file: UploadFile = File(...),
    rama_id: int = 0,
    tipos_camino_id: list[int] = [],
    mochila_id: int = 0) -> str:
    
    contents = await file.read()

    # check if the file is a valid gpx file
    try:
        gpx_content = contents.decode('utf-8')
        gpx = gpxpy.parse(gpx_content)
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": "Failed to parse GPX file", "error": str(e)})

    # check si len(tipos_camino_id) == nº segmentos en el gpx
    if len(tipos_camino_id) != sum(len(track.segments) for track in gpx.tracks):
        return JSONResponse(status_code=400, content={"message": "Invalid tipos_camino_id", "error": "len(tipos_camino_id) must be equal to the number of segments in the GPX file"})
    
    # check si los ids son validos
    if rama_id < 0 or rama_id > 4:
        return JSONResponse(status_code=400, content={"message": "Invalid rama_id", "error": "rama_id must be between 0 and 4"})
    if not all(0 <= tipo <= 2 for tipo in tipos_camino_id):
        return JSONResponse(status_code=400, content={"message": "Invalid tipos_camino_id", "error": "Each tipos_camino_id must be between 0 and 2"})
    if mochila_id < 0 or mochila_id > 1:
        return JSONResponse(status_code=400, content={"message": "Invalid mochila_id", "error": "mochila_id must be between 0 and 1"})
    
    # procesar el gpx
        
    return parse_seg_info(procesar_gpx(gpx, rama_id, tipos_camino_id, mochila_id))

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)