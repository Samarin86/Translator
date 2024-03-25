# pip install googletrans==3.1.0a0
from googletrans import Translator
import httpcore
import tkinter
import tkinter.messagebox


class GUI:
    def __init__(self):
        """
        Initializes the Word Translator application.

        This function creates the main window of the application and sets its title. It also creates two frames:
        `top_frame` and `botton_frame`. Inside the `top_frame`, it creates a label and an entry widget for the user
        to input an English word. Inside the `botton_frame`, it creates two buttons: one for translating the word
        and another for quitting the application.

        Parameters:
            None

        Returns:
            None
        """
        self.main_window = tkinter.Tk()
        self.main_window.title('Word translate')
        self.top_frame = tkinter.Frame()
        self.botton_frame = tkinter.Frame()

        self.labell = tkinter.Label(self.top_frame, text='Введите слово на английском:', borderwidth=1, relief='solid',
                                    background='sandybrown', font=('Helvetica', 14, 'bold'))
        self.original_word = tkinter.Entry(self.top_frame, width=30, justify='center', background='gray',
                                           font=('Helvetica', 12, 'bold'), cursor='draft_small')

        self.labell.pack(side='left', ipadx=40, ipady=20, padx=10, pady=10)
        self.original_word.pack(side='left', ipadx=60,
                                ipady=20, padx=10, pady=10)
        self.top_frame.pack()
        self.translate = tkinter.Button(self.botton_frame, text='Перевести', background='sandybrown',
                                        font=('Helvetica', 12, 'bold'), command=self.translate)

        self.quit_button = tkinter.Button(self.botton_frame, text='Выйти', background='sandybrown',
                                          font=('Helvetica', 12, 'bold'), command=self.main_window.destroy)

        self.translate.pack(side='left', ipadx=40, ipady=5, padx=10, pady=5)
        self.quit_button.pack(side='left', ipadx=20, ipady=5, padx=10, pady=5)
        self.botton_frame.pack()

        tkinter.mainloop()

    def translate(self):
        """
        A function that translates a word from English to Russian and saves the translation in a file.
        Uses the Google Translate API for translation. Handles exceptions for internet connection 
        issues and unbound local errors.
        """
        file_text = open('file_translate.txt', 'a')
        translator = Translator()
        try:
            original_word = str(self.original_word.get())
            translate_word = translator.translate(
                original_word, src='en', dest='ru')

            file_text.write(
                f'{original_word.capitalize()} - {translate_word.text.capitalize()}\n')
            tkinter.messagebox.showinfo('Перевод: ', str(translate_word.text))

            file_text = open('file_translate.txt', 'r')
            lines_sort = sorted(
                list(set(file_text.readlines())))

            file_text = open('file_translate.txt', 'w')
            for item in lines_sort:
                if not item.isspace():
                    file_text.write(item)

            file_text.close()

        except httpcore.ConnectError:
            tkinter.messagebox.showinfo(
                "Internet is broken!", str("Google is not available!"))
        except UnboundLocalError:
            tkinter.messagebox.showinfo(
                "Internet is broken!", str("Google is not available!"))


if __name__ == '__main__':
    my_gui = GUI()
