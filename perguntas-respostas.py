# Lista de perguntas e suas respectivas opções e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',  # Pergunta 1
        'Opções': ['1', '3', '4', '5'],  # Opções de resposta
        'Resposta': '4',  # Resposta correta
    },
    {
        'Pergunta': 'Quanto é 5*5?',  # Pergunta 2
        'Opções': ['25', '55', '10', '51'],  # Opções de resposta
        'Resposta': '25',  # Resposta correta
    },
    {
        'Pergunta': 'Quanto é 10/2?',  # Pergunta 3
        'Opções': ['4', '5', '2', '1'],  # Opções de resposta
        'Resposta': '5',  # Resposta correta
    },
]

# Variável para contar a quantidade de acertos
qtd_acertos = 0

# Loop para percorrer as perguntas
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])  # Exibe a pergunta
    print()

    opcoes = pergunta['Opções']  # Armazena as opções de resposta
    for i, opcao in enumerate(opcoes):  # Exibe as opções com índices
        print(f'{i})', opcao)
    print()

    # Solicita ao usuário escolher uma opção
    escolha = input('Escolha uma opção: ')

    acertou = False  # Variável para verificar se o usuário acertou
    escolha_int = None  # Variável para armazenar a escolha convertida em número inteiro
    qtd_opcoes = len(opcoes)  # Obtém a quantidade de opções disponíveis

    # Verifica se a escolha é um número
    if escolha.isdigit():
        escolha_int = int(escolha)  # Converte a escolha para inteiro

    # Verifica se a escolha é válida (entre 0 e a quantidade de opções)
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            # Verifica se a resposta escolhida está correta
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    # Exibe se o usuário acertou ou errou a questão
    if acertou:
        qtd_acertos += 1  # Incrementa o número de acertos
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()

# Exibe o número total de acertos e a quantidade de perguntas
print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
