import time
import zipfile
import os
import subprocess

CURRENT_PATH = os.getcwd()
ARCHIVE_PATH = CURRENT_PATH + "/Downloads.zip"
EXTRACT_PATH = CURRENT_PATH + "/Downloads"

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


# Функция извлечения, для работы нужен архив!

# def button_clicked(selection):
#     if selection:
#         print(selection)
#         with zipfile.ZipFile(ARCHIVE_PATH, "r") as archive:
#             for app in selection:
#                 if app in APPLICATION:
#                     app_file = APPLICATION[app]
#                     archive.extract(app_file, EXTRACT_PATH)
#
