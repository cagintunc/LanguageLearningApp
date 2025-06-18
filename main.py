import sqlite3
import random
import main_gui
import gui2
import gui3
import gui4
from PyQt5 import QtWidgets
import sys
import simulator
import gui_notification
import score_gui
import game1
import first_gui
import contin

def get_text(aList):
    print("Alist: ", aList)
    result = ""
    for i in aList.keys():
        if aList[i] != "":
            result += "'" + aList[i] + "'" + ", "
    return result

def set_up_game_1(secret_list):
    instance = game1
    instance.Main().set_up(secret_list, connect)

def find_proper_selection(secret_list, choice, score=0):
    if len(secret_list) > 0:
        random_choice = random.choice(secret_list)
        cur.execute(f"SELECT * FROM {random_choice}")
        my_list = list()
        is_finished = False
        while not is_finished:
            current = cur.fetchone()
            if current == None:
                is_finished = True
                break
            else:
                my_list.append(current)
        if len(my_list) < 3:
            print(f"There is not enough words in {random_choice}.")
            secret_list.remove(random_choice)
            find_proper_selection(secret_list, choice)
        else:
            cur_score = 0
            while len(my_list) >= 3:
                word_1 = random.choice(my_list)
                my_list.remove(word_1)

                word_2 = random.choice(my_list)
                my_list.remove(word_2)

                word_3 = random.choice(my_list)
                my_list.remove(word_3)

                chosen = [word_1, word_2, word_3]
                simu = simulator.Simu(chosen, random_choice, choice)
                simu.set_up()
                cur_score += simu.score

            secret_list.remove(random_choice)
            if len(secret_list) > 0:
                find_proper_selection(secret_list, choice)

            app_s = QtWidgets.QApplication(sys.argv)
            gui_sc = score_gui
            uis = gui_sc.Ui_MainWindow()
            score_gui.main(uis, cur_score)
            app_s.exec_()


def create_table(name, ls):
    cur.execute(f"CREATE TABLE IF NOT EXISTS {name} ({ls})")
    connect.commit()

def insert_to_table(table, values, flag):
    tmp_list = values.split(",")
    values_tmp = ""
    for i in tmp_list[:len(tmp_list)-2]:
        values_tmp += i + ","
    word_name = tmp_list[0]
    okunus = tmp_list[len(tmp_list)-2]
    colors = None
    if flag == 0 or table != "noun":
        colors = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    else:
        artikel = ""
        for i in tmp_list[2].lower():
            if i != " " and i != "'":
                artikel += i
        if "die" == artikel:
            colors = 160, 8, 90
        elif "der" == artikel:
            colors = 10, 144, 255
        else:
            colors = 60, 160, 60
    cur.execute(f"SELECT * FROM {table} WHERE word={word_name}")
    is_there = cur.fetchone()
    # TODO: look whether the word have been already inserted !!!!!!

    if is_there == None:
        print(f"INSERT INTO {table} VALUES ({values_tmp}{0},{0},{okunus},'{colors}')")
        cur.execute(f"INSERT INTO {table} VALUES ({values_tmp}{0},{0},{okunus},'{colors}')")
    else:
        for i in is_there:
            print(i)
        cur.execute(f"SELECT hardness FROM {table} WHERE word={word_name}")
        hardness = cur.fetchone()
        updated = str(int(hardness[0])+1)
        cur.execute(f"UPDATE {table} SET hardness={updated} "
                    f"WHERE word={word_name}")
    connect.commit()

def get_sql_text(array, nounType):
    text = None
    if nounType == "phrase":
        text = f"'{array[0]}', '{array[1]}', '{array[2]}'"
    elif nounType == "verb":
        text = f"'{array[0]}', '{array[1]}', '{array[2]}', '{array[3]}'," \
               f"'{array[4]}', '{array[5]}', '{array[6]}', '{array[7]}', " \
               f"'{array[8]}', '{array[9]}', '{array[10]}', '{array[11]}', '{array[12]}'"
    elif nounType == "noun":
        text = f"'{array[0]}', '{array[1]}', '{array[2]}', '{array[3]}', '{array[4]}'"
    else:
        text = f"'{array[0]}', '{array[1]}', '{array[2]}', '{array[3]}'"

    return text

