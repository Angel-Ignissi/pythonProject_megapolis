# Поиск осуществляется в файле 1.txt
# Файл 1.txt присутствует в репозитории данного проекта
with open('1.txt') as f:
    s = f.readline()
    li = [s.strip().split('\t') for s in f]
    answer = '1'
    # Осуществление поиска и вывода требуемой вакансии
    while answer != 'None':
        answer = input('Введите название компании: ')
        new_li = [x for x in li if x[4] == answer]
        for x in new_li:
            print(f'В {x[4]} найдена вакансия: {x[3]}. \
З/п составит: {x[0]}')
        # Программа завершит работу при вводе пользователем "None"
        if answer == 'None':
            break
