medidas_armazenamento =["byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
PRINCIPAL= 1024
VALOR_BYTE_BIT = 8

print("Preencha alguns dados com relação a lista de unidades de armazenamento a seguir:")
print("\nLista de unidades de armazenamento:", medidas_armazenamento)

medidas_iniciais = input("Escolha uma unidade de armazenamento você gostaria de converter:")
medidas_final = input("Escolha uma unidade de armazenamento para que o valor seja convertido:")
unidades_para_converter = int(input("Insira um valor à ser convertido:"))
