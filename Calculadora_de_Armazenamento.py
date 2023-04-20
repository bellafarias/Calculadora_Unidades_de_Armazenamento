def bit_para_byte(valorASerConvertido):
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byte_para_bit(valorASerConvertido):
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de bit para byte:"))
valorConvertido = bit_para_byte(entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de byte para bit:"))
valorConvertido = byte_para_bit (entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)

CONSTANTE_PRINCIPAL = 1024

def byte_para_kilobyte(valorASerConvertido):
    BytesParaKbyte = valorASerConvertido / (CONSTANTE_PRINCIPAL)
    return BytesParaKbyte

def kilobyte_para_byte(valorASerConvertido):
    kbyteParaBytes = valorASerConvertido * (CONSTANTE_PRINCIPAL)
    return kbyteParaBytes

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Byte para Kilobyte:"))
valorConvertido = byte_para_kilobyte (entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Kilobyte para Byte:"))
valorConvertido = kilobyte_para_byte(entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)

def kilobyte_para_megabyte(valorASerConvertido):
    KbyteParaMbyte = valorASerConvertido / (CONSTANTE_PRINCIPAL)
    return KbyteParaMbyte

def megabyte_para_kilobyte(valorASerConvertido):
    MBparaKB = valorASerConvertido * (CONSTANTE_PRINCIPAL)
    return MBparaKB

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Kilobyte para Megabyte:"))
valorConvertido = kilobyte_para_megabyte (entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Megabyte para Kilobyte:"))
valorConvertido = megabyte_para_kilobyte (entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)

def megabyte_para_gigabyte(valorASerConvertido):
    MBparaGB= valorASerConvertido / (CONSTANTE_PRINCIPAL)
    return MBparaGB

def gigabyte_para_megabyte(valorASerConvertido):
    GBparaMB = valorASerConvertido * (CONSTANTE_PRINCIPAL)
    return GBparaMB

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Megabyte para Gigabyte:"))
valorConvertido = megabyte_para_gigabyte (entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de Gigabyte para Megabyte:"))
valorConvertido = gigabyte_para_megabyte(entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)

def gigabyte_para_Terabyte(valorASerConvertido):
    GBparaTB= valorASerConvertido / (CONSTANTE_PRINCIPAL)
    return GBparaTB

def terabyte_para_gigabyte(valorASerConvertido):
    TBparaGB = valorASerConvertido * (CONSTANTE_PRINCIPAL)
    return TBparaGB

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de gigabyte para terabyte:"))
valorConvertido = gigabyte_para_Terabyte (entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)

entradaDotecladoValoraSerConvertido = float(input("Insira o valor a ser convertido de terabyte para gigabyte:"))
valorConvertido = terabyte_para_gigabyte(entradaDotecladoValoraSerConvertido)
print("Valor Convertido:", valorConvertido)
