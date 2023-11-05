from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QCheckBox, QLabel, QMainWindow, \
    QPushButton, QFontComboBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QPainter, QPixmap, QIcon
import sys


app = QApplication([])
app.setApplicationName("WinPostInstaller")


window = QWidget()
window.setGeometry(650, 300, 750, 400)
window.setWindowTitle("WinPostInstaller")
window.setStyleSheet("background-color: #1E1E1E;")

layout = QHBoxLayout(window)

column_layout1 = QVBoxLayout()
column_layout2 = QVBoxLayout()
column_layout3 = QVBoxLayout()
column_layout4 = QVBoxLayout()
column_layout5 = QVBoxLayout()


checkbox1 = QCheckBox("Discord")
checkbox2 = QCheckBox("Zoom")
checkbox3 = QCheckBox("Telegram")
checkbox4 = QCheckBox("Yandex Browser")
checkbox5 = QCheckBox("Vivaldi")
checkbox6 = QCheckBox("BraveBrowser")
checkbox7 = QCheckBox("Chrome")
checkbox8 = QCheckBox("AnyDesk")
checkbox9 = QCheckBox("WinRar")
checkbox10 = QCheckBox("Steam")
checkbox11 = QCheckBox("Epic Games Launcher")
checkbox12 = QCheckBox("MSI Afterburner")
checkbox13 = QCheckBox("CPU-Z")
checkbox14 = QCheckBox("LA Pleer")
checkbox15 = QCheckBox("Nvidia GeForce Experience")


label1 = QLabel("")
label2 = QLabel("")
label3 = QLabel("")
label4 = QLabel("")
label5 = QLabel("")
label6 = QLabel("")
label7 = QLabel("")
label8 = QLabel("")
label9 = QLabel("")
label10 = QLabel("")
label11 = QLabel("")
label12 = QLabel("")
label13 = QLabel("")
label14 = QLabel("")
label15 = QLabel("")
status_label = QLabel()
status_label.setStyleSheet("color: white;")


column_layout1.addWidget(checkbox1)
column_layout1.addWidget(label1)
column_layout1.addWidget(checkbox2)
column_layout1.addWidget(label2)
column_layout1.addWidget(checkbox3)
column_layout1.addWidget(label3)
column_layout1.addWidget(checkbox4)
column_layout1.addWidget(label4)
column_layout1.addWidget(checkbox5)
column_layout1.addWidget(label5)

column_layout2.addWidget(checkbox6)
column_layout2.addWidget(label6)
column_layout2.addWidget(checkbox7)
column_layout2.addWidget(label7)
column_layout2.addWidget(checkbox8)
column_layout2.addWidget(label8)
column_layout2.addWidget(checkbox9)
column_layout2.addWidget(label9)
column_layout2.addWidget(checkbox10)
column_layout2.addWidget(label10)

column_layout3.addWidget(checkbox11)
column_layout3.addWidget(label11)
column_layout3.addWidget(checkbox12)
column_layout3.addWidget(label12)
column_layout3.addWidget(checkbox13)
column_layout3.addWidget(label13)
column_layout3.addWidget(checkbox14)
column_layout3.addWidget(label14)
column_layout3.addWidget(checkbox15)
column_layout3.addWidget(label15)

layout.addLayout(column_layout1)
layout.addSpacing(20)
layout.addLayout(column_layout2)
layout.addSpacing(20)
layout.addLayout(column_layout3)
layout.addSpacing(20)
layout.addLayout(column_layout4)
layout.addSpacing(20)
layout.addLayout(column_layout5)


checkbox_states = {checkbox1: checkbox1.isChecked(), checkbox2: checkbox2.isChecked(), checkbox3: checkbox3.isChecked(),
                   checkbox4: checkbox4.isChecked(), checkbox5: checkbox5.isChecked(), checkbox6: checkbox6.isChecked(),
                   checkbox7: checkbox7.isChecked(), checkbox8: checkbox8.isChecked(), checkbox9: checkbox9.isChecked(),
                   checkbox10: checkbox10.isChecked(), checkbox11: checkbox11.isChecked(),
                   checkbox12: checkbox12.isChecked(), checkbox13: checkbox13.isChecked(),
                   checkbox14: checkbox14.isChecked(), checkbox15: checkbox15.isChecked()}


selected_count = sum(checkbox_states.values())
status_label.setText(f"Выбрано {selected_count} пункт(ов):")


def update_selected_count():
    selected_counter = sum(checkbox_states.values())
    status_label.setText(f"Выбрано {selected_counter} пункт(ов):")


def checkbox_changed():
    sender = window.sender()
    checkbox_states[sender] = sender.isChecked()
    update_selected_count()


checkbox1.stateChanged.connect(checkbox_changed)
checkbox2.stateChanged.connect(checkbox_changed)
checkbox3.stateChanged.connect(checkbox_changed)
checkbox4.stateChanged.connect(checkbox_changed)
checkbox5.stateChanged.connect(checkbox_changed)
checkbox6.stateChanged.connect(checkbox_changed)
checkbox7.stateChanged.connect(checkbox_changed)
checkbox8.stateChanged.connect(checkbox_changed)
checkbox9.stateChanged.connect(checkbox_changed)
checkbox10.stateChanged.connect(checkbox_changed)
checkbox11.stateChanged.connect(checkbox_changed)
checkbox12.stateChanged.connect(checkbox_changed)
checkbox13.stateChanged.connect(checkbox_changed)
checkbox14.stateChanged.connect(checkbox_changed)
checkbox15.stateChanged.connect(checkbox_changed)


