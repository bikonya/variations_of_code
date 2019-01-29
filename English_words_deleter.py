import re
file = input('Введи название файла: ')
en_words = re.compile(r"[/^a-zA-Z]")
ru_words = re.compile(r"[/^а-яА-Я]")

def deleter(open_file):
    with open(open_file, 'r') as file:
        for row in file.readlines():
                if not en_words.findall(row) or ru_words.findall(row):
                        with open(open_file + '_new', 'a') as new_file:
                                new_file.write(row)

print('Done')
print(input('Для продолжения нажми любую кнопку'))


if __name__ == '__main__':
    deleter(file)
