from pages import conexao
from tabulate import tabulate

# Função listar
def listar():
  print("------------- Lista de Contatos -------------")
  db_listar()

# Função db_listar
def db_listar():
  conexao.cursor.execute("SELECT * FROM contatos")
  resultado = conexao.cursor.fetchall()

  print(tabulate(resultado, tablefmt="grid"))