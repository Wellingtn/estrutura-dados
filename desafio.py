class Fila:
    """
    Classe Fila que tem atributos:
    tam: tamanho do vetor
    n: número de elementos atuais no vetor
    vet: vetor que forma a Fila
    ini: índice do início da fila (não é utilizado diretamente neste código)
    """
    def __init__(self, tam):
        self.tam = tam
        self.n = 0
        self.vet = [None] * tam
        self.ini = 0

def insere_fila(fila, elem):
    """
    Insere um elemento na fila, desde que haja espaço disponível.
    """
    if fila.n == fila.tam:
        return None  # Fila cheia
    fila.vet[fila.n] = elem
    fila.n += 1
    return fila

def imprime_fila(fila):
    """
    Imprime os elementos da fila na ordem original.
    """
    for atual in fila.vet:
        print(atual, end=" -> ")   
    print("None")
    
def concatena_filas(fila1, fila2):
    """
    Concatena duas filas.
    """
    fila3 = Fila(fila1.tam + fila2.tam)
    for atual in range(fila1.n):
        insere_fila(fila3, fila1.vet[atual])
    for atual in range(fila2.n):
        insere_fila(fila3, fila2.vet[atual])
    return fila3   

#cria filas
F01 = Fila(3)
insere_fila(F01, 1)
insere_fila(F01, 2)
insere_fila(F01, 3)
imprime_fila(F01)

F02 = Fila(3)
insere_fila(F02, 4)
insere_fila(F02, 5)
insere_fila(F02, 6)
imprime_fila(F02)

#concatena filas
F03 = concatena_filas(F01, F02)
imprime_fila(F03)
