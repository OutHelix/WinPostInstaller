from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QCheckBox, QLabel, QMainWindow,
                             QPushButton, QFontComboBox)
from PyQt5.QtCore import Qt


app = QApplication([])
app.setApplicationName("WinPostInstaller")


window = QWidget()
window_width = 750
window_height = 400
window.setGeometry(650, 300, window_width, window_height)
window.setWindowTitle("WinPostInstaller")


layout = QVBoxLayout(window)


checkbox1 = QCheckBox("Discord")
checkbox2 = QCheckBox("Zoom")
checkbox3 = QCheckBox("Skype")


label1 = QLabel("")
label2 = QLabel("")
label3 = QLabel("")
status_label = QLabel()


layout.addWidget(checkbox1)
layout.addWidget(label1)
layout.addWidget(checkbox2)
layout.addWidget(label2)
layout.addWidget(checkbox3)
layout.addWidget(label3)
layout.addWidget(status_label, alignment=Qt.AlignBottom | Qt.AlignLeft)


checkbox_states = {}


def checkbox_changed():
    sender = window.sender()
    checkbox_states[sender] = sender.isChecked()
    selected_count = sum(checkbox_states.values())
    if selected_count == 0:
        status_label.setText("Вы пока не выбрали ни одного пункта для установки.")
    else:
        status_label.setText(f"Вы выбрали {selected_count} пункт(ов):")


checkbox1.stateChanged.connect(checkbox_changed)
checkbox2.stateChanged.connect(checkbox_changed)
checkbox3.stateChanged.connect(checkbox_changed)


select_button = QPushButton("Выбрать и установить")
cancel_button = QPushButton("Отмена")


def select_button_clicked():
    for checkbox, state in checkbox_states.items():
        if state:
            print(checkbox.text())
            print("Выбрать и установить")


def cancel_button_clicked():
    print("Отменить выбор")


select_button.clicked.connect(select_button_clicked)
cancel_button.clicked.connect(cancel_button_clicked)


select_button.setStyleSheet("background-color: green;")
cancel_button.setStyleSheet("background-color: red;")
status_label.setStyleSheet("backgrounf-color: yellow; padding: 5px;")

button_layout = QHBoxLayout()
button_layout.addStretch(1)
button_layout.addWidget(select_button)
button_layout.addWidget(cancel_button)


layout.addLayout(button_layout)


window.setLayout(layout)
window.show()
app.exec()
