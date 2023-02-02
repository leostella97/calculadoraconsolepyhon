opcao = input("1 PARA SOMA | 2 PARA SUBTRAÇÃO | 3 PARA MULTIPLICAÇÃO \n 4 PARA DIVISÃO | 5 PARA MODULAR | 6 PARA EXPONENCIAÇÃO \n Escreva a opção desejada: ")

if opcao == "1":
    print("### Soma ###")
    x = input("Digite o primeiro número: ")
    y = input("Digite o segundo número: ")
    resultado = float(x)+float(y)
    print("O resultado é: ", resultado)

elif opcao == "2":
    print("### Subtração ###")
    x = input("Digite o primeiro número: ")
    y = input("Digite o segundo número: ")
    resultado = float(x)-float(y)
    print("O resultado é: ", resultado)

elif opcao == "3":
    print("### Multiplicação ###")
    x = input("Digite o primeiro número: ")
    y = input("Digite o segundo número: ")
    resultado = float(x)*float(y)
    print("O resultado é: ", resultado)

elif opcao == "4":
    print("### Divisão ###")
    x = input("Digite o primeiro número: ")
    y = input("Digite o segundo número: ")
    resultado = float(x)/float(y)
    print("O resultado é: ", resultado)

elif opcao == "5":
    print("### Modular ###")
    x = input("Digite o primeiro número: ")
    y = input("Digite o segundo número: ")
    resultado = float(x)%float(y)
    print("O resultado é: ", resultado)

elif opcao == "6":
    print("### Exponenciação ###")
    x = input("Digite o primeiro número: ")
    y = input("Digite o segundo número: ")
    resultado = float(x)**float(y)
    print("O resultado é: ", resultado)

else:
    print("Por favor, escolha uma opção válida")