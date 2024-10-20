import os
from typing import Dict, List
from groq import Groq
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class RequestBody(BaseModel):
    size: str
    
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # allow_origins=["http://localhost:5173"],  # ALLOW DEVELOPMENT ORIGIN
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

LLAMA3_2_90B = "llama-3.2-90b-vision-preview"

DEFAULT_MODEL = LLAMA3_2_90B

client = Groq()

def assistant(content: str):
    return { "role": "assistant", "content": content }

def user(content: str):
    return { "role": "user", "content": content }

def chat_completion(
    messages: List[Dict],
    model = DEFAULT_MODEL,
    temperature: float = 0.9,
    top_p: float = 0.9,
) -> str:
    response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        top_p=top_p,
    )
    return response.choices[0].message.content

@app.get("/generateEvents/")
def generateEvents():
    try:
        return chat_completion(messages=[
            user("Olvida cualquier interaccion anterior"),
            user("Eres el narrador de un juego de mesa llamado ciudad, cuyo objetivo es diseñar y dirigir los escenarios que enfrentan los jugadores. Como narrador, deberás delimitar los incidentes a los que se enfrenta la ciudad ficticia donde se desarrolla el juego. Historia: El gobierno de ciudad está desbordado y necesita la creatividad e innovación de sus ansiudadanxs para enfrentar incidentes inesperados que han azotado a la metrópoli."),
            user("Movilidad y transporte: Incidente: Una misteriosa criatura gigante ha emergido del subsuelo, dañando gravemente la línea del metro de ciudad. No se reportan heridos."),
            user("Manejo de desechos: Incidente: Los altos niveles de toxicidad en el vertedero de ciudad han otorgado a las ratas súper fuerza y resistencia a los raticidas."),
            assistant("Erupción fitoplanctónica: Incidente: Un fenómeno misterioso ha desatado una explosión de fitoplancton en el lago de ciudad, creando una iridiscente 'niebla verde' que ahoga la vida acuática y perturba el equilibrio del ecosistema. Prompt para los jugadores: Presenta una solución para controlar el crecimiento desenfrenado de fitoplancton y restaurar el equilibrio en el lago. Noticia: Investigadores han hallado que la niebla verde podría ser impulsada por una forma de vida extinta hace siglos, que alberga propiedades curativas desconocidas. Noticia: Los habitantes locales comienzan a explotar la niebla verde para crear productos farmacéuticos, ignorando las posibles consecuencias a largo plazo para su entorno."),
            user("menos detalles, más conciso "),
            assistant("Invasión fitoplanctónica: Incidente: Una misteriosa explosión de fitoplancton ha invadido el lago de ciudad, ahogando la vida acuática. Prompt para los jugadores: Presenta una solución para controlar el crecimiento desenfrenado de fitoplancton. Noticia: Científicos han hallado que la invasión podría estar relacionada con una forma de vida extinta desde hace siglos. Noticia: Empresarios locales intentan aprovechar el fitoplancton para crear productos rentables."),
            user("da un toque de fantasía"),
            assistant("Saturación WI-FI: Incidente: La red de wifi de ciudad se ha vuelto autónoma y ahora comparte memes y videos de gatos en todos los dispositivos de la ciudad, provocando una ola de apatía y distracción masiva."),
            {"role": "user", "content": "enfocate en los retos a los que se enfrentan grandes ciudades en el presente, un toque de humor, da solo 2 o 3 enunciados"},
        ])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)