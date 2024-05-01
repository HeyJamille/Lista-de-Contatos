import re

# Validação do telefone
def validacao_telefone():
  telefone_padrao = r'^\([0-9]{2}\) [0-9]{4,5}-[0-9]{4}$'
  telefone = input("Telefone (formato: (XX) XXXX-XXXX): ")
    
  while not re.match(telefone_padrao, telefone):
    print("Formato de telefone inválido.")
    telefone = input("Telefone (formato: (XX) XXXX-XXXX): ")

  return telefone