# Vamos importar a bibliotecas necessárias

import requests
import pandas as pd
import numpy as np
import sys
import json
import os
from dotenv import load_dotenv
import pyspark.pandas as ps


# Defina a variável de ambiente
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

# Carregar as variáveis do arquivo .env
load_dotenv()

# Vou criar uma class movie para receber os dados
class Movie:
    def __init__(self, ano:str, tipo:str) -> None:        
        self._api_key =  os.getenv("TMDB_API_KEY") # Chave da API
        self._url_padrao = f"https://api.themoviedb.org/3/discover/{tipo}?first_air_date_year={ano}&include_adult=false&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc"
        self._urlsystem = 'Data/dados_tratados'
        self._ano = ano
        self._tipo = tipo
        self._page = 1
        self._extracao = []
        self._transformacao = None
        self._carga = None
       

    # Vou criar o getters do movie
    @property
    def get_movie(self) -> dict:
        return self.movie 

    # Vou criar o getters do api_key
    @property
    def api_key(self) -> str:
        return self._api_key

    # Vou criar o getters do url_padrao
    @property
    def url_padrao(self) -> str:
        return self._url_padrao
    
    # Vou criar geters do caminho para salvar o arquivo
    @property
    def urlsystem(self) -> str:
        return self._urlsystem

    # Vou criar o getters do page
    @property
    def page(self) -> int:
        return self._page

    @property
    def extracao(self) -> list:
        return self._extracao

    @extracao.setter
    def list_extracao(self, js: dict):
        self._extracao.append(js)

    # Vou criar o geters e seters de ano
    @property
    def ano(self) -> str:
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano 

    # Vou criar geters e Seters de   tipo  
    @property   
    def tipo(self) -> str:
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo


    # Vou criar um método de extração

    def extrair_dados(self) -> list:

          # O Headers
         headers = {
             "accept": "application/json",
             "Authorization": f"Bearer {self.api_key}"
        }
         
         # Vou fazer um loop na URL até chegar ao final  
         dados = []
         contador = 1
        

         while True:                     
               url = f"{self.url_padrao}&page={contador}"
               response = requests.get(url, headers=headers)
               status_code = response.status_code
               if status_code == 200:        
                  js = json.loads(response.text)
                  dados.append(js)
                  self.list_extracao = js                  
                  contador += 1       
               else:
                  break  
               
         return dados  


    def transformar_dados(self) -> None:
        pass

    def carregar_dados(self) -> None:
        pass 


__name__ = '__main__'

option = int(input('Digite:  1 - TV ou 2 - Filme'))
ano = int(input('Digite o ano para extração: Ex: 1993'))

# Vou iniciar e instanciar a class movie
tipo = 'tv' if option == 1 else 'movie'
dado = Movie(str(ano), tipo)

#*****************************************EXTRAÇÃO*********************************************************

# Caminho padrão para salvar o arquivo. Observe que tem que ser da instância "dado" obs: Não sei porquê ainda, mas não aceita mais de um _ no atributo
url = dado.urlsystem
# Nome do arquivo 
nome_arquivo = f'extracao_{tipo}_{ano}.parquet'
# Verifica se o caminho não existe e o cria localmente

if not os.path.exists(url):
    # Criar o diretório
    os.makedirs(url)

df = None
# Verifica se o arquivo não existe e realiza a operação de criação do parquet
if not os.path.isfile(f'{url}/{nome_arquivo}'):
    # Como eu salvei no atributo de lista o resultado de cada página é necessário fazer um loop para converter em dataframe
    dado = dado.extrair_dados()
    df = pd.DataFrame([item for sublist in dado for item in sublist['results']]) # Usando List Comprehension
    df.reset_index()
    df.to_parquet(f'{url}/{nome_arquivo}') 

# A partir daqui será o trabalho de leitura do arquivo, transformação e carga
try:    
    # Ler o arquivo parquet   
    arquivo = pd.read_parquet(f'{url}/{nome_arquivo}', engine='pyarrow')
    # Setando a coluna ID como index do dataframe
    arquivo = arquivo.set_index('id')
    # Verificar quantas linhas e colunas
    print(arquivo.shape)    
except Exception as e:
    # Exibir a mensagem de erro detalhada
    print(f'Erro ao ler o arquivo em parquet: {e}')

# Verificar as 10 primeiras linhas
arquivo.head()

#*****************************************TRANSFORMAÇÃO*********************************************************


#*****************************************CARGA*********************************************************
