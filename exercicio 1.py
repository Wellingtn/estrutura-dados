#===========================================================================================================
#1. Crie uma função imprime_reversa(lista) que imprime os elementos de uma lista encadeada em ordem reversa.

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

def imprime_reversa(fila):
    """
    Cria uma nova fila invertida e imprime os elementos em ordem reversa.
    """
    reversa = Fila(fila.n)  # Cria nova fila com o mesmo número de elementos
    for atual in range(fila.n - 1, -1, -1):  # Percorre de trás pra frente
        insere_fila(reversa, fila.vet[atual])
    
    # Imprime a fila invertida
    for atual in reversa.vet:
        print(atual, end=" -> ")   
    print("None")

# ==== Teste da função ====
F01 = Fila(3)                         # Criação da fila F01 com capacidade 3
insere_fila(F01, 1)                   # Inserção de elementos
insere_fila(F01, 2)
insere_fila(F01, 3)
imprime_fila(F01)                    # Impressão original: 1 -> 2 -> 3 -> None
reversa = imprime_reversa(F01)      # Impressão reversa: 3 -> 2 -> 1 -> None


#===========================================================================================================
#2. Escreva uma função remove_ultimo(lista) que remove o último nó de uma lista encadeada e retorna a lista atualizada.

class Node:
    def __init__(self, info):
        self.info = info
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

def cria_lista():
    return ListaEncadeada()

def insere_lista(lista, valor):
    """
    Insere novo nó no fim da lista encadeada.
    """
    novo = Node(valor)
    if lista.primeiro is None:
        lista.primeiro = novo
        lista.ultimo = novo
    else:
        lista.ultimo.prox = novo
        lista.ultimo = novo
    return lista

def remove_ultimo(lista): 
    """
    Remove o último nó da lista.
    """
    if lista.primeiro is None:
        return None  # Lista vazia
    elif lista.primeiro == lista.ultimo:
        lista.primeiro = None
        lista.ultimo = None  # Apenas um elemento
    else:
        aux = lista.primeiro
        while aux.prox != lista.ultimo:
            aux = aux.prox
        aux.prox = None
        lista.ultimo = aux

def imprime_lista(lista):
    """
    Imprime a lista encadeada.
    """
    atual = lista.primeiro
    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")

# ==== Teste ====
lista = cria_lista()                     # Criação da lista
insere_lista(lista, 1)
insere_lista(lista, 2)
insere_lista(lista, 3)
insere_lista(lista, 4)
insere_lista(lista, 5)
imprime_lista(lista)                     # Lista original

remove_ultimo(lista)                     # Remove 5
imprime_lista(lista)
remove_ultimo(lista)                     # Remove 4
imprime_lista(lista)
remove_ultimo(lista)                     # Remove 3
imprime_lista(lista)
remove_ultimo(lista)                     # Remove 2
imprime_lista(lista)


#===========================================================================================================
# 3. Crie uma função soma_valores(lista) que soma os valores de uma lista encadeada.

class Node:
    def __init__(self, info):
        self.info = info
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

def cria_lista():
    return ListaEncadeada()

def insere_lista(lista, valor):
    """
    Insere valor no fim da lista.
    """
    novo = Node(valor)
    if lista.primeiro is None:
        lista.primeiro = novo
        lista.ultimo = novo
    else:
        lista.ultimo.prox = novo
        lista.ultimo = novo
    return lista

def soma_valores(lista):
    """
    Soma iterativamente os valores dos nós da lista.
    """
    soma = 0
    atual = lista.primeiro
    while atual is not None:
        soma += atual.info
        atual = atual.prox
    return soma

# ==== Teste ====
lista = cria_lista()
insere_lista(lista, 2)
insere_lista(lista, 3)
insere_lista(lista, 5)
print(soma_valores(lista))  # Esperado: 10


#===========================================================================================================
# 4. Crie uma função soma_valores_recursivo(lista) que soma recursivamente os valores de uma lista encadeada.

class Node:
    def __init__(self, info):
        self.info = info
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

def cria_lista():
    return ListaEncadeada()

def insere_lista(lista, valor):
    """
    Insere valor na lista.
    """
    novo = Node(valor)
    if lista.primeiro is None:
        lista.primeiro = novo
        lista.ultimo = novo
    else:
        lista.ultimo.prox = novo
        lista.ultimo = novo
    return lista

def soma_valores_recursivo(lista):
    """
    Função principal que chama a recursiva interna.
    """
    def soma_no(Node):
        if Node is None:
            return 0
        return Node.info + soma_no(Node.prox)
    
    return soma_no(lista.primeiro)

# ==== Teste ====
lista = cria_lista()
lista = insere_lista(lista, 2)
lista = insere_lista(lista, 3)
lista = insere_lista(lista, 5)
print(soma_valores_recursivo(lista))  # Esperado: 10


#===========================================================================================================
#5. Implemente uma função remove_duplicatas(lista) que remove todas as duplicatas de uma lista encadeada, mantendo apenas a primeira ocorrência.
class Node:
    def __init__(self, info):
        self.info = info
        self.prox = None    

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

