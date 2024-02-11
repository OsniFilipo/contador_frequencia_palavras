def contar_frequencia_palavras(frase):
    # Convertendo a frase para minúsculas e dividindo em palavras
    palavras = frase.lower().split()
    
    # Inicializando um dicionário para armazenar a frequência de cada palavra
    frequencia = {}
    
    # Contando a frequência de cada palavra na lista de palavras
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
            
    return frequencia

def main():
    frase = input("Digite uma frase para contar a frequência das palavras: ")
    resultado = contar_frequencia_palavras(frase)
    print("\nFrequência das palavras na frase:")
    for palavra, freq in resultado.items():
        print(f"{palavra}: {freq}")

if __name__ == "__main__":
    main()
