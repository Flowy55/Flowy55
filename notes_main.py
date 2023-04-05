import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QPushButton,
    QLabel, QInputDialog, QWidget, QVBoxLayout,
    QHBoxLayout, QListWidget,
    QLineEdit, QTextEdit
    )
##############################################
app=QApplication([])
window = QWidget()
window.setWindowTitle('Умные заметки')
window.resize(900, 600)
field_text = QTextEdit()
list_notes_Label = QLabel('Список заметок')
list_notes = QListWidget()
button_note_create = QPushButton('Создать заметку')
button_note_save = QPushButton('Сохранить заметку')
button_note_del = QPushButton('Удалить заметку')
list_tags_Label=QLabel('Список тегов')
list_tags=QListWidget()
line_text = QLineEdit('')
line_text.setPlaceholderText('Введите тег...')
button_tag_add = QPushButton('Удалить тег...')
button_tag_del = QPushButton('Поиск по тегу...')
button_tag_search = QPushButton('Поиск по тегу...')
layout = QVBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()
col_1.addWidget(field_text)
col_2.addWidget(list_notes_Label)
col_1.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_Label)
col_2.addWidget(list_tags)
col_2.addWidget(line_text)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QVBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)
layout.addLayout(col_1)
layout.addLayout(col_2)
window.setLayout(layout)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(window, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != '':
        notes[note_name] = {'текст': '', 'теги' : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])
        print(notes)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys = True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для сохранения не вабрана!')

def del_note():
    if list_notes.selectedItems()[0].text():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
            print(notes)
    else:
        print('Заметка для удаления не выбрана!')

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list.tags.addItems(tag)
            list_notes.clear()
            with open('notes_data.json', 'w', encoding='utf8') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)
            print(notes)
        else:
            print('Заметки для добавления тега выбрана!')

def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItem(notes[key]['теги'])
        with open('notes_data.json', 'w', encoding='utf8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    
    else:
        print('Тег для удаления')

def search_tag():
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag_search.text() == 'Искать заметки по тегу' and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note]=notes[note]
        button_tag_search.setText('Сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItem(notes_filtered)
        print(button_tag_search.text())
    elif button_tag_search.text() == 'Сбросить поиск':
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItem(notes)
        button_tag_search.setText('Искать заметки по тегу')
        print(button_tag_search.text())


button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_note)
button_tag_search.clicked.connect(search_tag)

with open('notes_data.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)
list_notes.addItems(notes)

window.show()
app.exec()