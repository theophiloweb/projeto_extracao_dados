# Projeto Extração de Dados ETL - Santander Coders 2024 🚀

![ETL Pipeline](https://media.istockphoto.com/id/1369267861/pt/vetorial/etl-extract-transform-load-acronym.jpg?s=612x612&w=0&k=20&c=MSVfVQY61F_CS_vuxPPc-S98W4aYZka6G5yNgnvD0wA=)


Este projeto faz parte do curso de Engenharia de Dados do programa Santander Coders 2024 em parceria com a Ada Tech, focado na trilha de extração de dados. A ideia principal é criar um pipeline de ETL (Extração, Transformação e Carga) utilizando a API do TheMovieDB (TMDB) para extrair informações sobre filmes e séries de TV. O projeto é acadêmico e tem como orientador o professor Lauro, Cientista de Dados.

## 📚 Equipe
Amanda Almeida<br>
Angel Salvino<br>
Naiara Andrade<br>
Francisco das Chagas Teófilo da Silva
## 🎯 Objetivo
O objetivo deste projeto é demonstrar a construção de um pipeline ETL em Python, onde é possível:

Selecionar o tipo (filme ou série de TV).<br>
Escolher um ano específico para a busca.<br>
Extrair dados da API TMDB.<br>
Armazenar os dados em um arquivo Parquet para análise posterior.

## 🛠️ Tecnologias Utilizadas


Linguagem: Python (>= 3.10)<br>
Java: Versão 21 ou superior<br>
Bibliotecas:
requests: Para requisições HTTP à API do TMDB.<br>
pandas: Manipulação de dados.<br>
numpy: Operações matemáticas.<br>
pyspark.pandas: Manipulação de dados em ambientes distribuídos.<br>
os e json: Operações de sistema e manipulação de JSON.<br>
python-dotenv: Biblioteca que extrai dados do arquivo .env.<br>
## 📦 Pré-requisitos
Antes de rodar o projeto, certifique-se de ter os seguintes pacotes e versões instaladas:

Python >= 3.10<br>
Java >= 21.0.2<br>
Instale as bibliotecas Python necessárias:
```
pip install requests pandas numpy pyspark pyarrow python-dotenv
```
## 🔑 Como Obter sua Própria API Key no TMDB
Para utilizar o projeto sem se preocupar com os limites de requisições, recomendamos que cada membro da equipe crie sua própria API Key. Siga os passos abaixo:

Acesse o site do TheMovieDB (TMDB).<br>
Crie uma conta gratuita ou faça login, caso já tenha uma.<br>
Navegue até as configurações da sua conta e vá para a seção API.<br>
Solicite uma nova chave de API.<br>
Copie a chave gerada e adicione ao arquivo .env conforme indicado abaixo:<br>

## 🗂️ Configuração do Arquivo .env
Crie um arquivo .env na raiz do projeto e adicione sua chave da API:

``` makefile
TMDB_API_KEY=YOUR_API_KEY_HERE
```
Substitua YOUR_API_KEY_HERE pela sua chave de API.

## 🚀 Como Executar
Clone o repositório:

```bash
git clone git@github.com:theophiloweb/projeto_extracao_dados.git
```
Navegue para o diretório do projeto:

```bash
cd projeto_extracao_dados
```
Execute o arquivo movie.py ou utilize o Jupyter Notebook movie.ipynb para rodar o processo de ETL:

```bash
python movie.py
```
## 📂 Estrutura do Projeto
movie.py: Código Python com a lógica de extração de dados da API, transformação e armazenamento em formato Parquet.<br>
movie.ipynb: Jupyter Notebook com o mesmo conteúdo do movie.py para facilitar a visualização e execução passo a passo.<br>
.env: Arquivo para armazenar a chave da API (não é compartilhado no repositório).<br>
README.md: Documentação do projeto.<br>

## 📜 Licença
Este projeto é licenciado sob a licença MIT. Sinta-se à vontade para clonar, modificar e contribuir!

## 📧 Contato
Caso tenha alguma dúvida ou queira colaborar com o projeto, entre em contato através do meu LinkedIn.

## ⭐ Agradecimentos
Agradeço à ADA Tech e ao Santander Coders pela oportunidade de aprendizado e desenvolvimento deste projeto.