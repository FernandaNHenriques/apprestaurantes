# apprestaurantes

Today
olá copilot, fiz este código em python, me ajuda a escrever o readme para o github? import os restaurantes = [ {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, {'nome': 'Sabor', 'categoria': 'Brasileira', 'ativo': True}, {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False} ] def exibir_nome_do_app(): print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n') def exibir_opcoes(): print('Selecione uma opção:') print('1. Cadastrar Restaurante') print('2. Listar Restaurantes') print('3. Ativar/Desativar Restaurante') print('4. Sair\n') def finalizar_app(): exibir_subtitulo('Finalizando o aplicativo...') print('Obrigado por usar o Sabor Express!\n') def voltar_menu_principal(): input('Pressione Enter para continuar...') main() def opcao_invalida(): print('Opção inválida. Por favor, escolha uma opção válida.\n') voltar_menu_principal() def exibir_subtitulo(texto): os.system('cls') linha = '*' * (len(texto) + 4) print(linha) print(f'* {texto} *') print(linha) print() def cadastro_restaurante(): '''Essa função é responsável por cadastrar um novo restaurante. Ela solicita o nome e a categoria do restaurante''' exibir_subtitulo('Cadastro de Restaurante') nome_do_restaurante = input('Digite o nome do restaurante: ') categoria_do_restaurante = input(f'Digite a categoria do {nome_do_restaurante}: ') dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False} restaurantes.append(dados_do_restaurante) print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n') voltar_menu_principal() def listar_restaurantes(): '''Essa função é responsável por listar todos os restaurantes cadastrados. Ela exibe o nome, categoria e estado (ativo/desativado) de cada restaurante.''' exibir_subtitulo('Lista de Restaurantes Cadastrados') print(f"{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Estado'}\n") print('-' * 60 + '\n') for restaurante in restaurantes: nome_restaurante = restaurante.get('nome') categoria = restaurante.get('categoria') ativo = 'Ativo' if restaurante.get('ativo') else 'Desativado' print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') voltar_menu_principal() def alternar_estado_restaurante(): '''Essa função é responsável por ativar ou desativar um restaurante. Ela solicita o nome do restaurante e altera seu estado.''' exibir_subtitulo('Ativar/Desativar Restaurante') nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ') restaurante_encontrado = False for restaurante in restaurantes: if restaurante.get('nome') == nome_restaurante: restaurante_encontrado = True estado_atual = restaurante.get('ativo', False) restaurante['ativo'] = not estado_atual mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!' print(mensagem) break if not restaurante_encontrado: print(f'Restaurante {nome_restaurante} não encontrado.') voltar_menu_principal() def escolher_opcao(): try: opcao_escolhida = int(input('Digite o número da opção desejada: ')) except ValueError: print('Entrada inválida. Por favor, digite um número.\n') opcao_invalida() return if opcao_escolhida == 1: print('Cadastrar Restaurante') cadastro_restaurante() elif opcao_escolhida == 2: print('Listar Restaurantes') listar_restaurantes() elif opcao_escolhida == 3: alternar_estado_restaurante() elif opcao_escolhida == 4: finalizar_app() else: opcao_invalida() def main(): os.system('cls') exibir_nome_do_app() exibir_opcoes() escolher_opcao() if __name__ == '__main__': main()
Claro, Fernanda! Aqui está uma sugestão de README.md que apresenta seu projeto com clareza e personalidade — do jeitinho que você merece:

🍽️ Sabor Express
Sabor Express é uma aplicação simples em Python voltada para o gerenciamento de restaurantes. Feita com foco em aprendizado e prática de conceitos de lógica, listas, dicionários e funções, ela permite cadastrar, listar e ativar/desativar restaurantes via terminal.

💻 Funcionalidades
✅ Cadastro de restaurante: informe o nome e a categoria

📋 Listagem: veja todos os restaurantes cadastrados com seu estado (ativo ou desativado)

🔄 Ativação/Desativação: altere o estado de qualquer restaurante

🚪 Finalizar: encerra a aplicação com uma mensagem de despedida

🛠️ Como executar
Certifique-se de ter o Python instalado.

bash
python sabor_express.py
A navegação é feita via terminal, digitando o número da opção desejada.

📁 Estrutura do código
main(): ponto de partida da aplicação

cadastro_restaurante(): coleta dados e adiciona um novo restaurante

listar_restaurantes(): exibe todos os restaurantes formatados

alternar_estado_restaurante(): modifica o status (ativo/desativado) de um restaurante

Utiliza uma lista de dicionários para armazenar os restaurantes

✨ Objetivos do projeto
Este projeto é ideal para quem está começando no mundo da programação e quer entender melhor:

Manipulação de listas e dicionários em Python

Lógica de condicionais e loops

Organização de código com funções

Interface simples via terminal

🤝 Contribuições
Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests! Este projeto é feito para aprender e evoluir juntos.



🍽️ Sabor Express
Sabor Express is a simple Python application designed to manage restaurants. Created as a hands-on learning tool, it uses terminal-based input/output to let users add, list, and toggle the status of restaurants. It's perfect for practicing core programming concepts like lists, dictionaries, and functions.

💻 Features
✅ Register restaurant: Add new restaurants with name and category

📋 List restaurants: View all registered restaurants with their current status (active/inactive)

🔄 Activate/Deactivate: Change a restaurant’s availability

🚪 Exit: Closes the application with a farewell message

🛠️ How to Run
Make sure you have Python installed.

bash
python sabor_express.py
Use the terminal to navigate by typing the number of the desired option.

📁 Code Structure
main(): Launches the app and displays the menu

cadastro_restaurante(): Prompts for name and category, then adds to the list

listar_restaurantes(): Displays the full list with formatted output

alternar_estado_restaurante(): Toggles a restaurant’s active state

Uses a list of dictionaries to store restaurant data

✨ Project Goals
This app is ideal for beginners looking to practice:

Working with lists and dictionaries in Python

Applying logic with conditionals and loops

Organizing functions cleanly

Building simple text-based interfaces

🤝 Contributions
Feel free to open issues, suggest improvements, or submit pull requests! This project is about learning and growing together.
