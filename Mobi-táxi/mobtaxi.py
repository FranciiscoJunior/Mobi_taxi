import psycopg2

conexao = psycopg2.connect(
    database="mobtaxi",
    user='postgres',
    password='5870SPFC8196',
    host='localhost',
    port='5433'
)

cursor = conexao.cursor()


def menu_mototaxi():
    print('MENU')
    print('1 - Cadastrar Mototaxista ')
    print('2 - Visualizar Informações dos Mototaxistas ')
    print('3 - Atualizar informações do mototaxi ')
    print('4 - Deletar informações do mototaxi ')
    print('5 - Sair ')

    escolha = int(input('Opção: '))

    if escolha == 1:
        return cadastrar_mototaxi()
    elif escolha == 2:
        return visualizar_mototaxi()
    elif escolha == 3:
        return atualizar_mototaxi()
    elif escolha == 4:
        return deletar_mototaxi()
    elif escolha == 5:
        return


def cadastrar_mototaxi():
    dado_nome = str(input("Informe o nome :"))
    dadotelefone = str(input('Informe um numero de telefone: '))
    dadomarca_moto = str(input('informe a marca da sua moto: '))
    dadoplaca = str(input('Informe a placa da sua moto: '))
    dadodia_trabalho = str(input('Informe seu dia de trabalho: '))
    cursor.execute(f''' INSERT INTO mototaxi(nome, telefone, marca_moto, placa, dia_trabalho)
                           VALUES('{dado_nome}','{dadotelefone}', '{dadomarca_moto}', '{dadoplaca}','{dadodia_trabalho}')''')
    print('Dados Inseridos Com Sucesso!')


def visualizar_mototaxi():
    cursor.execute('''SELECT * FROM mototaxi''')
    dado_mototaxi = cursor.fetchall()
    contador = 0
    for mototaxi in dado_mototaxi:
        print(f'Dados do Mototaxista {contador + 1}')
        print('nome: {}'.format(mototaxi[0]))
        print('telefone: {}'.format(mototaxi[1]))
        print('marca_moto: {}'.format(mototaxi[2]))
        print('placa: {}'.format(mototaxi[3]))
        print('dia_trabalho: {}'.format(mototaxi[4]))
        print('')
        contador = contador + 1


def atualizar_mototaxi():
    telefone = str(input('Atualizar telefone: '))
    codigo = str(input('codigo: '))

    cursor.execute(f'''UPDATE mototaxi
    SET telefone = '{telefone}' where codigo = '{codigo}' ''')

    print('Operação realizada com sucesso!')
    print('Os dados atualizados são: ')
    cursor.execute(
        f'''SELECT nome, telefone, marca_moto, placa, dia_trabalho FROM mototaxi where codigo = '{codigo}' ''')
    dado_mototaxi = cursor.fetchall()
    for mototaxi in dado_mototaxi:
        print('Nome: {}'.format(mototaxi[0]))
        print('Telefone: {}'.format(mototaxi[1]))
        print('marca_moto: {}'.format(mototaxi[2]))
        print('placa: {}'.format(mototaxi[3]))
        print('dia_trabalho: {}'.format(mototaxi[4]))
        print('')


def deletar_mototaxi():
    nome = str(input('Informe o codigo do mototaxista que deseja excluir: '))
    if (op == 's'):
        deletar_mototaxi()
        cursor.execute(f'''DELETE FROM mototaxi
        WHERE codigo = '{codigo}' ''')
        print('Mototaxista excluido com sucesso!')
    else:
        print('Não foi possível excluir o mototaxista!')


menu_mototaxi()
conexao.commit()
