# Leitura da linha de entrada
entrada = input().strip()

# Separa os campos
produto, quantidade, valor_unitario = entrada.split(',')

# Converte para inteiro e calcula o total
total = int(quantidade) * int(valor_unitario)

# Exibe o resultado formatado
print(f"{produto}: {total}")