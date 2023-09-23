# pip install googletrans==3.1.0a0
from googletrans import Translator
import httpcore

def main():
    print('***** Hello *****')
    file_text = open('file_translate.txt', 'a')

    def write_word():
        original_word = input('Введите слово на Английском: ')
        # translate_word = input('Введите перевод слова: ')
        translator = Translator()

        try:
            result = translator.translate(original_word, src='en', dest='ru')
            translate_word = result.text
            print(f'Перевод на Русский: {result.text}\nСлово c переводом будет записано в файл.'
                  f'\n* * * * * * * * * * * * * * * * * * * *')
            file_text.write(f'{original_word.capitalize()} - {translate_word.capitalize()}\n')

        except httpcore.ConnectError:
            print("* * * Internet is broken! * * *\n* * * Google is not available! * * *")
        except UnboundLocalError:
            print("* * * Internet is broken! * * *\n* * * Google is not available! * * *")

    again = 'е'
    while again.lower() != 'в' and again.lower() != 'd':
        write_word()
        again = input('Нажмите "Enter" чтобы продолжить или "В" для выхода из программы: ')

    # Передача строк файла в список и сортировка по алфавиту
    file_text = open('file_translate.txt', 'r')
    lines_sort = sorted(
        list(set(file_text.readlines())))  # Преобразование в набор и обратно в список для удаления дубликатов

    # Запись отсортированных строк обратно в файл
    file_text = open('file_translate.txt', 'w')
    for item in lines_sort:
        if not item.isspace():  # Удаление пустых строк в файле
            file_text.write(item)

    file_text.close()


if __name__ == '__main__':
    main()
