from flask import Flask, request, jsonify
import os
import sqlite3


#Inicia o flask
app = Flask(__name__)

#cria um banco de dados chamado livros.db na pasta BANCO_DADOS, assim como o caminho até o banco
livros_db = os.path.join(os.path.dirname(__file__), '..', 'BANCO_DADOS', 'livros.db')

#Conetar ao banco de dados
def conectar_db():
    #conn = variavel que conctada no banco através do sql.connct
    conn = sqlite3.connect(livros_db)
    return conn

#Funsão que cria o banco de dados caso ele não exista assim como suas tabelas
def criar_banco():
    #Concectar ao banco de dados
    conn = conectar_db()
    #Cria um cursor para manipular o sql através de comandos
    cursor = conn.cursor()

    #-----Sessão onde vai ocorrer a criação da tabela de livros no banco de dados-----
    
    #Executa as funções do cursor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   autor TEXT,
                   capa_url TEXT,
                   sinopse TEXT,
                   preco FLOAT,                  
                   quantidade_estoque INTERGER DEFAULT 0,
                   qrcode TEXT UNIQUE)''')
    #------------------------------------------------------------------------------------


    #Sessão onde vai criar a  tabela de temas/categoria de livros, como por exemplo, ação, aventura, fantasia e etc...
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS temas (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   tema TEXT)''')
    #--------------------------------------------------------


    #-----Sessão onde vai ficar a tabela que liga o livro a seu tema-----
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livro_tema (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   livro_id INTEGER NOT NULL,
                   tema_id INTEGER NOT NULL,
                   FOREIGN KEY (livro_id) REFERENCES livros (id),
                   FOREIGN KEY (tema_id) REFERENCES temas (id)
                   );''')
    #--------------------------------------------------------

    #Salva as mudanças
    conn.commit()
    #Fecha conexão
    conn.close()

@app.route("/BACKEND_ESTOQUE_LOGISTICA", methods=["POST"])
def cadastro_livros():

    #Variavel que faz a coleta dos dados enviados do Front-end através do JSON e tranforma em um dicionário
    livros = request.json

    #Variaveis que coleta cada dado separadamente do dicionário, para assim colocar em sua respectiva coluna no Banco de Dados 
    nome = livros['nome']



    conn = conectar_db()
    cursor = conn.cursor()

    #Sessão de código responsavel pela criação automática de um texto "Livro:1/Livro:2/Livro:3..." que será cadastrado na coluna do QRCODE, para gerar um código futuramente
    cursor.execute("SELECT COUNT(*) FROM livros") #Conta o total de linhas no banco de dados e retorna o valor
    contador = cursor.fetchone()[0] #Armazena o número retornado do comando acima

    #Gera o texto do QRCODE com base no número total de linhas, somando sempre +1
    qrcode = f'Livro:{contador + 1}'


    cursor.execute(''' INSERT INTO livros (nome, qrcode) VALUES (?, ?)''', (nome, qrcode,)) #Insere os valores no banco
    conn.commit() #Salva as mudanças
    conn.close() #fecha a conexão

    return jsonify({"status": "sucesso"}), 201 #Retorna o status de sucesso para o front OBS: Toda rota flask precisa retornar um https

if __name__ == '__main__':
    criar_banco() #garante que o banco e tabela seja criado ao iniciar o sistema
    app.run(debug=True)