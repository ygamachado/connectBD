import create
import usuario


def save():
    print('Nome:')
    nome = input()
    print("email")
    email = input()
    user = usuario.User(1,nome,email)
    return user
    ob=create.Create()