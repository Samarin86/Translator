# pip install googletrans==3.1.0a0
from googletrans import Translator


def main():
    print('***** Hello *****')
    file_text = open('file_translate.txt', 'a')

    def write_word():
        original_word = input('Введите слово на Английском: ')
        # translate_word = input('Введите перевод слова: ')
        translator = Translator()
        result = translator.translate(original_word, src='en', dest='ru')
        translate_word = result.text
        print(f'Перевод на Русский: {result.text}\nСлово c переводом будет записано в файл.')
        file_text.write(f'{original_word.capitalize()} - {translate_word.capitalize()}\n')

    again = 'е'
    while again.lower() != 'в' and again.lower() != 'd':
        write_word()
        again = input('Нажмите "Enter" чтобы продолжить или "В" (Выход) для выхода из программы: ')

    print('***** Файл отредактирован (The file has been edited) *****')

    # Передача строк файла в список и сортировка по алфавиту
    file_text = open('file_translate.txt', 'r')
    lines = file_text.readlines()
    lines_sort = sorted(lines)

    # Запись отсортированных строк обратно в файл
    file_text = open('file_translate.txt', 'w')
    for item in lines_sort:
        if not item.isspace():  # Удаление пустых строк в файле
            file_text.write(item)

    file_text.close()


if __name__ == '__main__':
    main()
