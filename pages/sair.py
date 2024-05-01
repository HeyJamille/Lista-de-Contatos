import sys
from pages import conexao 

def sair():
  conexao.cursor.close()
  conexao.banco.close()

  sys.exit()

