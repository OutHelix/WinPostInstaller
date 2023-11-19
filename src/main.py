import time
import zipfile
import os
import subprocess
import requests

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
def download_archive(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print("Архив успешно скачан!")


# Функция извлечения
def button_clicked(selection):
    # Проверяем наличие архива
    if not os.path.exists(ARCHIVE_PATH):
        download_archive(ARCHIVE_URL, ARCHIVE_PATH)

    # Извлечение выбранных приложений из архива
    with zipfile.ZipFile(ARCHIVE_PATH, "r") as archive:
        for app in selection:
            if app in APPLICATION:
                app_file = APPLICATION[app]
                archive.extract(app_file, EXTRACT_PATH)
                print(f"Приложение {app} успешно извлечено!")