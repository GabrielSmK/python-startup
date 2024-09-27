from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_ideia_startup(input_usuario):
    resposta = client.chat.completions.create(
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model = "gpt-4",
        messages = [
            {
                "role": "system", 
                "content": "Você é um assistente inteligente."
            },
            {
                "role": "user",
                "content": input_usuario
            }
        ],
    )
    return resposta.choices[0].message.content

input_usuario = input("Digite o que deseja: ")
startup_ideias = gerar_ideia_startup(input_usuario)
print("Ideias de Startup:", startup_ideias)