medidas_armazenamento =["byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
valor_padrao = 1024

def dadinhos():
    print("Preencha alguns dados com relação a lista a seguir:", medidas_armazenamento)
    medidas_nominhos = input("Escolha uma unidade de armazenamento você gostaria de converter:")
    while medidas_nominhos not in medidas_armazenamento:
        medidas_nominhos = input ("Unidade não encontrada, tente novamente:")
    medidas_nomes = input("Escolha uma unidade de armazenamento para que o valor seja convertido:")
    while medidas_nomes not in medidas_armazenamento:
        medidas_nomes = input ("Unidade não encontrada, tente novamente:")
    unidades_para_converter = int(input("Insira um valor à ser convertido:"))
    return medidas_nomes, medidas_nominhos, unidades_para_converter

