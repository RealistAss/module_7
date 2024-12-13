info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]
def custom_write(file_name, strings):
    string_position = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i,string in enumerate(strings, 1):
        a =  file.tell()

        file.write(string + '\n')

        string_position[i, a] = string

    file.close()
    return string_position


print(custom_write('text.txt', info))