from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

def generar_resumen(contenido, clave_api):
    """
    Genera un resumen del contenido dado utilizando OpenAI a través de LangChain.

    Parámetros:
        contenido (str): Texto a resumir.
        clave_api (str): Clave de API de OpenAI.

    Retorna:
        str: El resumen generado por el modelo.
    """
    # Inicializar el modelo
    chat = ChatOpenAI(
        model_name="gpt-4o-mini",  # O gpt-3.5-turbo, etc.
        temperature=0.3,
        openai_api_key=clave_api
    )

    # Componer el mensaje
    mensajes = [
        SystemMessage(content="Eres un asistente de investigación útil."),
        HumanMessage(content=f"Por favor, resume la siguiente información:\n\n{contenido}")
    ]

    # Obtener la respuesta
    respuesta = chat(mensajes)

    return respuesta.content
