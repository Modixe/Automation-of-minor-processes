import tkinter as tk
from tkinter import ttk
import sqlite3

import os
import sys

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()


    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)


        btn_open_dialog = tk.Button(toolbar, text='Добавить учётку', command=self.open_dialog, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        btn_folder_creation = tk.Button(toolbar, text = "Создать каталог", command=self.folder_creation, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_folder_creation.pack(side=tk.LEFT)
        btn_folder_creation.pack()

        self.tree = ttk.Treeview(self, columns=('ID', 'title', 'login', 'password', 'email'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('title', width=250, anchor=tk.CENTER)
        self.tree.column('login', width=150, anchor=tk.CENTER)
        self.tree.column('password', width=110, anchor=tk.CENTER)
        self.tree.column('email', width=250, anchor=tk.CENTER)

        self.tree.heading('ID', text='№')
        self.tree.heading('title', text='Название')
        self.tree.heading('login', text='Логин')
        self.tree.heading('password', text='Пароль')
        self.tree.heading('email', text='Электронная почта')

        self.tree.pack()


    def records(self, title, login, password, email):
        self.db.insert_data(title, login, password, email)
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM finance''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]


    def open_dialog(self):
        Child()

    def folder_creation(self):
        folder()

class folder(tk.Toplevel):



    def __init__(self):
        super().__init__(root)
        self.init_folder()
        self.view = app

    def log(self, name):

        self.label_title = tk.Label(self, text=name)
        self.label_title.place(x=5, y=100)

    def show_text(self):
        self.label_text.set('Каталог: ' + self.entry_text.get() + ' создан')
        projectname = self.entry_text.get()
        path = os.path.dirname(sys.argv[0]) + r'/'
        folders = \
            [
                ['Torrent', [
                    ['Downloads', []]
                ]],
                ['Study', [
                    ['Books', []]
                ]],
                ['Programs', [
                    ['', []]
                ]],
                ['Proging', [
                    ['C#', [
                        ['Project', []]
                    ]],
                    ['CSS', [
                        ['Project', []]
                    ]],
                    ['Data', [
                        ['Project', []]
                    ]],
                    ['HTML', [
                        ['Project', []]
                    ]],
                    ['PHP', [
                        ['Project', []]
                    ]],
                    ['Python', [
                        ['Project', []]
                    ]],
                    ['SQL', [
                        ['Project', []]
                    ]],

                ]],
                ['Hobby', [
                    ['Music', []],
                    ['Photo', []],
                    ['Ranobe', []],
                    ['Video', []]
                ]],
                ['Games', [
                    ['', []]
                ]],
                ['Files', [
                    ['Documents', []],
                    ['Password', []],
                    ['Pictures', []],
                    ['Programs', []]
                ]],
                ['Desktop', [
                    ['', []]
                ]],
            ]
        if projectname:
            fullPath = os.path.join(path, projectname)
            self.createFolder(fullPath)
            self.build(fullPath, folders)


    def init_folder(self):

        self.title('Автоматизация')
        self.geometry('400x300+400+300')
        self.resizable(False, False)

        self.name_folder = tk.Label(self, text='Введите название каталога:')
        self.name_folder.place(x=5, y=5)

        self.entry_text = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.entry_text)
        self.entry.place(x=160, y=5)

        self.label_text = tk.StringVar()
        self.label = tk.Label(root, textvariable=self.label_text)
        self.label.pack()

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=210, y=60)

        self.button = ttk.Button(self, text='Создать', command=self.show_text)
        self.button.place(x=210, y=30)
        # # btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_folder_name.get()))
        # btn_ok.bind('Button-1', command=self.log)
        self.grab_set()
        self.focus_set()



    def createFolder(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def build(self, root, data):
        if data:
            for d in data:
                name = d[0]
                path = os.path.join(root, name)
                self.createFolder(path)
                self.build(path, d[1])


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app


    def init_child(self):
        self.title('Добавить запись')
        self.geometry('400x300+400+300')
        self.resizable(False, False)

        label_title = tk.Label(self, text='Наименование:')
        label_title.place(x=50, y=50)
        label_select = tk.Label(self, text='Логин:')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Пароль:')
        label_sum.place(x=50, y=110)
        label_email = tk.Label(self, text='Электронная почта:')
        label_email.place(x=50, y=140)

        self.entry_title = ttk.Entry(self)
        self.entry_title.place(x=200, y=50)

        self.entry_login = ttk.Entry(self)
        self.entry_login.place(x=200, y=110)

        self.entry_password = ttk.Entry(self)
        self.entry_password.place(x=200, y=140)

        self.entry_email = ttk.Entry(self)
        self.entry_email.place(x=200, y=80)

        # self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        # self.combobox.current(0)
        # self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=250, y=170)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.place(x=170, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_title.get(),
                                                                  self.entry_login.get(),
                                                                  self.entry_password.get(),
                                                                  self.entry_email.get()))


        self.grab_set()
        self.focus_set()


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, title text, login text, password text, email text)''')
        self.conn.commit()

    def insert_data(self, title, login, password, email):
        self.c.execute('''INSERT INTO finance(title, login, password, email) VALUES (?, ?, ?, ?)''',
                       (title, login, password, email))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Modixe")
    root.geometry("800x450+300+200")
    root.resizable(False, False)
    root.mainloop()
    
