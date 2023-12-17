import threading
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QCheckBox, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QMessageBox
from main import CURRENT_PATH


class ProgramCheckbox(QCheckBox):
    def __init__(self, text, icon_path):
        super().__init__(text)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(20, 20))


def message_after_select_button_clicked():
    message_box = QMessageBox()
    message_box.setStyleSheet(
        "background-color: #2C394B; color: white;"
        "font: 12pt;"
    )
    message_box.setText("Убедитесь, что вашей системой является Windows 10 (64-бит)")
    message_box.setWindowTitle("Внимание")
    message_box.setIcon(QMessageBox.Icon.Information)

    ok_button = message_box.addButton(QMessageBox.StandardButton.Ok)
    ok_button.setStyleSheet(
        "background-color: #F0FFFF; border-color: #9370DB; border-style: solid; border-width: 3px;"
        " border-radius: 6px; color: black; min-width: 100px; min-height: 30px;"
    )

    message_box.exec()


class WinPostInstaller(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("WinPostInstaller")
        self.setStyleSheet("background-color: #2C394B; color: white;")
        self.setGeometry(650, 300, 750, 400)
        self.setFixedSize(800, 250)

        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)

        self.create_checkboxes()
        self.create_status_layout_and_select_button()
        self.update_selected_count()

    def create_checkboxes(self):
        columns = [QVBoxLayout() for _ in range(3)]
        checkbox_layouts = {0: columns[0], 1: columns[1], 2: columns[2]}
        checkboxes = [
            ("Discord", f"{CURRENT_PATH}\\icons\\discord.png"),
            ("Telegram", f"{CURRENT_PATH}\\icons\\telegram.png"),
            ("Vivaldi", f"{CURRENT_PATH}\\icons\\vivaldi.png"),
            ("Chrome", f"{CURRENT_PATH}\\icons\\chrome.png"),
            ("WinRar", f"{CURRENT_PATH}\\icons\\winrar.png"),
            ("Steam", f"{CURRENT_PATH}\\icons\\steam.png"),
            ("MSI Afterburner", f"{CURRENT_PATH}\\icons\\msi.png"),
            ("CPU-Z", f"{CURRENT_PATH}\\icons\\cpu-z.png"),
            ("7-Zip", f"{CURRENT_PATH}\\icons\\7zip.png"),
            ("(!) VLC", f"{CURRENT_PATH}\\icons\\vlc.png"),
            ("VSCode", f"{CURRENT_PATH}\\icons\\vscode.png"),
            ("Notepad++", f"{CURRENT_PATH}\\icons\\notepad.png"),
            ("Отключить WinDef", f"{CURRENT_PATH}\\icons\\windef.png"),
            ("Отключить уведомления WD", f"{CURRENT_PATH}\\icons\\notification.png"),
            ("Отключить автозапуск программ", f"{CURRENT_PATH}\\icons\\autostart.png")
        ]

        self.checkbox_objects = []

        for text, icon_path in checkboxes:
            checkbox = ProgramCheckbox(text, icon_path)
            self.checkbox_objects.append(checkbox)

            column_index = checkboxes.index((text, icon_path)) % 3
            checkbox_layouts[column_index].addWidget(checkbox)
            checkbox.stateChanged.connect(self.checkbox_changed)

        self.layout.addSpacing(20)
        self.layout.addLayout(columns[0])
        self.layout.addLayout(columns[1])
        self.layout.addLayout(columns[2])

    def create_status_layout_and_select_button(self):
        status_layout = QVBoxLayout()

        self.status_label = QLabel()
        self.status_label.setStyleSheet("color: white;")
        status_layout.addWidget(self.status_label, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)

        self.select_button = QPushButton("Установить")
        self.select_button.setStyleSheet(
            "background-color: #F0FFFF; border-color: #9370DB; border-style: solid; border-width: 4px;"
            " border-radius: 6px; color: black;")
        self.select_button.clicked.connect(self.select_button_clicked)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.select_button)

        status_layout.addLayout(button_layout)
        self.layout.addLayout(status_layout)

    def update_selected_count(self):
        selected_count = sum(checkbox.isChecked() for checkbox in self.checkbox_objects)
        self.status_label.setText(f"Выбрано {selected_count} пункт(ов)")

    def checkbox_changed(self):
        sender_checkbox = self.sender()
        if sender_checkbox.text() == "Отключить WinDef":
            for checkbox in self.checkbox_objects:
                if checkbox.text() == "Отключить уведомления WD":
                    checkbox.setChecked(sender_checkbox.isChecked())

        self.update_selected_count()

    def select_button_clicked(self):
        selected_checkboxes = [checkbox.text() for checkbox in self.checkbox_objects if checkbox.isChecked()]

        if selected_checkboxes:
            from main import ARCHIVE_URL, ARCHIVE_PATH
            message_after_select_button_clicked()
            self.start_download(selected_checkboxes, ARCHIVE_URL, ARCHIVE_PATH)

    def start_download(self, selected_checkboxes, url, path):
        download_thread = threading.Thread(target=self.download_and_extract_threaded,
                                           args=(selected_checkboxes, url, path))
        download_thread.start()

    def download_and_extract_threaded(self, selected_checkboxes, url, path):
        from main import download_and_extract
        download_and_extract(url, path, selected_checkboxes, self.update_status)

    def update_status(self, text):
        self.status_label.setText(f"Статус: {text}")
