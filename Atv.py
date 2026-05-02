while True:
    lista_projetos = []

    comando = input("Olá, digite um comando (ABOUT/QUIT/ADD): ").upper() #<- ".upper" permite o funcionamento do código mesmo digitando letras minúsculas
    despedida = "Até logo!"

    if comando == "ABOUT":
        print("Gestor de portfólio do/a Alex.")

    elif comando == "QUIT":
        print("Saindo do Gestor de Portfólio....")
        print(despedida)
        break

    elif comando == "ADD":
        projetos = int(input("Quantos projetos gostaria de cadastrar? "))

        while projetos <= 0:
            projetos = int(input("ERRO: insira um número válido de projetos: "))

        for i in range(projetos):
            nome = input(f"Digite o nome do projeto {i + 1}: ")
            print(f"Sucesso: Projeto {nome} adicionado")
            lista_projetos.append(nome)

    else:
        print("ERRO: comando inválido")

print("\nProjetos cadastrados: "+",".join (lista_projetos))


print(despedida)