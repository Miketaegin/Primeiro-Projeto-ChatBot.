chave_pix = "toystore@pix.com"  
identificacao_boleto = "123456789-BOL"  

produtos = {
    "1": ("LEGO", 150.00),
    "2": ("Quebra-Cabeça", 60.00),
    "3": ("Bonecas Baby Alive", 120.00),
    "4": ("Carrinho de Controle Remoto", 250.00),
    "5": ("Jogo de Tabuleiro", 100.00),
    "6": ("Brinquedos Educativos", 80.00),
    "7": ("Bicicleta Infantil", 350.00)
}
custos_frete = {
    "1": ("REGIONAL 1", 10.00),
    "2": ("REGIONAL 2", 15.00),
    "3": ("REGIONAL 3", 12.00),
    "4": ("REGIONAL 4", 18.00),
    "5": ("REGIONAL 5", 20.00),
    "6": ("REGIONAL 6", 25.00),
    "7": ("REGIONAL 7", 22.00),
    "8": ("REGIONAL 8", 19.00),
    "9": ("REGIONAL 9", 30.00),
    "10": ("REGIONAL 10", 16.00),
    "11": ("REGIONAL 11", 17.00),
    "12": ("REGIONAL 12", 28.00),
    "13": ("REGIÃO METROPOLITANA DE FORTALEZA", 50.00)
}

frete_selecionado = None 
carrinho = ""
preço_total = 0.0
custo_frete = 0.0
preço = 0.0

while True:
    print("\nOlá, me chamo Ed, sou um robô de suporte de vendas da loja Toy Store!")
    print("Como poderia ajudar você?")
    print("1: Ver Brinquedos")
    print("2: Preços de Brinquedos")
    print("3: Taxas de Entrega")
    print("4: Encerrar o suporte")
    opção = input("Qual seria sua opção? ")

    if opção == "1":
        # Exibindo produtos
        for key, (nome, _) in produtos.items():
            print(f"{key}. {nome}")
        escolha = input("\nDigite o número do produto para saber mais: ")
        if escolha in produtos:
            nome, preço = produtos[escolha]
            if escolha == "1":
                print("LEGO - Conjunto de blocos de montar com 500 peças.")
            elif escolha == "2":
                print("Quebra-Cabeça - Quebra-cabeça de 1000 peças com tema de paisagens.")
            elif escolha == "3":
                print("Bonecas Baby Alive - Boneca de plástico e tecido *fashion*.")
            elif escolha == "4":
                print("Carrinho de Controle Remoto - Carrinho para crianças com controle remoto.")
            elif escolha == "5":
                print("Jogo de Tabuleiro - Jogo clássico de estratégia.")
            elif escolha == "6":
                print("Brinquedos Educativos - Caixa com formas geométricas e instrumentos musicais.")
            elif escolha == "7":
                print("Bicicleta Infantil - Bicicleta infantil aro 16 com rodinhas.")
            
            adicionar = input(f"Deseja adicionar {nome} ao carrinho? (s/n): ")
            if adicionar == "s" or adicionar == "S":
                carrinho += nome + ", "
                preço_total += preço
                print(f"{nome} foi adicionado ao carrinho.")
        else:
            print("\nProduto não encontrado. Tente novamente.")

    elif opção == "2":
        print("\nPreços dos Brinquedos:")
        for nome, preço in produtos.values():
            print(f"{nome}: R$ {preço:.2f}") 

    elif opção == "3":
        print("\n--- Opções de Frete ---")
        for região, (nome, custo) in custos_frete.items():
            print(f"{nome}: R$ {custo:.2f}")

        while True:
            região = input("\nDigite o número da região (ou 'sair' para encerrar): ")
            if região == 'sair' or região == 'SAIR':
                print("Encerrando a calculadora de frete.")
                break

            if região in custos_frete:
                nome, frete = custos_frete[região]
                preço_total_final = preço_total + frete
                print(f"O custo do frete para {nome} é R$ {frete:.2f}")
                print(f"O valor total da compra, incluindo o frete, é R$ {preço_total_final:.2f}")
                frete_selecionado = frete
            else:
                print("Região inválida. Tente novamente.")

    elif opção == '4':
        # Opções de pagamento
        print("\n--- Métodos de Pagamento ---")
        print("1: Pix")
        print("2: Cartão de Crédito")
        print("3: Cartão de Débito")
        print("4: Boleto")
        print("5: Dinheiro Físico")
        
        método_pagamento = input("Escolha seu método de pagamento: ")
        if método_pagamento == "1":
            print(f"Para pagamento via Pix, use a chave: {chave_pix}")
        elif método_pagamento == "2":
            print("Para pagamento com Cartão de Crédito, dirija-se ao caixa 1, 2 ou 3.")
        elif método_pagamento == "3":
            print("Para pagamento com Cartão de Débito, dirija-se ao caixa 1, 2 ou 3.")
        elif método_pagamento == "4":
            print(f"Para pagamento via Boleto, utilize o número de identificação: {identificacao_boleto}")
        elif método_pagamento == "5":
            print("Para pagamento em Dinheiro Físico, dirija-se ao caixa para concluir o pagamento.")
        else:
            print("Método de pagamento inválido. Tente novamente.")
        
        print("\n--- SAC ---")
        print("1 - Elogios")
        print("2 - Reclamações e Suporte Técnico")
        print("0 - Sair")

        opção_sac = input("Escolha uma opção: ")

        if opção_sac == '1':
            elogio = input("Digite seu elogio: ")
            print("Obrigado pelo seu elogio!")
        elif opção_sac == '2':
            telefone = input("Digite seu número de telefone para que nossa equipe entre em contato: ")
            print("Obrigado! Nossa equipe especializada entrará em contato no número fornecido para oferecer o suporte necessário.")
        elif opção_sac == '0':
            print("Saindo do SAC. Obrigado!")
        else:
            print("Opção inválida! Tente novamente.")

        print("Finalizando a compra...")

        print("\n--- Histórico da Compra ---")
        if carrinho:
            print("Itens no carrinho:", carrinho[:-2])
            print(f"Total da compra: R$ {preço_total:.2f}")
            print(f"Frete: R$ {frete_selecionado:.2f}" if frete_selecionado else "Frete: R$ 0.00")
            print(f"Total final: R$ {preço_total + (frete_selecionado if frete_selecionado else 0):.2f}")
        else:
            print("Nenhum item no carrinho.")
        
        avaliação = 0
        while avaliação < 1 or avaliação > 5:
            avaliação = int(input("Por favor, avalie nosso atendimento de 1 a 5: "))
            if avaliação < 1 or avaliação > 5:
                print("Avaliação inválida. Digite um número entre 1 e 5.")

        comentário = input("Deixe um comentário sobre sua experiência (opcional): ")
        
        print("Obrigado pela sua avaliação!")
        print("Sua avaliação:", avaliação)
        if comentário:
            print("Seu comentário:", comentário)

        print("Obrigado pela sua compra! Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")