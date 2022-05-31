from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QButtonGroup,QWidget,QHBoxLayout,QPushButton,QLabel,QRadioButton,QVBoxLayout,QGroupBox
from random import shuffle
from random import randint

class Question():
    def __init__ (self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    
def show_result():
    RadioGroupBox.hide()
    ansgroupbox.show()
    button.setText('Следущий вопрос')

def show_question():
    RadioGroupBox.show()
    ansgroupbox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    answer.setText(q.question)
    nadpis2.setText(q.right_answer)
    show_question()
def show_correct(res):
    nadpis1.setText(res)
    show_result()
    
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика')
        print('-Всего вопросов:',window.total)
        print('Правильных ответов:',window.score)
        print('Рейтинг:',window.score/window.total*100,"%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Статистика')
            print('Неверно')
            print('-Всего вопросов:',window.total)
            print('Правильных ответов:',window.score)
            print('Рейтинг:',window.score/window.total*100, '%')
def next_question():
    cur_question = randint(0,len(questions_list)-1)
    
    q = questions_list[cur_question]
    ask(q)
    window.total += 1
    print('Статистика')
    print('-Всего вопросов:',window.total)
    print('Правильных ответов:',window.score)



def click_ok():
    if button.text() == "Ответить":
        check_answer()
    else:
        next_question()

app = QApplication([])
window = QWidget()
window.resize(600,400)
window.setWindowTitle('Почему-ка')
#создать вопрос
answer = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Атстеки')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_quest = QHBoxLayout()
layout_ques = QHBoxLayout()
layout_quest.addWidget(rbtn_1)
layout_quest.addWidget(rbtn_2)
layout_ques.addWidget(rbtn_3)
layout_ques.addWidget(rbtn_4)
lay = QVBoxLayout()
lay.addLayout(layout_quest)
lay.addLayout(layout_ques)
RadioGroupBox.setLayout(lay)
button = QPushButton('Ответить')
ansgroupbox = QGroupBox('Результат теста')
nadpis1 = QLabel('Прав ты или нет?')
nadpis2 = QLabel('Ответ тут')
layout_quest_ans = QVBoxLayout()
layout_quest_ans.addWidget(nadpis1, alignment=Qt.AlignLeft)
layout_quest_ans.addWidget(nadpis2, alignment = Qt.AlignCenter)
ansgroupbox.setLayout(layout_quest_ans)
ansgroupbox.hide()
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
shuffle(answers)

#создать главный вертикальный лэйаут
layout_quest2 = QVBoxLayout()
#прикрепить к лэйауту виджеты - вопрос, рэдиогрупбокс, кнопку
layout_quest2.addWidget(answer, alignment = Qt.AlignCenter)
layout_quest2.addWidget(RadioGroupBox)
layout_quest2.addWidget(ansgroupbox)
layout_quest2.addWidget(button, alignment = Qt.AlignCenter)

#прикрепить к лэйауту иконку window

q = Question('Выберите пепревод слова "переменная"','variable','variation','changing','variant')
questions_list = []
questions_list.append(q)
q1 = Question(
    'Государственный язык Португалии',
'Португальский',
    'Английский','Испанский','Французкий')
questions_list.append(q1)

q2 = Question(
    'Когда впервые выпустили игру Brawl Stars?',
'11.11.2017',
    '12.04.2020','14.06.2017','8.12.2018')
questions_list.append(q2)

q3 = Question(
    'Кого называли "отцом цифровой революции" и "визионером"?',
'Стив Джобс',
    'Стив Возняк','Дональд Трамп','Тим Кук')
questions_list.append(q3)

q4 = Question(
    'Кто основал компанию "Alibaba Group"?',
'Джек Ма',
    'Илон Маск','Роберт Кийосаки','Никлаус Вирт')
questions_list.append(q4)

q5 = Question(
    'Актер фильма "Тупой и еще тупее", который играл роль Ллойда?',
'Джим Керри',
    'Джим Пан','Павел Тихонов','Кузя')

questions_list.append(q5)

window.total = 0
window.score = 0
next_question()
button.clicked.connect(click_ok)
window.setLayout(layout_quest2)
window.show()
app.exec_()