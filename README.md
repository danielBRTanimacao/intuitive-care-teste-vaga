# Intuitive Care testes vaga 📚

> Repositorio criado para resolver testes cotidianos com programação utilizando tecnologias como, Java, Python e Vue.js.

## Requisitos ⚙️

Antes de clonar o projeto é necessario instalar as seguintes tecnologias

### DataBase 🐋

-   Necessario `PostgreSql`
-   `Dbeaver` (recomendado)

### BACKEND 🌑

-   Necessario ter `python3+` instalado.
-   Requisito `git` para clonar.
-   Sua maquina `Windows`, `Linux` ou `Mac`.
-   Necessario baixar `Java SDK`.

### FRONTEND ☀️

-   Necessario instalar `Node.js`.
-   `npm`ou `yarn` instalado para gerenciar pacotes.

### Clonando projeto

```
git clone https://github.com/danielBRTanimacao/intuitive-care-teste-vaga.git
```

Abrindo o projeto configurando ambiente de desenvolvimento

se você estiver no windows o comando para ativar o `venv` python é
`venv/scripts/activate`

```
cd intuitive-care-teste-vaga

python3 -m venv venv
source venv/bin/activate
pip -r requirements.txt
```

### Primeiro teste diretorio `test-web-scraping`

Como rodar o teste, basta apenas rodar o `main.py` na pasta `test-web-scraping` ele automaticamente ira fazer os requests e salvar os arquivos necessarios

### Segundo teste diretorio `test-transform-data`

Para o segundo teste basta modificar a linha 11 na `main.py`

```
your_name = "Daniel"  # Pode alterar o nome
```

### Terceiro teste diretorio `test-data-base`

Para rodar o script recomende utilizar uma interface como o `dbeaver`

#### Como instalar dbeaver linux

```
sudo snap install dbeaver-ce
```

#### Como instalar no windows / MacOS

Link direto pela [documentação oficial](https://dbeaver.io/download/)

#### Abrindo o Dbeaver

Crie o projeto `PostgreSql` abra as tabela e o `script.sql` em `test-data-base`

Altere o caminho dos arquivos se for rodar o `psql` localmente

```
'/home/danie/Programação/intuitive-care-teste-vaga/csvs/Relatorio_cadop.csv'
```

importe o arquivo csv e rode query por query

### Quarto teste diretorio `test-api`

Abra dois terminais entre no diretorio `/backend/main.py` rode a aplicação

esse e o backend da aplicação não precisa ser alterado nada

Para rodar o front end entre no diretorio `/frontend/`

instale as dependencias node

```
npm i
npm run dev
```
