import re

# Validação do email
def validacao_email():
  email_padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  email = input("E-mail: ")
 
  while not re.match(email_padrao, email):
    print("Formato de e-mail inválido.")
    email = input("E-mail: ")

  return email