from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QCheckBox, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize


class WinPostInstaller(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("WinPostInstaller")
        self.setStyleSheet("background-color: #1E1E1E;")
        self.setGeometry(650, 300, 750, 400)

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        columns = []

        for _ in range(3):
            column_layout = QVBoxLayout()
            columns.append(column_layout)
            layout.addLayout(column_layout)

        checkboxes = [
            ("Discord", "discord.png"), ("Zoom", "zoom.png"), ("Telegram", "telegram.png"),
            ("Yandex Browser", "yandex.png"), ("Vivaldi", "vivaldi.png"), ("BraveBrowser", "brave.png"),
            ("Chrome", "chrome.png"), ("AnyDesk", "anyDesk.png"), ("WinRar", "winRar.png"),
            ("Steam", "steam.png"), ("Epic Games Launcher", "epicGames.png"), ("MSI Afterburner", "msiAfterburner.png"),
            ("CPU-Z", "cpu-z.png"), ("LA Pleer", "laPleer.png"), ("Nvidia GeForce Experience", "geforceExperience.png")
        ]

        checkbox_objects = []

        for text, icon_path in checkboxes:
            checkbox = QCheckBox(text)
            checkbox.setIcon(QIcon(icon_path))
            checkbox.setIconSize(QSize(20, 20))
            checkbox_objects.append(checkbox)

            columns[checkboxes.index((text, icon_path)) % 3].addWidget(checkbox)
            checkbox.stateChanged.connect(self.checkbox_changed)

        layout.addSpacing(20)

        self.select_button = QPushButton("Выбрать и установить")
        self.cancel_button = QPushButton("Отмена")

        self.select_button.setStyleSheet(
            "background-color: #F0FFFF; border-color: #E6E6FA; border-style: solid; border-width: 4px;"
            " border-radius: 6px; color: black;")
        self.cancel_button.setStyleSheet(
            "background-color: #F0FFFF; border-color: #00CED1; border-style: solid; border-width: 4px;"
            " border-radius: 6px; color: black;")

        self.select_button.clicked.connect(self.select_button_clicked)
        self.cancel_button.clicked.connect(self.cancel_button_clicked)

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.select_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.status_label = QLabel()
        self.status_label.setStyleSheet("color: white;")
        status_layout = QHBoxLayout()
        status_layout.addWidget(self.status_label, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        layout.addLayout(status_layout)

        self.update_selected_count()

    def update_selected_count(self):
        checkbox_objects = self.findChildren(QCheckBox)
        selected_count = sum(checkbox.isChecked() for checkbox in checkbox_objects)
        self.status_label.setText(f"Выбрано {selected_count} пункт(ов):")

    def checkbox_changed(self):
        self.update_selected_count()

    def select_button_clicked(self):
        checkbox_objects = self.findChildren(QCheckBox)
        selected_checkboxes = [checkbox.text() for checkbox in checkbox_objects if checkbox.isChecked()]

        if selected_checkboxes:
            self.button_clicked(selected_checkboxes)

    def cancel_button_clicked(self):
        checkbox_objects = self.findChildren(QCheckBox)
        for checkbox in checkbox_objects:
            checkbox.setChecked(False)

        self.update_selected_count()
        print("Отменить выбор")

    def button_clicked(self, selected_checkboxes):
        print("Выбранные программы:", selected_checkboxes)
        

app = QApplication([])
app.setApplicationName("WinPostInstaller")

win_post_installer = WinPostInstaller()
win_post_installer.show()

app.exec()
