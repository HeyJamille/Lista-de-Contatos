from pages.adicionar import adicionar
from pages.excluir import excluir
from pages.alterar import alterar
from pages.listar import listar
from pages.pesquisar import pesquisar
from pages.sair import sair

def menu_principal():
  print("------------- Menu ----1---------")
  print("1 - Adicionar")
  print("2 - Excluir")
  print("3 - Alterar")
  print("4 - Listar")
  print("5 - Pesquisar")
  print("6 - Sair")
  opcao = input("Opção: ")

  if (opcao == '1'):
    adicionar()
    menu_principal()
  elif (opcao == '2'):
    excluir()
    menu_principal()
  elif (opcao == '3'):
    alterar()
    menu_principal()
  elif (opcao == '4'):
    listar()
    menu_principal()
  elif(opcao == '5'):
    pesquisar()
    menu_principal()
  elif(opcao == '6'):
    sair()
  else:
    print("Tente novamente.")
