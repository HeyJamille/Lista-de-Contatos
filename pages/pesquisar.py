from pages import conexao
from tabulate import tabulate

# Função pesquisar
def pesquisar():
  print("------------- Lista de Contatos -------------")
  nome = input("Qual contato deseja pesquisar? ")

  db_pesquisar(nome)

# Função db_pesquisar
def db_pesquisar(nome):
  conexao.cursor.execute("SELECT * FROM contatos WHERE nome = ?", [nome])
  resultado = conexao.cursor.fetchall()

  if(resultado):
    print(tabulate(resultado, tablefmt="grid"))
  else: 
    print("\nContato não existe.")

  conexao.banco.commit()
  