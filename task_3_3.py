name_list = ["Иван", "Мария", "Александр", "Марина", "Петр", "Ирина", "Валерия", "Виктория", "Анна"]
leters = []
for names in name_list:
    leters.append(names[0])
print(leters)

dict_list = {}
for i, l in zip(name_list, leters):
    dict_list[i] = l
print(dict_list)

# inverse_list = dict_list([n, l] for n, l in dict_list.items())