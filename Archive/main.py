# pip install googletrans==3.1.0a0
from googletrans import Translator
import httpcore
import tkinter
import tkinter.messagebox


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Word translate')
        self.labell = tkinter.Label(self.main_window, text='Введите слово на английском', borderwidth=1, relief='solid')
        self.original_word = tkinter.Entry(self.main_window, width=10)

        self.labell.pack(ipadx=40, ipady=20, padx=10, pady=10)
        self.original_word.pack(ipadx=60, ipady=20, padx=10, pady=10)

        self.translate = tkinter.Button(self.main_window, text='Перевести', command=self.translate)
        self.quit_button = tkinter.Button(self.main_window, text='Выйти', command=self.main_window.destroy)

        self.translate.pack(ipadx=40, ipady=20, padx=10, pady=10)
        self.quit_button.pack(ipadx=20, ipady=20, padx=10, pady=10)

        tkinter.mainloop()

    def translate(self):
        file_text = open('file_translate.txt', 'a')
        translator = Translator()
        try:
            original_word = str(self.original_word.get())
            translate_word = translator.translate(original_word, src='en', dest='ru')

            file_text.write(f'{original_word.capitalize()} - {translate_word.text.capitalize()}\n')

            tkinter.messagebox.showinfo('Перевод: ', str(translate_word.text))

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

        except httpcore.ConnectError:
            tkinter.messagebox.showinfo("Internet is broken! \nGoogle is not available!")
        except UnboundLocalError:
            tkinter.messagebox.showinfo("Internet is broken! \nGoogle is not available!")


if __name__ == '__main__':
    my_gui = GUI()
