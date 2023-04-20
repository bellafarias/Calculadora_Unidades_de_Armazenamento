from Calculadora_de_Armazenamento import bit_para_byte, byte_para_bit, byte_para_kilobyte, kilobyte_para_byte, kilobyte_para_megabyte, megabyte_para_kilobyte, megabyte_para_gigabyte, gigabyte_para_megabyte, gigabyte_para_Terabyte, terabyte_para_gigabyte, terabyte_para_petabyte, petabyte_para_terabyte

print("-Escreva 1 para converter Bit(b) para Byte(B) \n-Escreva 2 para converter Byte(B) para Bit(b) \n-Escreva 3 para converter Byte(B) para KiloByte(KB) \n-Escreva 4 para converter Kilobyte(KB) para Byte(B) \n-Escreva 5 para converter Kilobyte(KB) para MegaByte(MB) \n-Escreva 6 para converter Megabyte(MB) para Kilobyte(KB) \n-Escreva 7 para converter Megabyte(MB) para GigaByte(GB) \n-Escreva 8 para converter Gigabyte(GB) para Megabyte(MB) \n-Escreva 9 para converter Gigabyte(GB) para Terabyte(TB) \n-Escreva 10 para converter Terabyte(TB) para Gigabyte(GB) \n-Escreva 11 para converter Terabyte(TB) para Petabyte(PB) \n-Escreva 12 Para converter Petabyte(PB) para Terabyte(TB)")
funcEscolha = input()
if(funcEscolha == '1'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de bit para byte:"))
    valorConvertido = bit_para_byte(entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '2'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de byte para bit:"))
    valorConvertido = byte_para_bit (entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '3'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Byte para Kilobyte:"))
    valorConvertido = byte_para_kilobyte (entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '4'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Kilobyte para Byte:"))
    valorConvertido = kilobyte_para_byte(entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido) 

elif(funcEscolha == '5'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Kilobyte para Megabyte:"))
    valorConvertido = kilobyte_para_megabyte (entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '6'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Megabyte para Kilobyte:"))
    valorConvertido = megabyte_para_kilobyte (entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '7'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Megabyte para Gigabyte:"))
    valorConvertido = megabyte_para_gigabyte (entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '8'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Gigabyte para Megabyte:"))
    valorConvertido = gigabyte_para_megabyte(entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '9'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Gigabyte para Terabyte:"))
    valorConvertido = gigabyte_para_Terabyte (entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '10'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Terabyte para Gigabyte:"))
    valorConvertido = terabyte_para_gigabyte(entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '11'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Terabyte para Petabyte:"))
    valorConvertido = terabyte_para_petabyte (entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)

elif(funcEscolha == '12'):
    entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Petabyte para Terabyte:"))
    valorConvertido = petabyte_para_terabyte(entradaDotecladoValoraSerConvertido)
    print("Valor Convertido:", valorConvertido)
