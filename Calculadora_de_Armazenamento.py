def bit_para_byte(valorASerConvertido):
    print('Valor convertido de bit para bytes')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byte_para_bit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

print('Insira o valor a ser convertido de bit para byte:')
entradaDotecladoValoraSerConvertido = float(input())
valorConvertido = bit_para_byte(entradaDotecladoValoraSerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de byte para bit:')
entradaDotecladoValoraSerConvertido = float(input())
valorConvertido = byte_para_bit (entradaDotecladoValoraSerConvertido)
print(valorConvertido)