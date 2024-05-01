from pages import conexao

# Função excluir
def excluir():
  print("------------- Excluindo Contato -------------")
  nome = input("Qual contato deseja excluir? ")

  db_excluir(nome)

# Função db_excluir
def db_excluir(nome):
  conexao.cursor.execute("SELECT * FROM contatos WHERE nome = ?", [nome])
  resultado = conexao.cursor.fetchall()

  if(resultado):
    conexao.cursor.execute("DELETE FROM contatos WHERE nome = (?)", [nome]) 
    print("\nContato excluído!")
  else:
    print("\nContato não existe.")

  conexao.banco.commit()
