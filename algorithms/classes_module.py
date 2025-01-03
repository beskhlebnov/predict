from collections import Counter
def classes(class_list, point_list):
    classes = [class_list[i]['centr'] for i in range(len(class_list))]
    len_classes = len(classes)
    points = [point_list[i]['centr'] for i in range(len(point_list))]
    len_points = len(points)
    docenter = []
    scalar = []
    korel = []
    ugl = []

    result = {}

    countfactors = min(len(points[0]), len(classes[0]))

    for i in range(len_points):
        result[point_list[i]['name']] = []
        res = []
        for j in range(len_classes):
            sume = 0
            for cor in range(countfactors):
                sume += (points[i][cor] - classes[j][cor]) ** 2
            res.append(sume)
        docenter.append(res)

    for i in range(len_points):
        for j in range(len_classes):
            if (docenter[i][j] == min(docenter[i])):
                result[point_list[i]['name']].append(class_list[j]['name'])

    for i in range(len_points):
        res = []
        for j in range(len_classes):
            sume = 0
            for cor in range(countfactors):
                sume += (points[i][cor] * classes[j][cor])
            res.append(sume)
        scalar.append(res)

    for i in range(len_points):
        for j in range(len_classes):
            if (scalar[i][j] == max(scalar[i])):
                result[point_list[i]['name']].append(class_list[j]['name'])

    for i in range(len_points):
        res = []
        for j in range(len_classes):
            sump = 0
            sumc = 0
            for cor in range(countfactors):
                sump += points[i][cor]
                sumc += classes[j][cor]
            res.append(scalar[i][j] - ((sump * sumc) / len(points[i])))
        korel.append(res)

    for i in range(len_points):
        for j in range(len_classes):
            if (korel[i][j] == max(korel[i])):
                if korel[i].count(korel[i][j] == 1):
                    result[point_list[i]['name']].append(class_list[j]['name'])
                else:
                    answer = ''
                    print(korel[i])
                    for k in range(len_classes):
                        if korel[i][k] == korel[i][j]:
                            answer += f"{class_list[k]['name']} "
                    print(answer)
                    result[point_list[i]['name']].append(answer)
                    break

    for i in range(len_points):
        res = []
        for j in range(len_classes):
            sump = 0
            sumc = 0
            for cor in range(countfactors):
                sump += points[i][cor] ** 2
                sumc += classes[j][cor] ** 2
            res.append(round(scalar[i][j] / (sump ** 0.5 * sumc ** 0.5), 2))
        ugl.append(res)
    for i in range(len_points):
        for j in range(len_classes):
            if ugl[i][j] == max(ugl[i]):
                if ugl[i].count(ugl[i][j] == 1):
                    result[point_list[i]['name']].append(class_list[j]['name'])
                else:
                    answer = ''
                    for k in range(len_classes):
                        if ugl[i][k] == ugl[i][j]:
                            answer += f"{class_list[k]['name']} "
                    result[point_list[i]['name']].append(answer)
                    break


    def most_frequent(List):
        occurence_count = Counter(List)
        max_count = max(occurence_count.values())
        most_common_elements = [element for element, count in occurence_count.items() if count == max_count]
        return most_common_elements

    def all_elements_are_same(lst):
        return len(set(lst)) <= 1

    def get_max_class(substring):
        full = ""
        for m in substring:
            full += m
        result_count = []
        for i in range(len(class_list)):
            result_count.append(full.count(class_list[i]['name']))
        for i in range(len(class_list)):
            if result_count[i] == max(result_count):
                return class_list[i]['name']

    for key in result:
        if all_elements_are_same(result[key]):
            result[key].append(f"Исходя из результата всех методов, точка {key} принадлежит классу {result[key][0]} без отклонений")
        else:
            most = most_frequent(result[key])
            result[key].append(
                f"Результаты методов разнятся, исходя из текущих исследований можно сказать что точка {key} сколняется к классу {get_max_class(most)}, для более точного результата необходимо больше исследований")
    return result