select_button = QPushButton("Выбрать и установить")
cancel_button = QPushButton("Отмена")


def select_button_clicked():
    for checkbox, state in checkbox_states.items():
        if state:
            print(checkbox.text())
            print("Выбрать и установить")


def cancel_button_clicked():
    global checkbox_states
    for checkbox in checkbox_states.keys():
        checkbox.setChecked(False)
    checkbox_states = {checkbox: False for checkbox in checkbox_states.keys()}
    update_selected_count()
    print("Отменить выбор")


select_button.clicked.connect(select_button_clicked)
cancel_button.clicked.connect(cancel_button_clicked)


checkbox_style = """
QCheckBox {
    color: white
}
"""


select_button.setStyleSheet("background-color: #F0FFFF; border-color: #E6E6FA; border-style: solid; border-width: 4px; border-radius: 6px; color: black;")
cancel_button.setStyleSheet("background-color: #F0FFFF; border-color: #00CED1; border-style: solid; border-width: 4px; border-radius: 6px; color: black;")
checkbox1.setStyleSheet(checkbox_style)
checkbox2.setStyleSheet(checkbox_style)
checkbox3.setStyleSheet(checkbox_style)
checkbox4.setStyleSheet(checkbox_style)
checkbox5.setStyleSheet(checkbox_style)
checkbox6.setStyleSheet(checkbox_style)
checkbox7.setStyleSheet(checkbox_style)
checkbox8.setStyleSheet(checkbox_style)
checkbox9.setStyleSheet(checkbox_style)
checkbox10.setStyleSheet(checkbox_style)
checkbox11.setStyleSheet(checkbox_style)
checkbox12.setStyleSheet(checkbox_style)
checkbox13.setStyleSheet(checkbox_style)
checkbox14.setStyleSheet(checkbox_style)
checkbox15.setStyleSheet(checkbox_style)

button_layout = QHBoxLayout()
button_layout.addStretch(1)
button_layout.addWidget(select_button)
button_layout.addWidget(cancel_button)

status_layout = QHBoxLayout()
status_layout.addWidget(status_label, alignment=Qt.AlignLeft | Qt.AlignBottom)
layout.addLayout(status_layout)


layout.addLayout(button_layout)


icon1 = QIcon(r"discord.png")
icon2 = QIcon(r"zoom.png")
icon3 = QIcon(r"telegram.png")
icon4 = QIcon(r"yandex.png")
icon5 = QIcon(r"vivaldi.png")
icon6 = QIcon(r"brave.png")
icon7 = QIcon(r"chrome.png")
icon8 = QIcon(r"anyDesk.png")
icon9 = QIcon(r"winRar.png")
icon10 = QIcon(r"steam.png")
icon11 = QIcon(r"epicGames.png")
icon12 = QIcon(r"msiAfterburner.png")
icon13 = QIcon(r"cpu-z.png")
icon14 = QIcon(r"laPleer.png")
icon15 = QIcon(r"geforceExperience.png")

checkbox1.setIcon(icon1)
checkbox2.setIcon(icon2)
checkbox3.setIcon(icon3)
checkbox4.setIcon(icon3)
checkbox5.setIcon(icon3)
checkbox6.setIcon(icon3)
checkbox7.setIcon(icon3)
checkbox8.setIcon(icon3)
checkbox9.setIcon(icon3)
checkbox10.setIcon(icon3)
checkbox11.setIcon(icon3)
checkbox12.setIcon(icon3)
checkbox13.setIcon(icon3)
checkbox14.setIcon(icon3)
checkbox15.setIcon(icon3)

icon_size = 20
checkbox1.setIconSize(QSize(icon_size, icon_size))
checkbox2.setIconSize(QSize(icon_size, icon_size))
checkbox3.setIconSize(QSize(icon_size, icon_size))
checkbox4.setIconSize(QSize(icon_size, icon_size))
checkbox5.setIconSize(QSize(icon_size, icon_size))
checkbox6.setIconSize(QSize(icon_size, icon_size))
checkbox7.setIconSize(QSize(icon_size, icon_size))
checkbox8.setIconSize(QSize(icon_size, icon_size))
checkbox9.setIconSize(QSize(icon_size, icon_size))
checkbox10.setIconSize(QSize(icon_size, icon_size))
checkbox11.setIconSize(QSize(icon_size, icon_size))
checkbox12.setIconSize(QSize(icon_size, icon_size))
checkbox13.setIconSize(QSize(icon_size, icon_size))
checkbox14.setIconSize(QSize(icon_size, icon_size))
checkbox15.setIconSize(QSize(icon_size, icon_size))
window.setLayout(layout)


select_button_clicked()
window.show()
sys.exit(app.exec())
