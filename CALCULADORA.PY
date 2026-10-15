def calculadora():
    print("=== CALCULADORA SIMPLES ===")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    opcao = input("Escolha a operação (1/2/3/4): ")

    if opcao in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")
            return

        if opcao == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcao == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcao == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcao == '4':
            if num2 == 0:
                print("Erro: Divisão por zero não permitida.")
            else:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    calculadora()