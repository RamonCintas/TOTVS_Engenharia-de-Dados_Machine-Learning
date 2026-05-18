# Lê a linha de entrada contendo nomes separados por vírgula e espaço
entrada = input()

# Separa os nomes
nomes = entrada.split(',')

# Remove espaços extras e transforma em maiúsculas
nomes_tratados = [nome.strip().upper() for nome in nomes]

# Junta os nomes no formato solicitado
resultado = '; '.join(nomes_tratados)

# Exibe o resultado
print(resultado)