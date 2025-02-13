# API SATCLIN para análise de feedbacks de pacientes

## Descrição do Projeto
Este projeto foi desenvolvido como parte da disciplina **Construção de APIs para Inteligencia Artificial** da pós-graduação em **Sistemas e Agentes Inteligentes da UFG**. 
A API foi construída utilizando o **FastAPI** e tem como objetivo fornecer 2 serviços de inteligencia artificial na área da saúde:
- Análise de sentimentos dos feedbacks dos pacientes de uma unidade de saúde. 
- Geração de texto baseada nos feedbacks para sugerir melhorias contínuas.

## Equipe
  - Samantha Adiely Alecrim
  - Edson Laranjeiras
  - Billy Fádel
    
## Funcionalidades
1. Análise de sentimento
- Utiliza um modelo de linguagem natural (LLM), para classificar um texto como Positivo, Neutro ou Negativo. 
- Aplicação na área da saúde: auxiliar na interpretação dos feedbacks de pacientes, ajudando na tomada de decisões. 
2. Geração de texto
- Com base no feedback do paciente, gera sugestões de melhorias contínuas para a unidade de saúde, utilizando IA.
- Aplicação: Pode ser utilizado por gestores para implementar mudanças baseadas nas percepções dos pacientes.

## Instalação

1.  Clone este repositório:

- git clone https://github.com/Adiely/projeto_API.git

2.  Crie e ative um ambiente virtual:

- python -m venv venv       # Criar um ambiente virtual
- venv\Scripts\activate     # Ativar no Windows

3.  Instale as dependências:
- pip install -r requirements.txt


## Execução
1. Rodar o servidor FastAPI

- fastapi dev main.py
ou 
- uvicorn main:app --host 0.0.0.0 --port 8000 --reload

2. Testar os endpoints

 A API estará disponível em:

- Documentação Swagger (para testar os endpoints): http://127.0.0.1:8000/docs
- Documentação Redoc (documentação): http://127.0.0.1:8000/redoc
