# NBA CRUD
O projeto em questão trata-se de uma api de times da nba, onde buscamos estudar a integração de alguns serviços da aws. 
A seguir alguns detalhes sobre o projeto, teconologias e como reproduzir o sistema.

### 🏗️ Tecnologias Utilizadas
- Python
- Flask
- Docker
- AWS Lambda
- AWS API Gateway
- AWS RDS
- SQL
- GitHub

### 📁 Estrutura do Projeto
```
nba-crud/
├── app.py 
├── config/ 
├── controller/ 
├── models/
├── repository/ 
├── img/
├── createTable.sql 
├── requirements.txt 
├── Dockerfile 
├── lambda_function.py 
├── lambda_function.zip 
├── lambda_function_requirements.txt 
├── AWS CRUD.pdf 
├── aws.mp4
├── aws.webm 
└── test.sh 
```

### 🚀 Executar Localmente
```
git clone https://github.com/luizTavolaro/nba-crud.git
cd nba-crud

#Linux / MACOS
pip install virtualenv
virtualenv .venv
source .venv/bin/ativate

#Windows
pip install virtualenv
virtualenv .venv
source .venv/Scrpits/activate

pip install -r requirements.txt

python app.py
```

### 🐳 Docker
```
docker build -t nba-crud .
docker run -p 30000:30000 nba-crud
```

### ⚙️ Lambda 
Para o lambda, precisamos fazer um zip com todas as dependência ja instaladas no diretorio e com o zip fazer o deploy da lambda

```
git clone https://github.com/luizTavolaro/nba-function.git
cd nba-function

#Linux / MACOS
pip install virtualenv
virtualenv .venv
source .venv/bin/ativate

#Windows
pip install virtualenv
virtualenv .venv
source .venv/Scrpits/activate

pip install -r requirements.txt -t .
zip -r lambda_function.zip .
```

### 🎥 Apresentação
https://youtu.be/P8erqX1yQk8
