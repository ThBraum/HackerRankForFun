def handle_insert(lista_atual, posicao, valor):
    lista_atual.insert(posicao, valor)

def handle_remove(lista_atual, valor):
    if valor in lista_atual:
        lista_atual.remove(valor)

def handle_append(lista_atual, valor):
    lista_atual.append(valor)

def handle_sort(lista_atual):
    lista_atual.sort()

def handle_pop(lista_atual):
    if lista_atual:
        lista_atual.pop()

def handle_reverse(lista_atual):
    lista_atual.reverse()

def handle_print(lista_atual):
    print(lista_atual)


if __name__ == '__main__':
    N = int(input())
    
    minha_lista = []
    
    for _ in range(N):
        entrada = input().split()
        comando = entrada[0]
        
        if comando == 'insert':
            handle_insert(minha_lista, int(entrada[1]), int(entrada[2]))
            
        elif comando == 'print':
            handle_print(minha_lista)
            
        elif comando == 'remove':
            handle_remove(minha_lista, int(entrada[1]))
            
        elif comando == 'append':
            handle_append(minha_lista, int(entrada[1]))
            
        elif comando == 'sort':
            handle_sort(minha_lista)
            
        elif comando == 'pop':
            handle_pop(minha_lista)
            
        elif comando == 'reverse':
            handle_reverse(minha_lista)