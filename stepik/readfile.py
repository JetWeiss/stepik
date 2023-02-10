def change_words():
    c = ''
    number = '0123456789'
    num = ''
    with open('input.txt') as inf:
        for line in inf:
            line = line.strip()
    for i in range(len(line)):
        if line[i] not in number and num != '':
            c += (str(str(line[i - len(num) - 1]) * (int(num) - 1)))
            c += str(line[i])
            num = ''
        elif line[i] not in number:
            c += str(line[i])
        else:
            num += str(line[i])
    with open('output.txt', 'w') as ouf:
        ouf.write(c)

# Функция чтения файла построчно в список
def ReadFile(filename):
    str = []
    with open(filename) as import_file:
        for line in import_file:
            str.append(line.strip().upper())
    return str

# Функция сохранения списка построчно
def SaveFile(filename, file_strings):
    with open(filename, "w") as export_file:
        for line in file_strings:
            export_file.write(line + "\n")

# Функция декомперссии (a1b8)
def UncompressString(s):
    nom = 0
    new_str = ""
    while nom < len(s):
        ch1 = str(s[nom])
        ch2 = ""
        while nom + 1 < len(s) and s[nom + 1].isdigit():
            ch2 += str(s[nom + 1])
            nom += 1
        new_str += str(ch1 * int(ch2))
        nom += 1
    return new_str

# Функция словарь пословно с количеством ('aaa': 8)
def WordCountInDict(list_in):
    dic = {}
    for line in list_in:
        list_words = line.split()
        for word in list_words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] = dic[word] + 1
    return dic


# Функция поиск максимума по значению в словаре
def MaxInDict(dict_in):
    max_key = ""
    max_value = 0
    for key, val in dict_in.items():
        if max_value < val:
            max_value = val
            max_key = key
    return max_key


if __name__ == "__main__":
    filename_in = 'input.txt'
    filename_out = 'output.txt'
    # Словарик
    dic = {}
    file_strings = ""

    # Получить список
    file_strings = ReadFile(filename_in)

    # Список в словарь
    dic = WordCountInDict(file_strings)

    # Максимальное значение в словаре
    max_dic = MaxInDict(dic)

    # Максимум в список
    file_strings.clear()
    file_strings.append(max_dic + " " + str(dic[max_dic]))
    # Список в файл
    SaveFile(filename_out, file_strings)