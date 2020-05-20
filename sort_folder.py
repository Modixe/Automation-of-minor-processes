import os
import shutil
import time
import sys

class sortFolder(object):
    def __init__(self):

        self.assembly_by_category = dict()  # Сртировка файлов по типу
        self.folder_catalog = list()  # Содержит имена папок в каталоге
        self.all_files_catalog = list()  # Содержит расширения всех файлов в каталоге
        self.file_all = {}  # Кортеж содержащий элементы каталога
        self.read_catalog()  # Считывание каталога
        self.db_catalog()  # Хранение дерева каталога
        self.sort_catalog()  # Сортировка каталога
        self.sort_folder()  # Отсеивание папок каталогов
        self.create_catalog()  # Создание каталога
        self.file_transfer()  # Перенос файлов
        self.copy_file()  # Копирует файлы
        self.time()  # Время выполнения программы

    def create_catalog(self):  # Создание каталога (получем расширение файла)

        # Сравниваем списки, удаляем все повторяющие элементы
        result = list(set(self.all_files_catalog) - set(self.folder_catalog))

        if result.__len__() != 0:  # Есть ли папки для создания
            for a in result:
                os.mkdir("donwlaod/" + a)
            print('Созданы папки: \n ', result)
        else:
            print("Все папки уже созданы")

    def read_catalog(self):  # Чтение каталога
        files = os.listdir(path="donwlaod")  # Считывает содержимое директории
        path_to_catalog = 'donwlaod/dll'

        for test in files:
            file_name = os.path.splitext(test)[0]  # Считываем имя файла
            file_extension = os.path.splitext(test)[1][1:]  # Считываем расширение файла,Удаляем первый символ
            self.file_all[file_name] = file_extension  # Заполняем словарь(имя файла: расширение)
        ttt = sorted(self.file_all.values())
        print(ttt)

        self.list_extension = list(self.file_all.values())  # Создаем список с расширениями

    def sort_catalog(self):  # Сортировка файла по каталогам
        type_files = sorted(self.file_all.values())  # считываем расширение файлов
        ttt = ''
        for type_file in type_files:
            if ttt == type_file:
                pass
            else:
                ttt = type_file
                self.all_files_catalog.append(type_file)

        print('Расширение в каталоге: \n', self.all_files_catalog)

    def sort_folder(self):  # В общем каталоге ищем уже созданные папки
        for a in self.file_all.items():
            if a[1] == "":  # Если нет расширения то записать имя
                self.folder_catalog.append(a[0])
        print('Папки в каталоге: \n', self.folder_catalog)

    def file_transfer(self):  # Перенос файлов по каталогам
        # self.assembly_by_category = {val: [val] for key, val in self.file_all.items()}
        i = 0
        self.assembly_by_category = {val: [] for val in self.folder_catalog}
        for x in self.all_files_catalog:  # список со всеми расширениями
            for val, key in sorted(self.file_all.items()):  # список имя файла, расширение в дерректории
                temp = str(val + "." + key)

                if key == x:
                    self.assembly_by_category[key].append(temp)
                    print("Успех")

                elif val == "":
                    print("folder")
                else:
                    i = i + 1
                    # print(i, "error", )
        print("Сортировка по типу выполнена. ")

    def copy_file(self):

        dir_from = 'donwlaod'  # указать директорию, где лежат необходимые файлы
        dir_to = 'donwlaod'  # указать директорию куда нужно перенести (или скопировать файлы)

        for k, v in self.assembly_by_category.items():

            # для определения файлов с расширением .txt, достаточно убедиться в наличии 2-х букв t в нужных позициях
            if v.__len__ == 0:
                pass
            else:
                for x in v:
                    shutil.move(dir_from + "\\" + x, dir_to + "\\" + k)  # эта команда переносит! файлы

    def db_catalog(self):  # Хранение созданных каталогов
        pass

    def add_db_catalog(self):  # Добавление в базу новые имена каталога
        pass

    def test_catalog(self):  # проверка каталога
        pass

    def time(self):

        print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
sortFolder()