def english():
    create_table("noun", "word TEXT, meaning TEXT, score INT, hardness INT, pronounce TEXT, color TEXT")
    create_table("adjective", "word TEXT, meaning TEXT, preposition TEXT,"
                              "score INT, hardness INT, pronounce TEXT, color TEXT")
    create_table("adverb", "word TEXT, meaning TEXT, score INT, hardness INT, pronounce TEXT, color TEXT")
    create_table("verb", "word TEXT, meaning TEXT, preposition TEXT, is_gerund TEXT,"
                         "score INT, hardness INT, pronounce TEXT, color TEXT")
    create_table("phrase", "word TEXT, meaning TEXT, score INT, hardness INT, pronounce TEXT, color TEXT")
    app2 = QtWidgets.QApplication(sys.argv)
    mg = main_gui
    ui2 = mg.Ui_MainWindow()
    mg.main(ui2)
    app2.exec_()
    value = mg.get_values(ui2)

    if value == 1:
        g0 = gui_notification
        ui0 = g0.Ui_MainWindow()
        app0 = QtWidgets.QApplication(sys.argv)
        g0.main(ui0)
        app0.exec_()
        g2 = gui2
        ui1 = g2.Ui_MainWindow()
        app = QtWidgets.QApplication(sys.argv)
        g2.main(ui1)
        app.exec_()
        noun_type = g2.get_values(ui1)
        app_2 = QtWidgets.QApplication(sys.argv)
        my_gui = gui3
        ui = my_gui.Ui_MainWindow(noun_type)
        my_gui.main(ui)
        values = my_gui.get_values(ui)
        app_2.exec_()
        insert_to_table(noun_type.lower(), get_text(values), 0)

    elif value == 2:
        secret_list = ["noun", "adjective", "adverb", "verb", "phrase"]
        find_proper_selection(secret_list, 1)

    elif value == 3:
        secret_list = ["noun", "adjective", "adverb", "verb"]
        set_up_game_1(secret_list)

    elif value == 4:
        # new game
        pass

def german():
    create_table("noun", "word TEXT, meaning TEXT, artikel TEXT, plural TEXT, "
                         "score INT, hardness INT, "
                         "shape TEXT, color TEXT")
    create_table("adjective", "word TEXT, meaning TEXT, antonym TEXT,"
                              "score INT, hardness INT, shape TEXT, color TEXT")
    create_table("adverb", "word TEXT, meaning TEXT, antonym TEXT, score INT, hardness INT,"
                           " shape TEXT, color TEXT")
    create_table("verb", "word TEXT, meaning TEXT, dativ_akkusativ TEXT, preposition TEXT,"
                         "ich TEXT, du TEXT, Sie_singular TEXT, er_sie_es TEXT, wir TEXT,"
                         "ihr TEXT, Sie_plural TEXT, sie TEXT,"
                         "score INT, hardness INT, shape TEXT, color TEXT")
    create_table("phrase", "word TEXT, meaning TEXT, score INT, hardness INT, shape TEXT, color TEXT")
    app2 = QtWidgets.QApplication(sys.argv)
    mg = main_gui
    ui2 = mg.Ui_MainWindow()
    mg.main(ui2)
    app2.exec_()
    value = mg.get_values(ui2)
    if value == 1:
        g0 = gui_notification
        ui0 = g0.Ui_MainWindow()
        app0 = QtWidgets.QApplication(sys.argv)
        g0.main(ui0)
        app0.exec_()

        g2 = gui2
        ui1 = g2.Ui_MainWindow()
        app = QtWidgets.QApplication(sys.argv)
        g2.main(ui1)
        app.exec_()
        noun_type = g2.get_values(ui1)

        app_2 = QtWidgets.QApplication(sys.argv)
        my_gui = gui4
        ui = my_gui.Ui_MainWindow(noun_type)
        my_gui.main(ui)
        app_2.exec_()
        values = my_gui.get_values(ui)
        sql_text = get_sql_text(values, noun_type.lower())
        insert_to_table(noun_type.lower(), sql_text, 1)

    elif value == 2:
        secret_list = ["noun", "adjective", "adverb", "verb", "phrase"]
        find_proper_selection(secret_list, 0)

    elif value == 3:
        secret_list = ["noun", "adjective", "adverb", "verb"]
        set_up_game_1(secret_list)


tmp = ["databases\\german.db", "databases\\english.db"]
app = QtWidgets.QApplication(sys.argv)
instance = first_gui
ui = instance.Ui_MainWindow()
instance.main(ui)
app.exec_()
val1 = instance.get_result(ui)
connect = sqlite3.connect(tmp[val1])
cur = connect.cursor()
result = 0
if val1 == 0:
    while result == 0:
        german()
        app7 = QtWidgets.QApplication(sys.argv)
        instance2 = contin
        ui = instance2.Ui_MainWindow()
        instance2.main(ui)
        result = ui.result
        app7.exec_()


elif val1 == 1:
    while result == 0:
        english()
        app8 = QtWidgets.QApplication(sys.argv)
        instance2 = contin
        ui = instance2.Ui_MainWindow()
        instance2.main(ui)
        result = ui.result
        app8.exec_()
connect.close()