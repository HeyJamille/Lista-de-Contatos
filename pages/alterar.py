from pages import conexao

# Função alterar
def alterar():
  print("------------- Alterando Contato -------------")
  nome_antigo = input("Qual contato deseja alterar? ")

  db_alterar(nome_antigo)

# Função db_alterar
def db_alterar(nome_antigo):
  conexao.cursor.execute("SELECT * FROM contatos WHERE nome = ?", [nome_antigo])
  resultado = conexao.cursor.fetchall()

  if(resultado):
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    conexao.cursor.execute("UPDATE contatos SET nome = (?), email = (?), telefone = (?) WHERE nome = (?)", (nome, email, telefone, nome_antigo))
    print("\nContato atualizado!")
  else: 
    print("\nContato não existe.")

  conexao.banco.commit()
