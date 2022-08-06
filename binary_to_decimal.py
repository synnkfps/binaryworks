# Interpretar Binários em Python
# Como um binário funciona:
# x*64 + x*32 + x*16 + x*8 + x*4 + x*2 + x*1 = Y

# Programa:
# Perguntar ao usuário qual binário ele deseja decodificar
# Decodificar pegar a resposta dele
# A cada digito, colocar em uma array
# Depois fazer os calculos como dito a cima.

def main():
    binary = []
    decimal = ""
    operations = [64, 32, 16, 8, 4, 2, 1]
    valido = True
    inp = input("Digite um binário para ser decodificado (7 números, 1 e 0 apenas): ")

    if len(inp) != 7:
        print("Binário invalido. O tamanho de um binário deve ser de 7 números.")
        main()

    for i in inp:
        binary.append(i)

    for i in binary:
        if i == "1" or i=="0":
            valido = True 
        else:
            valido = False 
            if valido == False:
                print("Binário invalido. Use apenas 1 e 0 (zeros).")
                main()

    for i, j in zip(binary, operations):
        decimal += f'({str(i)}*{j})+'
    else:
        decimal = list(decimal)
        decimal[-1] = ''
        decimal = ''.join(decimal)

    exec(f"print({decimal})")

main()
