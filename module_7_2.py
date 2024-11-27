def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, "w", encoding = "utf-8")
    for i, string in enumerate(strings, 1):
        string_position = file.tell()
        file.write(f'{string}\n')
        strings_positions[(i, string_position)] = string
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)