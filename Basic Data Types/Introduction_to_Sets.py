def get_unique_values(lista_com_duplicatas):
    return set(lista_com_duplicatas)

def calculate_sum(colecao_de_numeros):
    return sum(colecao_de_numeros)

def count_items(colecao_de_numeros):
    # Responsability: counting the number of items in a collection
    return len(colecao_de_numeros)

def compute_division(total, quantidade):
    # Responsability: pure math (safe division)
    if quantidade == 0:
        return 0
    return total / quantidade


def average(array):
    alturas_unicas = get_unique_values(array)
    
    # Do the calculations
    soma_total = calculate_sum(alturas_unicas)
    
    # Discover how many unique heights there are
    quantidade = count_items(alturas_unicas)
    
    # Calculate the average using the sum and the count
    media_final = compute_division(soma_total, quantidade)
    
    return media_final

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)