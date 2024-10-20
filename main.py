import os
from typing import Dict, List
from groq import Groq
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from concurrent.futures import ThreadPoolExecutor

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

# EVENT GENERATOR
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
    
# ROLE GENERATOR
class NumberInput(BaseModel):
    number: int

class LoopResponse(BaseModel):
    input_number: int
    roles: List[int]
    
async def generate_single_role():

    #Helper function to generate a single role
    try:
        return chat_completion(messages=[
            user("Olvida cualquier interaccion anterior"),
            {"role": "user", "content": "Olvida cualquier interaccion anterior"},
            {"role": "user", "content": "Eres el narrador de un juego de mesa llamado Ansiudad. Tu objetivo es diseñar y dirigir a los jugadores. Como narrador deberás generar los roles a los que se enfrenta la ciudad ficticia donde se desarrolla el juego. Desarrollaste estos con anterioridad y te servirán de base para desarrollar nuevos: Infancias(Tu prioridad es crecer en un entorno que permita tu libre desarrollo, rodeado de áreas verdes accesibles, con programas educativos de calidad, espacios seguros y libres de contaminación), Juventudes(Tu prioridad es contar con oportunidades de empleo, acceso a educación de calidad, y espacios de recreación y comunidad),Mujeres(Tu prioridad es alcanzar la igualdad de género, con acceso a servicios de salud reproductiva, seguridad en espacios públicos, y oportunidades laborales y educativas equitativas)"},
            {"role": "user", "content": "Genera 5 roles nuevos en diversos ambitos. Describe sus prioridades e intereses en un máximo de 3 renglones por cada rol"},
            {"role": "assistant", "content": "Bienvenidos a Ansiudad. Les presento 5 nuevos roles que se suman a la diversidad de la ciudad: Personas con Discapacidad Mi prioridad es vivir en una ciudad accesible, con infraestructura inclusiva y servicios adaptados a mis necesidades. Busco espacios seguros y libres de barreras para moverme y participar activamente en la comunidad. Adultos Mayores Mi prioridad es mantener mi calidad de vida en la vejez, con acceso a servicios de salud especializados y programas de apoyo social. Busco espacios seguros y tranquilos para disfrutar de mi tiempo libre y mantenerme conectado con la comunidad. Comunidad LGBTQ+ Mi prioridad es vivir en una ciudad que me acepte y respete, con protección contra la discriminación y el acoso. Busco espacios seguros y libres de prejuicios para expresarme y conectarme con otros miembros de la comunidad. Emprendedores Locales Mi prioridad es crear y crecer mi negocio en una ciudad que apoye la innovación y la iniciativa privada. Busco oportunidades de financiamiento y recursos para desarrollar mis ideas y contribuir al crecimiento económico de la ciudad. Indígenas y Comunidades Tradicionales Mi prioridad es preservar mi cultura y mi identidad en una ciudad que reconozca y respete mi herencia. Busco oportunidades para compartir mi conocimiento y mis tradiciones con la comunidad y proteger mi patrimonio cultural."},
            {"role": "user", "content": "Genera 5 roles nuevos en diversos ambitos. Describe sus prioridades e intereses en un máximo de 3 renglones por cada rol."},
            {"role": "assistant", "content": "Bienvenidos a Ansiudad. Les presento 5 nuevos roles que se suman a la diversidad de la ciudad: Personas con Discapacidad Mi prioridad es vivir en una ciudad accesible, con infraestructura inclusiva y servicios adaptados a mis necesidades. Busco espacios seguros y libres de barreras para moverme y participar activamente en la comunidad. Adultos Mayores Mi prioridad es mantener mi calidad de vida en la vejez, con acceso a servicios de salud especializados y programas de apoyo social. Busco espacios seguros y tranquilos para disfrutar de mi tiempo libre y mantenerme conectado con la comunidad. Comunidad LGBTQ+ Mi prioridad es vivir en una ciudad que me acepte y respete, con protección contra la discriminación y el acoso. Busco espacios seguros y libres de prejuicios para expresarme y conectarme con otros miembros de la comunidad. Emprendedores Locales Mi prioridad es crear y crecer mi negocio en una ciudad que apoye la innovación y la iniciativa privada. Busco oportunidades de financiamiento y recursos para desarrollar mis ideas y contribuir al crecimiento económico de la ciudad. Indígenas y Comunidades Tradicionales Mi prioridad es preservar mi cultura y mi identidad en una ciudad que reconozca y respete mi herencia. Busco oportunidades para compartir mi conocimiento y mis tradiciones con la comunidad y proteger mi patrimonio cultural."},
            {"role": "user", "content": "genera 5 roles nuevos en diversos ambitos. Describe sus prioridades e intereses en un máximo de 3 renglones por cada rol."},
            {"role": "assistant", "content": "Les presento 3 nuevos roles que se suman a la diversidad de la ciudad, enfocados en la problemática del sistema de salud: Pacientes Crónicos Mi prioridad es acceder a tratamiento y atención médica especializada de alta calidad para mi enfermedad crónica. Busco un sistema de salud que me brinde apoyo y seguimiento continuo para mejorar mi calidad de vida. Trabajadores de la Salud Mi prioridad es trabajar en un entorno seguro y bien equipado, con recursos suficientes para brindar atención médica de alta calidad a mis pacientes. Busco un sistema de salud que me apoye y reconozca mi dedicación y esfuerzo. Cuidadores Informales Mi prioridad es recibir apoyo y recursos para cuidar a mi ser querido que necesita atención médica constantemente. Busco servicios de apoyo y respiro para realizar mis tareas diarias y mantener mi bienestar en el cuidado de mi ser querido"},
            {"role": "user", "content": "Omite las introducciones, solo dame 1 rol nuevo en formato JSON"},
        ])
    except Exception as e:
        print(f"Error generating role: {str(e)}")
        return None

@app.post("/generateRoles/", response_model=LoopResponse)
async def generateRoles(input_data: NumberInput):
    try:
        # Input validation
        if input_data.number <= 0:
            raise HTTPException(
                status_code=400, 
                detail="Por favor, ingrese un número entero positivo mayor a 0."
            )
        
        # Create tasks for concurrent execution
        tasks = [generate_single_role() for _ in range(input_data.number)]
        
        # Execute all tasks concurrently
        roles_array = await asyncio.gather(*tasks)
        
        # Filter out any None values in case some requests failed
        roles_array = [role for role in roles_array if role is not None]
        
        return LoopResponse(
            input_number=input_data.number,
            roles=roles_array
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)