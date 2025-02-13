# API SATCLIN para análise de feedbacks de pacientes

## Descrição do Projeto
Este projeto foi desenvolvido como parte da disciplina **Construção de APIs para Inteligencia Artificial** da pós-graduação em **Sistemas e Agentes Inteligentes da UFG**. A API foi construída utilizando o **FastAPI** e tem como objetivo fornecer 2 serviços de inteligência artificial na área da saúde: análise de sentimentos dos pacientes de uma unidade de saúde e a geração de texto a partir do feedback para um aprimoramento constante.

## Alunos:
  - Samantha Adiely Alecrim
  - Edson Laranjeiras
  - Billy Fádel
    
## Funcionalidades
- Análise de sentimento: Utiliza um modelo de linguagem (LLM), para classificar um texto como positivo, neutro ou negativo. No contexto da área da saúde, para obter feedbacks de pacientes.
- Geração de texto: Com base no feedback do paciente, gera sugestões de melhorias contínuas para a unidade de saúde, utilizando IA.

## Instalação

1.  Clone este repositório:

- git clone https://github.com/Adiely/projeto_API.git

2.  Crie e ative um ambiente virtual:

- venv\Scripts\activate     # Ativar no Windows

3.  Instale as dependências:

- pip install -r requirements.txt


## Execução
1. Rodar o servidor FastAPI
- 

2. Testar os endpoints
 A API estará disponível em:

- Documentação Swagger: http://127.0.0.1:8000/docs
- Documentação Redoc: http://127.0.0.1:8000/redoc
