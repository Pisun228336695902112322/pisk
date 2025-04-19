from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QMessageBox)
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = list()
question_list.append(Question('Ветилй Чикатилин Когда помер?', 'Вчера', 'гавно', 'сегодня', 'Сейчас'))
question_list.append(Question('Когда некита спалит номер телефона чтобы купить кредит', 'Некогда', 'Сейчас скажет', 'Ага', 'Спалил'))
question_list.append(Question('Влад а4 атдаст свой акаунт', 'Гав Гав', 'Я ква ква квадробер', 'Мяу мяу', 'Некита пали номер телефона'))
question_list.append(Question('Ты кокашка', 'Эщкере', 'Нет', 'Да', 'Эщ эщ эщ'))
question_list.append(Question('1 Лат энэрге вам или 2 другому', '2 другому', 'мне', 'Эщкере', '8 другому'))
question_list.append(Question('卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐', 'Вентиляторы', 'Много букавка', 'ПАСХАЛКА', 'СТрашила'))
question_list.append(Question('Вы хамстер куриминальни?', 'Кандиции', '10 лат энэрге мне', 'Э', 'Максим Ишак'))



app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Максим какашка')
14
RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Да')
rbtn_2 = QRadioButton('Конечно')
rbtn_3 = QRadioButton('Ес')
rbtn_4 = QRadioButton('нет')

RadioGroup =QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout() #H
layout_ans2 = QVBoxLayout() #V
layout_ans3 = QVBoxLayout() #V
layout_ans2.addWidget(rbtn_1) #L_2, rbtn_1
layout_ans2.addWidget(rbtn_2) #_2, rbtn_2
layout_ans3.addWidget(rbtn_3) #_3, rbtn_3
layout_ans3.addWidget(rbtn_4) #_4, rbtn_4

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_Result = QLabel('Никита')
lb_Correct = QLabel('инапланетяне')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
RadioGroupBox.show()
AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong2)
    answers[2].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правельна!')
        window.score +=1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('卐')

def next_question():

    window.total += 1
    print('Статистика:', window.total)
    print('Количество вопросов:', window.total)
    print('Рейтинг (% правильных ответов):', window.score/window.total*100)

    cur_question = randint(0,len(question_list)-1)
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
            
btn_OK.clicked.connect(click_OK)

window = QWidget()
window.resize(400, 400)

window.cur_question = -1
window.setLayout(layout_card)
window.setWindowTitle('Эщкере')
window.show()
window.total = 0
window.score = 0
next_question()
app.exec()