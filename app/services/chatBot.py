from openai import OpenAI

client = OpenAI(api_key="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")  # coloca aquí tu API key

async def generar_respuesta_openai(mensaje: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente legal confiable."},
                {"role": "user", "content": mensaje}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Error al consultar OpenAI: {str(e)}")