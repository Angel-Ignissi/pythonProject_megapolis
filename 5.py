with open('1.txt') as f:
    s = f.readline()
    li = [s.strip().split('\t') for s in f]
    # Создание и заполнение хэш-таблицы
    hash = {x[4]: [] for x in li}
    for elem in li:
        hash[elem[4]].append(elem[3])
    # В этот список будет записано название компании
    # и кол-во вакансий в ней
    maxi = ['name_of_company', 0]

    # Осуществление поиска компании с наибольшим числом вакансий в ней
    for x in hash.items():
        if len(x[1]) > maxi[1]:
            maxi = [x[0], len(x[1])]
    # Вывод компании с самым большим кол-вом вакансий и
    # кол-вом вакансий в ней
    print(f'Компания с самым большим кол-вом вакансий: {maxi[0]}. \
Кол-во вакансий в ней: {maxi[1]}')