def cria_lista():
    return ListaEncadeada()

def insere_lista(lista, valor):
    """
    Insere valor na lista.
    """
    novo = Node(valor)
    if lista.primeiro is None:
        lista.primeiro = novo
        lista.ultimo = novo
    else:
        lista.ultimo.prox = novo
        lista.ultimo = novo
    return lista

def imprime_lista(lista):
    """
    Imprime os elementos da lista encadeada.
    """
    atual = lista.primeiro
    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")
    
def remove_duplicatas(lista):
    """
    Percorre a lista e remove elementos com valores duplicados, mantendo apenas a primeira ocorrência.
    """
    atual = lista.primeiro
    while atual is not None:
        anterior = atual
        prox = atual.prox
        while prox is not None:
            if prox.info == atual.info:
                anterior.prox = prox.prox  # Remove duplicata
                if prox == lista.ultimo:   # Atualiza o último se necessário
                    lista.ultimo = anterior
                prox = anterior.prox       # Continua do nó seguinte
            else:
                anterior = prox
                prox = prox.prox
        atual = atual.prox

# ==== Teste ====
lista = cria_lista()
lista = insere_lista(lista, 2)
lista = insere_lista(lista, 3)
lista = insere_lista(lista, 5)
lista = insere_lista(lista, 2)
lista = insere_lista(lista, 3)
lista = insere_lista(lista, 5)
lista = insere_lista(lista, 10)
imprime_lista(lista)             # Antes: 2 -> 3 -> 5 -> 2 -> 3 -> 5 -> 10 -> None
remove_duplicatas(lista)
imprime_lista(lista)             # Depois: 2 -> 3 -> 5 -> 10 -> None


#===========================================================================================================
#6. Retorne os elementos diferentes entre duas listas
class Node:
    def __init__(self, info):
        self.info = info
        self.prox = None    

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

def cria_lista():
    return ListaEncadeada()

def insere_lista(lista, valor):
    novo = Node(valor)
    if lista.primeiro is None:
        lista.primeiro = novo
        lista.ultimo = novo
    else:
        lista.ultimo.prox = novo
        lista.ultimo = novo
    return lista

def imprime_lista(lista):
    atual = lista.primeiro
    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")
    
def elementos_diferentes(list1, list2):
    atual1 = list1.primeiro
    atual2 = list2.primeiro
    while atual1 is not None and atual2 is not None:
        if atual1.info == atual2.info:
            atual1 = atual1.prox
            atual2 = atual2.prox
        elif atual1.info < atual2.info:
            print(atual1.info, end=" -> ")
            atual1 = atual1.prox
        else:
            print(atual2.info, end=" -> ")
            atual2 = atual2.prox
    while atual1 is not None:
        print(atual1.info, end=" -> ")
        atual1 = atual1.prox
    while atual2 is not None:
        print(atual2.info, end=" -> ")
        atual2 = atual2.prox
    print("None")

lista1 = cria_lista()    
lista1 = insere_lista(lista1, 2)
lista1 = insere_lista(lista1, 3)
lista1 = insere_lista(lista1, 5)

lista2 = cria_lista()    
lista2 = insere_lista(lista2, 2)
lista2 = insere_lista(lista2, 3)
lista2 = insere_lista(lista2, 5)
lista2 = insere_lista(lista2, 10)

print("Lista 1:")
imprime_lista(lista1)

print("Lista 2:")
imprime_lista(lista2)

print("Elementos diferentes:")
elementos_diferentes(lista1, lista2)

#===========================================================================================================
# DESAFIO (Valor 5% da G1): Uma lista encadeada cíclica, o ultimo nó aponta para o primeiro nó, ficando um looping infinito,
# como identificar se uma lista é cíclica ou não. Use o algoritmo da "tartaruga e lebre" (Floyd’s Cycle-Finding Algorithm).
# tem_ciclo(lista) (esperado: TRUE/FALSE)
class Node:
    def __init__(self, info):
        self.info = info
        self.prox = None

class ListaEncadeadaCiclica:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

def cria_lista():
    return ListaEncadeadaCiclica()

def insere_lista(lista, valor):
    novo = Node(valor)
    if lista.primeiro is None:
        lista.primeiro = novo
        lista.ultimo = novo
        novo.prox = novo  # cria ciclo com ele mesmo
    else:
        novo.prox = lista.primeiro
        lista.ultimo.prox = novo
        lista.ultimo = novo
    return lista

def tem_ciclo(lista):
    tartaruga = lista.primeiro
    lebre = lista.primeiro
    while tartaruga is not None and lebre is not None and lebre.prox is not None:
        tartaruga = tartaruga.prox
        lebre = lebre.prox.prox
        if tartaruga == lebre:
            return True
    return False

# Teste com lista cíclica
lista = cria_lista()    
insere_lista(lista, 2)
insere_lista(lista, 3)
insere_lista(lista, 5)

print(tem_ciclo(lista))  # Esperado: True
