import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

library_file = 'library.json'

def load_library():
    if os.path.exists(library_file):
        with open(library_file, 'r') as file:
            return json.load(file)
    return []

def save_library():
    with open(library_file, 'w') as file:
        json.dump(library, file, indent=4)

library = load_library()

def add_book():
    title = simpledialog.askstring("Добавить книгу", "Введите название книги:")
    if not title or not title.strip():
        messagebox.showerror("Ошибка", "Название книги не может быть пустым!")
        return

    author = simpledialog.askstring("Добавить книгу", "Введите автора книги:")
    if not author or not author.strip():
        messagebox.showerror("Ошибка", "Автор книги не может быть пустым!")
        return

    year = simpledialog.askstring("Добавить книгу", "Введите год издания книги:")
    if not year or not year.strip():
        messagebox.showerror("Ошибка", "Год издания книги не может быть пустым!")
        return

    genre = simpledialog.askstring("Добавить книгу", "Введите жанр книги:")
    if not genre or not genre.strip():
        messagebox.showerror("Ошибка", "Жанр книги не может быть пустым!")
        return

    book = {'title': title.strip(), 'author': author.strip(), 'year': year.strip(), 'genre': genre.strip(), 'text': ''}
    library.append(book)
    save_library()
    messagebox.showinfo("Добавление книги", f"Книга '{title.strip()}' добавлена в библиотеку.")

def remove_book():
    title = simpledialog.askstring("Удалить книгу", "Введите название книги для удаления:")
    if not title or not title.strip():
        messagebox.showerror("Ошибка", "Название книги не может быть пустым!")
        return

    title = title.strip().lower()
    global library
    original_length = len(library)

    # Создаем новый список без книги с заданным названием
    new_library = []
    for book in library:
        if isinstance(book, dict) and book.get('title') and book['title'].lower() == title:
            continue  # Пропускаем книгу для удаления
        new_library.append(book)

    # Если размер библиотеки изменился, сохраняем изменения
    if len(new_library) < len(library):
        library = new_library
        save_library()
        messagebox.showinfo("Удаление книги", f"Книга '{title}' удалена из библиотеки.")
    else:
        messagebox.showerror("Ошибка", f"Книга '{title}' не найдена.")

def find_book(title=None, author=None, year=None):
    if not title and not author and not year:
        title = simpledialog.askstring("Найти книгу", "Введите название книги для поиска:")
        if not title or not title.strip():
            messagebox.showerror("Ошибка", "Название книги не может быть пустым!")
            return

    title = title.strip().lower()
    book_found = False
    for book in library:
        if isinstance(book, dict) and book.get('title') and book['title'].lower() == title:
            details = (
                f"Название: {book['title']}\n"
                f"Автор: {book['author']}\n"
                f"Год издания: {book['year']}\n"
                f"Жанр: {book['genre']}"
            )
            messagebox.showinfo("Поиск книги", details)
            book_found = True
            break

    if not book_found:
        messagebox.showerror("Ошибка", f"Книга '{title}' не найдена.")

def find_book_by_author():
    author = simpledialog.askstring("Найти книги по автору", "Введите имя автора для поиска:")
    if not author or not author.strip():
        messagebox.showerror("Ошибка", "Имя автора не может быть пустым!")
        return

    author = author.strip().lower()
    books_found = False
    for book in library:
        if isinstance(book, dict) and book.get('author') and book['author'].lower() == author:
            details = (
                f"Название: {book['title']}\n"
                f"Автор: {book['author']}\n"
                f"Год издания: {book['year']}\n"
                f"Жанр: {book['genre']}"
            )
            messagebox.showinfo("Поиск книг по автору", details)
            books_found = True

    if not books_found:
        messagebox.showerror("Ошибка", f"Книги автора '{author}' не найдены.")

def find_book_by_year():
    year = simpledialog.askstring("Найти книги по году издания", "Введите год издания для поиска:")
    if not year or not year.strip():
        messagebox.showerror("Ошибка", "Год издания не может быть пустым!")
        return

    year = year.strip()
    books_found = False
    for book in library:
        if isinstance(book, dict) and book.get('year') and book['year'] == year:
            details = (
                f"Название: {book['title']}\n"
                f"Автор: {book['author']}\n"
                f"Год издания: {book['year']}\n"
                f"Жанр: {book['genre']}"
            )
            messagebox.showinfo("Поиск книг по году издания", details)
            books_found = True

    if not books_found:
        messagebox.showerror("Ошибка", f"Книги издания '{year}' не найдены.")

def list_books():
    if library:
        books_info = []
        for book in library:
            info = (
                f"Название: {book['title']}\n"
                f"Автор: {book['author']}\n"
                f"Год издания: {book['year']}\n"
                f"Жанр: {book['genre']}\n"
                "---------------------------"
            )
            books_info.append(info)

        books_list = "\n\n".join(books_info)
        messagebox.showinfo("Список книг в библиотеке", books_list)
    else:
        messagebox.showinfo("Список книг в библиотеке", "Библиотека пуста.")

