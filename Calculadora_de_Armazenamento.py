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


