# Функция чтения файла построчно в список
def ReadFile(filename):
    str = []
    with open(filename) as import_file:
        for line in import_file:
            str.append(line.strip())
    return str

def WordCountInDict(list_in):
    dic = []
    for l in range(len(list_in)):
        for i in range(4):
            dic[l][i] = list_in[l]
    return dic

# Функция сохранения списка построчно
def SaveFile(filename, file_strings):
    with open(filename, "w") as export_file:
        for line in file_strings:
            export_file.write(line + "\n")

if __name__ == "__main__":
    math_values = []
    physics_values = []
    russian_values = []
    with open('input.txt', 'r', encoding='utf-8') as in_file:
        for line in in_file:
            current_line = line.strip().split(';')
            math_values.append(int(current_line[1]))
            physics_values.append(int(current_line[2]))
            russian_values.append(int(current_line[3]))
    out_file = open('output.txt', 'w', encoding='utf-8')
    for i in range(len(math_values)):
        out_file.write(str((math_values[i] + physics_values[i] + russian_values[i]) / 3) + '\n')
    if len(math_values) > 0:
        out_file.write(str(sum(math_values) / len(math_values)) + ' ' +
                       str(sum(physics_values) / len(physics_values)) + ' ' +
                       str(sum(russian_values) / len(russian_values)))
    out_file.close()