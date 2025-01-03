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
    response = {"segments": []}

    for i, segmento in enumerate(segmentos, start=1):
        response["segments"].append({
            "id": i,
            "distance": round(segmento["distancia"], 2),
            "totalAscent": round(segmento["ascenso_acumulado"], 2),
            "totalDescent": round(segmento["descenso_acumulado"], 2),
            "mideTime": round(segmento["t_mide"], 2),
            "actualTime": round(segmento["t_extra"], 2),
            "koticApproved": segmento["val_kotic"],
            "experienceApproved": segmento["val_exp"]
        })

    response["overall"] = {
        "koticApproved": all(s["val_kotic"] for s in segmentos),
        "experienceApproved": all(s["val_exp"] for s in segmentos)
    }

    return response

# this is a get query really but we are using post to allow file uploads, so a file can be used as a parameter
@app.post("/query-gpx/")
async def query_gpx(
    file: UploadFile = File(...),
    rama_id: int = 0,
    tipos_camino_id: list[int] = [],
    mochila_id: int = 0) -> str:
    
    gpxContents = await file.read()

    # check if the file is a valid gpx file
    try:
        gpx_content = gpxContents.decode('utf-8')
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
    jsonResponse = parse_seg_info(procesar_gpx(gpx, rama_id, tipos_camino_id, mochila_id))
    return JSONResponse(content=jsonResponse)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)