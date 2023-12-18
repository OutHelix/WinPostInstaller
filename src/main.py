import time
import winreg
import zipfile
import os

import requests
import subprocess
from PyQt6.QtWidgets import QApplication

CURRENT_PATH = os.getcwd()
if CURRENT_PATH.find("src"):
    CURRENT_PATH = CURRENT_PATH[:-4]
ARCHIVE_PATH = CURRENT_PATH + "\\Downloads.zip"
EXTRACT_PATH = CURRENT_PATH + "\\Downloads"
ARCHIVE_URL = "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=14PgenzJx4GJamJTo0kCijJ7uXz2xiJWl"

APPLICATION = {
    "Discord": "DiscordSetup.exe",
    "Telegram": "telegram.exe",
    "CPU-Z": "cpu-z.exe",
    "Adobe Acrobat": "AdobeAR.exe",
    "7-Zip": "7z.exe",
    "VLC": "vlc.exe",
    "Notepad++": "npp.exe",
    "Chrome": "ChromeSetup.exe",
    "VSCode": "VSCode.exe",
    "Vivaldi": "Vivaldi.exe",
    "WinRar": "winrar.exe",
    "Steam": "SteamSetup.exe",
    "MSI Afterburner": "MSI-Afterburner.exe",
}

# Приложения, которые могут устанавливаться тихо
SILENT_INSTALL_APPS = {
    "Discord",
    "Telegram",
    "CPU-Z",
    "7-Zip",
    "LA Pleer",
    # "Adobe Acrobat", - возможно убран навсегда
    # "VLC", - временно убран
    "Notepad++",
    "VSCode"
}


# функция для скачивания архива
def download_archive(url, save_path, update_status_callback):
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

    # Проверяем наличие архива
    if not os.path.exists(ARCHIVE_PATH):
        update_status_callback("Ошибка: архив не найден")
        time.sleep(1)
        download_archive(url, save_path, update_status_callback)
    if os.path.exists(ARCHIVE_PATH):
        # Извлекаем выбранные приложения
        with zipfile.ZipFile(ARCHIVE_PATH, "r") as archive:
            for app in selection:
                if app in APPLICATION:
                    app_file = APPLICATION[app]
                    archive.extract(app_file, EXTRACT_PATH)
                    print(f"Приложение {app} успешно извлечено!")
        # install_extracted_programs(update_status_callback)
                    update_status_callback(f"{app} распакован")
        time.sleep(1)

    silent_install_apps = [app for app in selection if app in SILENT_INSTALL_APPS]
    regular_install_apps = [app for app in selection if app not in SILENT_INSTALL_APPS]

    # Установка тихих приложений
    for app in silent_install_apps:
        if app in APPLICATION:
            app_file = os.path.join(EXTRACT_PATH, APPLICATION[app])
            if app == "7-Zip":
                update_status_callback(f"{app} устанвливается.")
                subprocess.run([app_file, "/S"], check=True, shell=True)
            else:
                update_status_callback(f"{app} устанвливается.")
                subprocess.run([app_file, "/S", "/silent", "/verysilent", "/quiet", "/qn"], check=True, shell=True)
            update_status_callback(f"{app} установлен.")
            print(f"Приложение {app} установлено тихо.")
            time.sleep(2)

    # Установка остальных приложений
    for app in regular_install_apps:
        if app in APPLICATION:
            app_file = os.path.join(EXTRACT_PATH, APPLICATION[app])
            subprocess.run([app_file], check=True, shell=True)  # Обычная установка
            print(f"Приложение {app} установлено.")
            update_status_callback(f"{app} установлен.")
            time.sleep(2)


def disable_autostart(update_status_callback):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run",
                             0, winreg.KEY_ALL_ACCESS)
        i = 0
        while True:
            try:
                name, value, type = winreg.EnumValue(key, i)
                winreg.DeleteValue(key, name)
                update_status_callback(f"Автозагрузка отключена:\n{name}")
                print(f"Автозагрузка отключена для: {name}")
                time.sleep(0.5)
            except OSError:
                break
            i += 1
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f"Ошибка при отключении автозагрузки: {e}")
        update_status_callback("Ошибка при отключении\nавтозагрузки")
        return False


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("WinPostInstaller")

    from interface import WinPostInstaller

    win_post_installer = WinPostInstaller()
    win_post_installer.show()

    app.exec()
