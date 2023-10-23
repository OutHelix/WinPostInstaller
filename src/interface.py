from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QCheckBox, QLabel, QMainWindow, QPushButton, QFontComboBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QPainter, QPixmap, QIcon
import sys


app = QApplication([])
app.setApplicationName("WinPostInstaller")


window = QWidget()
window.setGeometry(650, 300, 750, 400)
window.setWindowTitle("WinPostInstaller")
window.setStyleSheet("background-color: #1E1E1E;")

layout = QVBoxLayout(window)


checkbox1 = QCheckBox("Discord")
checkbox2 = QCheckBox("Zoom")
checkbox3 = QCheckBox("Skype")


label1 = QLabel("")
label2 = QLabel("")
label3 = QLabel("")
status_label = QLabel()
status_label.setStyleSheet("color: white;")


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
        status_label.setText("Пожалуйста, выберете программу/ы для установки.")
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


checkbox_style = """
QCheckBox {
    color: white
}
"""


select_button.setStyleSheet("background-color: green; color: white;")
cancel_button.setStyleSheet("background-color: red; color: white;")
checkbox1.setStyleSheet(checkbox_style)
checkbox2.setStyleSheet(checkbox_style)
checkbox3.setStyleSheet(checkbox_style)

button_layout = QHBoxLayout()
button_layout.addStretch(1)
button_layout.addWidget(select_button)
button_layout.addWidget(cancel_button)


layout.addLayout(button_layout)


icon1 = QIcon(r"discord.png")
icon2 = QIcon(r"zoom.png")
icon3 = QIcon(r"skype.png")
checkbox1.setIcon(icon1)
checkbox2.setIcon(icon2)
checkbox3.setIcon(icon3)


icon_size = 50
checkbox1.setIconSize(QSize(icon_size, icon_size))
checkbox2.setIconSize(QSize(icon_size, icon_size))
checkbox3.setIconSize(QSize(icon_size, icon_size))
window.setLayout(layout)


select_button_clicked()
window.show()
sys.exit(app.exec())
