def bit_para_byte(valorASerConvertido):
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byte_para_bit(valorASerConvertido):
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

CONSTANTE_PRINCIPAL = 1024

def byte_para_kilobyte(valorASerConvertido):
    BytesParaKbyte = valorASerConvertido / (CONSTANTE_PRINCIPAL)
    return BytesParaKbyte

def kilobyte_para_byte(valorASerConvertido):
    kbyteParaBytes = valorASerConvertido * (CONSTANTE_PRINCIPAL)
    return kbyteParaBytes


def kilobyte_para_megabyte(valorASerConvertido):
    KbyteParaMbyte = valorASerConvertido / (CONSTANTE_PRINCIPAL)
    return KbyteParaMbyte

def megabyte_para_kilobyte(valorASerConvertido):
    MBparaKB = valorASerConvertido * (CONSTANTE_PRINCIPAL)
    return MBparaKB

def megabyte_para_gigabyte(valorASerConvertido):
    MBparaGB= valorASerConvertido / (CONSTANTE_PRINCIPAL)
    return MBparaGB

def gigabyte_para_megabyte(valorASerConvertido):
    GBparaMB = valorASerConvertido * (CONSTANTE_PRINCIPAL)
    return GBparaMB

def gigabyte_para_Terabyte(valorASerConvertido):
    GBparaTB= valorASerConvertido / (CONSTANTE_PRINCIPAL)
    return GBparaTB

def terabyte_para_gigabyte(valorASerConvertido):
    TBparaGB = valorASerConvertido * (CONSTANTE_PRINCIPAL)
    return TBparaGB


def terabyte_para_petabyte(valorASerConvertido):
    TBparaPB= valorASerConvertido / (CONSTANTE_PRINCIPAL)
    return TBparaPB

def petabyte_para_terabyte(valorASerConvertido):
    PBparaTB = valorASerConvertido * (CONSTANTE_PRINCIPAL)
    return PBparaTB