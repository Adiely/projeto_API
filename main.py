from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel
from enum import Enum
import logging
from transformers import pipeline

# Configuração do log (serve para identificar possiveis erros e realizar auditorias)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("fastapi")

# Segurança - Autenticação simples via token (Testar com JWT tokens depois)
API_TOKEN = 123

# Definição de grupos de endpoints (para tags)
class NomeGrupo(str, Enum):
    ia_services = "Serviços de IA"

description = f"""
    Aqui podemos verificar o esquema dos endpoints dessa API que utiliza modelos de IA para análise de sentimentos e sugestões baseadas nos feedbacks de pacientes.

    - /sentiment-analysis: Classifica o feedbacks como Positivo, Neutro ou Negativo.
    - /generate-text: Sugestões de melhoria com base no feedback recebido.
"""

# Criar uma instância para a classe FastAPI
app = FastAPI(
    title="API SATCLIN - IA para Feedbacks de pacientes",
    description=description,
    version="1.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Billy Fádel, Edson Laranjeiras e Samantha Alecrim",
        "url": "http://github.com/Adiely/",
        "email": "samanthaalecrim.biotec@gmail.com",
    },
     license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# MODELOS DE DADOS 
class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float

class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 100

class TextGenerationResponse(BaseModel):
    generated_text: str

# AUTENTICAÇÃO SIMPLES 
def check_api_token(api_token: int):
    if api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="API Token inválido")
    
# CONFIGURAÇÃO DOS SERVIÇOS DE IA
sentiment_pipeline = pipeline("sentiment-analysis")
text_generator = pipeline("text-generation", model="gpt2")  

# Nos endpoints: define um decorador de rota, que será responsável por tratar as requisições que vão 
# para as rotas: /sentiment-analysis/ e /generate-text/ usando o POST.
# Nas funções da rota: recebe um texto e retorna o conteúdo , Se o sentimento é POSITIVO, NEGATIVO ou NEUTRO)

# ENDPOINTS
@app.post(
    path="/v1/sentiment-analysis/{api_token}", 
    response_model=SentimentResponse, 
    tags=[NomeGrupo.ia_services],
    summary="Envio de dados para Análise de Sentimento",
    description="Endpoint que aceita requisições para envio de dados de Análise de Sentimento"
    )
def sentiment_analysis(request: SentimentRequest, api_token: int):
    check_api_token(api_token)
    logger.info(f"Analisando sentimento do texto: {request.text}")
    try:
        result = sentiment_pipeline(request.text)[0]
        return SentimentResponse(sentiment=result["label"], confidence=result["score"])
    except Exception as e:
        logger.error(f"Erro na análise de sentimento: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno ao analisar sentimento")
    
@app.post(
    path="/v1/generate-text/{api_token}", 
    response_model=TextGenerationResponse, 
    tags=[NomeGrupo.ia_services],
    summary="Envio de dados para gerar sugestões de melhoria com base no feedback fornecido",
    description="Endpoint que aceita requisições para envio de dados de Geração de texto"
    )  

def generate_text(request: TextGenerationRequest, api_token: int):
    check_api_token(api_token)
    logger.info(f"Gerando texto para o prompt: {request.prompt}")

    try:
        result = text_generator(request.prompt, max_length=request.max_length, num_return_sequences=1)
        return TextGenerationResponse(generated_text=result[0]["generated_text"])
    except Exception as e:
        logger.error(f"Erro na geração de texto: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno ao gerar texto")

@app.get(
    path="/v1/teste", 
    summary="Verificar se API está funcionando",
    description="Endpoint que aceita requisições para verificar se a API está rodando",
    tags=[NomeGrupo.ia_services])

def check_API():
    return {"mensagem": "A API está rodando corretamente"}
