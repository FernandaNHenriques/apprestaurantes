import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Sabor', 'categoria': 'Brasileira', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]


def exibir_nome_do_app():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    print('Selecione uma opção:')
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar/Desativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo...')
    print('Obrigado por usar o Sabor Express!\n')

def voltar_menu_principal():
    input('Pressione Enter para continuar...')
    main()

def opcao_invalida():
    print('Opção inválida. Por favor, escolha uma opção válida.\n')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'* {texto} *')
    print(linha)
    print()


def cadastro_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante. Ela solicita o nome e a categoria do restaurante'''
    
    exibir_subtitulo('Cadastro de Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar todos os restaurantes cadastrados. Ela exibe o nome, categoria e estado (ativo/desativado) de cada restaurante.'''
    
    exibir_subtitulo('Lista de Restaurantes Cadastrados')
    print(f"{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Estado'}\n")
    print('-' * 60 + '\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante.get('nome')
        categoria = restaurante.get('categoria')
        ativo = 'Ativo' if restaurante.get('ativo') else 'Desativado'
        
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por ativar ou desativar um restaurante. Ela solicita o nome do restaurante e altera seu estado.'''
    
    exibir_subtitulo('Ativar/Desativar Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante.get('nome') == nome_restaurante:
            restaurante_encontrado = True
            estado_atual = restaurante.get('ativo', False)
            restaurante['ativo'] = not estado_atual
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
            break

    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado.')
    
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite o número da opção desejada: '))
    except ValueError:
        print('Entrada inválida. Por favor, digite um número.\n')
        opcao_invalida()
        return

    if opcao_escolhida == 1:
        print('Cadastrar Restaurante') 
        cadastro_restaurante()
    elif opcao_escolhida == 2:
        print('Listar Restaurantes')
        listar_restaurantes()
    elif opcao_escolhida == 3:
        alternar_estado_restaurante()
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()