def edit_book():
    title = simpledialog.askstring("Редактировать книгу", "Введите название книги для редактирования:")
    if not title or not title.strip():
        messagebox.showerror("Ошибка", "Название книги не может быть пустым!")
        return

    title = title.strip().lower()
    global library

    book_found = False
    for book in library:
        if isinstance(book, dict) and book.get('title') and book['title'].lower() == title:
            new_title = simpledialog.askstring("Редактировать книгу", "Введите новое название (оставьте пустым для сохранения текущего): ")
            new_author = simpledialog.askstring("Редактировать книгу", "Введите нового автора (оставьте пустым для сохранения текущего): ")
            new_year = simpledialog.askstring("Редактировать книгу", "Введите новый год издания (оставьте пустым для сохранения текущего): ")
            new_genre = simpledialog.askstring("Редактировать книгу", "Введите новый жанр (оставьте пустым для сохранения текущего): ")

            if new_title is not None and new_title.strip() != "":
                book['title'] = new_title.strip()
            if new_author is not None and new_author.strip() != "":
                book['author'] = new_author.strip()
            if new_year is not None and new_year.strip() != "":
                book['year'] = new_year.strip()
            if new_genre is not None and new_genre.strip() != "":
                book['genre'] = new_genre.strip()

            book_found = True
            break

    if book_found:
        save_library()
        messagebox.showinfo("Редактирование книги", f"Книга '{title}' успешно обновлена.")
    else:
        messagebox.showerror("Ошибка", f"Книга '{title}' не найдена.")

def add_book_text():
    title = simpledialog.askstring("Добавить текст книги", "Введите название книги для добавления текста:")
    if not title or not title.strip():
        messagebox.showerror("Ошибка", "Название книги не может быть пустым!")
        return

    title = title.strip().lower()
    global library

    for book in library:
        if isinstance(book, dict) and book.get('title') and book['title'].lower() == title:
            text = simpledialog.askstring("Добавить текст книги", "Введите текст книги:")
            if text:
                book['text'] = text
                save_library()
                messagebox.showinfo("Добавление текста", f"Текст книги '{title}' добавлен.")
            return

    messagebox.showerror("Ошибка", f"Книга '{title}' не найдена в библиотеке.")

def view_book_text():
    title = simpledialog.askstring("Просмотр текста книги", "Введите название книги для просмотра текста:")
    if not title or not title.strip():
        messagebox.showerror("Ошибка", "Название книги не может быть пустым!")
        return

    title = title.strip().lower()
    global library

    for book in library:
        if isinstance(book, dict) and book.get('title') and book['title'].lower() == title:
            if 'text' in book and book['text']:
                messagebox.showinfo(f"Текст книги '{title}'", book['text'])
            else:
                messagebox.showinfo(f"Текст книги '{title}'", "Текст книги отсутствует.")
            return

    messagebox.showerror("Ошибка", f"Книга '{title}' не найдена в библиотеке.")

def change_theme():
    theme_choice = theme_var.get()
    if theme_choice == 'light':
        root.configure(bg='white')
        style.theme_use('clam')
    elif theme_choice == 'dark':
        root.configure(bg='darkgray')
        style.theme_use('clam')

def main():
    global root, style, theme_var
    root = tk.Tk()
    root.title("Управление библиотекой")

    # Создание стиля для кнопок
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12), padding=10)

    # Создание рамок и разделителей
    separator = ttk.Separator(root, orient='horizontal')
    separator.pack(fill='x', padx=10, pady=10)

    # Выбор цветовой схемы
    theme_var = tk.StringVar(root, value='light')
    light_theme_button = ttk.Radiobutton(root, text='Светлая тема', value='light', variable=theme_var, command=change_theme)
    dark_theme_button = ttk.Radiobutton(root, text='Темная тема', value='dark', variable=theme_var, command=change_theme)
    light_theme_button.pack()
    dark_theme_button.pack()

    # Создание кнопок
    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=10)

    ttk.Button(buttons_frame, text="Добавить книгу", command=add_book).pack(side='left', padx=5)
    ttk.Button(buttons_frame, text="Удалить книгу", command=remove_book).pack(side='left', padx=5)
    ttk.Button(buttons_frame, text="Найти книгу по названию", command=find_book).pack(side='left', padx=5)
    ttk.Button(buttons_frame, text="Найти книги по автору", command=find_book_by_author).pack(side='left', padx=5)
    ttk.Button(buttons_frame, text="Найти книги по году издания", command=find_book_by_year).pack(side='left', padx=5)
    ttk.Button(buttons_frame, text="Показать все книги", command=list_books).pack(side='left', padx=5)
    ttk.Button(buttons_frame, text="Редактировать книгу", command=edit_book).pack(side='left', padx=5)
    ttk.Button(buttons_frame, text="Добавить текст книги", command=add_book_text).pack(side='left', padx=5)
    ttk.Button(buttons_frame, text="Просмотреть текст книги", command=view_book_text).pack(side='left', padx=5)
    ttk.Button(buttons_frame, text="Выйти", command=root.quit).pack(side='left', padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()