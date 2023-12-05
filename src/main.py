import zipfile
import os
import requests
import subprocess
from PyQt6.QtWidgets import QApplication

CURRENT_PATH = os.getcwd()
ARCHIVE_PATH = CURRENT_PATH + "/Downloads.zip"
EXTRACT_PATH = CURRENT_PATH + "/Downloads"
ARCHIVE_URL = "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1qGbBqnwju7w8YT8zrWQwO4P589sqfs-T"

APPLICATION = {
    "Discord": "DiscordSetup.exe",
    "Zoom": "ZoomInstaller.exe",
    "Telegram": "telegram.exe",
    "Yandex Browser": "Yandex.exe",
    "Vivaldi": "Vivaldi.exe",
    "BraveBrowser": "BraveBrowserSetup.exe",
    "Chrome": "ChromeSetup.exe",
    "AnyDesk": "AnyDesk.exe",
    "WinRar": "winrar.exe",
    "Steam": "SteamSetup.exe",
    "Epic Games Launcher": "EpicInstaller.msi",
    "MSI Afterburner": "MSI-Afterburner.exe",
    "CPU-Z": "cpu-z.exe",
    "LA Pleer": "LA_Setup.exe",
    "Nvidia GeForce Experience": "GeForce_Experience.exe"
}


# функция для скачивания архива
def download_archive(url, save_path, update_status_callback):
    print('ddddd')
    response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        update_status_callback("Скачивание завершено")
    else:
        dl = 0
        total_length = int(total_length)
        with open(save_path, 'wb') as file:
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                file.write(data)
                done = int(100 * dl / total_length)
                update_status_callback(f"Скачивается... {done}%")
        update_status_callback("Скачивание завершено")


# Функция извлечения
def download_and_extract(url, save_path, selection, update_status_callback):
    # Сначала загружаем архив
    download_archive(url, save_path, update_status_callback)

    # Проверяем наличие архива
    if os.path.exists(ARCHIVE_PATH):
        # Извлекаем выбранные приложения
        with zipfile.ZipFile(ARCHIVE_PATH, "r") as archive:
            for app in selection:
                if app in APPLICATION:
                    app_file = APPLICATION[app]
                    archive.extract(app_file, EXTRACT_PATH)
                    print(f"Приложение {app} успешно извлечено!")
        update_status_callback("Установка завершена")
    else:
        update_status_callback("Ошибка: архив не найден")


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("WinPostInstaller")

    from interface import WinPostInstaller
    win_post_installer = WinPostInstaller()
    win_post_installer.show()

    app.exec()
