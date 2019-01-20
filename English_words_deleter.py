import re
file = input('Введи название файла: ')
p = re.compile(r"[/^a-zA-Z]")

def deleter(open_file):
    with open(open_file, 'r') as file:
        for row in file.readlines():
                if not p.search(row[:len(row) // 2]):
                        with open(open_file + '_new', 'a') as new_file:
                                new_file.write(row)


if __name__ == '__main__':
    deleter(file)
