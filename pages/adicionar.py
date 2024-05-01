from pages import conexao
from components.validacao_telefone import validacao_telefone
from components.validacao_email import validacao_email

# Função adicionar
def adicionar():
  print("------------- Adicionando novo Contato -------------")
  nome = input("Nome: ")

  email = validacao_email()
  telefone = validacao_telefone()

  db_adicionar(nome, email, telefone)

# Função db_adicionar
def db_adicionar(nome, email, telefone):
  conexao.cursor.execute("INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone)) 
  conexao.banco.commit()

