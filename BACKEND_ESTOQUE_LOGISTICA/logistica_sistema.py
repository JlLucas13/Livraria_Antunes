from flask import Flask, request, jsonify
import os
import sqlite3


#Inicia o flask
app = Flask(__name__)

#cria o caminho dos códigos a baixo até o banco de dados
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
    #Executa as funções do cursor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   qrcode TEXT UNIQUE,
                   preco FLOAT,
                   capa_url TEXT,
                   descricao TEXT,
                   quantidade_estoque INTERGER DEFAULT 0)''')
    
#OBSERVAÇÃO, AINDA FALTA DESENHAR COMO SERÁ ADICIONADO OS TEMAS DE CADA LIVRO, EXEMPLO: AÇÃO, AVENTURA, ROMANCE E ETC...
# ESTOU PROCURANDO A MELHOR OPÇÃO PARA ADICIONAR OS TEMAS NO BANCO DE DADOS, JÁ QUE UM LIVRO PODE CONTER DEZENAS DELES E NÃO É VIAVEL CRIAR VÁRIAS COLIUNAS DIFERENTES PARA ADICIONAR O TEMA DE CADA LIVRO SENDO QUE ELES VÃO SER DIFERENTES ENTRE SI


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
    cursor.execute(''' INSERT INTO livros (nome) VALUES (?)''', (nome,)) #Insere os valores no banco
    conn.commit() #Salva as mudanças
    conn.close() #fecha a conexão

    return jsonify({"status": "sucesso"}), 201 #Retorna o status de sucesso para o front OBS: Toda rota flask precisa retornar um https

if __name__ == '__main__':
    criar_banco() #garante que o banco e tabela seja criado ao iniciar o sistema
    app.run(debug=True)