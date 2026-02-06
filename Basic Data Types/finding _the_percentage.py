def calculate_average(numbers_list):
    # Responsabilidade: Calcular a media
    return sum(numbers_list) / len(numbers_list)

def format_output(number):
    return "{:.2f}".format(number)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    
    # 1 Busca as notas do aluno pedido (O(1))
    notas_do_aluno = student_marks[query_name]
    
    # 2 Calcula a media usando sua funcao
    media = calculate_average(notas_do_aluno)
    
    print(format_output(media))
    
    