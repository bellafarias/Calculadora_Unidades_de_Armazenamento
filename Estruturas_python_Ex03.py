medidas_armazenamento =["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
PRINCIPAL= 1024
VALOR_BYTE_BIT = 8

print("Preencha alguns dados com relação a lista de unidades de armazenamento a seguir:")
print("\nLista de unidades de armazenamento:", medidas_armazenamento)

medidas_iniciais = input("Escolha uma unidade de armazenamento você gostaria de converter em relação a lista anterior:")
while medidas_iniciais not in medidas_armazenamento:
    medidas_iniciais = input ("Unidade não encontrada, tente novamente:")
else:
    origem_marota = medidas_armazenamento.index(medidas_iniciais)

medidas_final = input("Escolha uma unidade de armazenamento para que o valor seja convertidoem relação a lista anterior:")
while medidas_final not in medidas_armazenamento:
    medidas_final = input ("Unidade não encontrada, tente novamente:")
else:
    destino_maroto = medidas_armazenamento.index(medidas_final)

unidades_para_converter = int(input("Insira um valor à ser convertido:"))

def dadinhos_convert():
    if origem_marota < destino_maroto:
        tamanho = destino_maroto - origem_marota
        resultado = unidades_para_converter / (PRINCIPAL**tamanho)
    else:
        tamanho = destino_maroto - origem_marota
        resultado = unidades_para_converter * (PRINCIPAL**tamanho)
    print ("Seu resultado é:", resultado, str(medidas_final))

dadinhos_convert()