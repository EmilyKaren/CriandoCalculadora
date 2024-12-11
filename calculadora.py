from time import sleep

print("="*20,"CALCULADORA!", "="*20)
while True:
    n = int(input("Digite o primeiro número: "))
    num = int(input("Digite o segundo número: "))
    while True:
        ope = int(input(f"Escolha o operador \n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n:"))
        if ope == 1:
            equacao = n + num
            print(f"{n} + {num} = {equacao}")
            break
        elif ope == 2:
            equacao = n - num
            print(f"{n} + {num} = {equacao}")
            break
        elif ope == 3:
            equacao = n * num
            print(f"{n} X {num} = {equacao}")
            break
        elif ope == 4:
            equacao = n / num
            print(f"{n} / {num} = {equacao}")
            break
        else:
            print("Número inválido tente novamente!")
    cont = str(input("Deseja continuar? [S/N] ")).upper()
    if cont != "S":
        print("Fechando calculadora.")
        sleep(0.5)
        print("...")
        sleep(0.2)
        print("="*54)
        break
