#Esqueda Rodriguez, Fabian Alejandro

import string

alfabeto = list(string.ascii_lowercase)

def main():
    archivo = open("unstoppable.txt", 'r')#Abrir el archivo en modo de lectura

    cifrar = archivo.read()#Leer el archivo

    archivo_cifrado = cifrado_cesar(alfabeto, 1, cifrar)#Mandar el archivo para cifrarlo

    print('\n')
    print(archivo_cifrado)#Imprimir el texto del archivo cifrado

    archivo.close()


def cifrado_cesar(alfabeto, n, texto):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + n
            if indice_cesar > 25:
                indice_cesar -= 25
            texto_cifrado += alfabeto[indice_cesar]
        else:
            texto_cifrado += letra

    return texto_cifrado


main()