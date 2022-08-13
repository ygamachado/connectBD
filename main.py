import usuario

opcao=10
def salvar():
    nome = input("Digite o nome:")
    email = input("Digite o email:")
    user=usuario.User(1,nome,email)
    save=input("Deseja savar s/n?")
    if save=="s":
        user.save_bd()
def consultar(id):
   ob=usuario.User.from_db(id)
   print(ob.name,ob.email)
def ler():
   obs= usuario.User.lister()
def alterar():
    ler()
    print("digite o indice:")
    id=int(input())
    ob = usuario.User.from_db(id)
    print("Usuario selecioando: ",ob.name, ob.email)
    name=input("digite novo nome:")
    email=input("Digite novo email")
    ob.update(id,name,email)
def deletar():
    ler()
    id=int(input("Digite o indice do usuario a ser deletado: "))
    ob = usuario.User.from_db(id)
    print(ob.name, ob.email)
    print("Tem certeza que deseja deletar o usuário: ",ob.name)
    confirmar=input("s/n?")
    if confirmar =="s":
        ob.deletar(id)
    else:
        menu()
def menu():
    print("======================================\n"
          "Menu\n"
          "======================================\n"
          "1-Cadastrar no Banco de Dados\n"
          "2- Listar Todos os Usuários\n"
          "3-Editar Usuário\n"
          "4-Deletar Usuário\n"
          "0-Sair\n"
          "=======================================")


while (opcao != 0):
    menu()
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 1:
        salvar()
        print("salvar")
    elif opcao == 2:
        ler()
    elif (opcao == 3):
        alterar()
    elif (opcao == 4):
        deletar()
    elif (opcao == 0):
        break
