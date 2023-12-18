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
    "Notepad++",
    "VSCode"
}


# функция для скачивания архива
def download_archive(url, save_path, selection, update_status_callback, count):
    try:
        if not os.path.exists(ARCHIVE_PATH):
            update_status_callback("Ошибка: архив не найден")
            time.sleep(1)

            # Получение содержимого архива по URL
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            # Загрузка архива по частям или целиком в зависимости от информации о размере
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

        # Извлечение приложений из архива после загрузки
        extract_applications(url, save_path, selection, update_status_callback)

    except Exception as e:
        count += 1
        if count <= 3:
            download_archive(url, save_path, selection, update_status_callback, count)
        update_status_callback("Ошибка при скачивании архива\nпроверьте подключение к интернету")
        print(f"Ошибка при скачивании архива: {e}")


# Извлечение приложений из архива
def extract_applications(url, save_path, selection, update_status_callback):
    try:
        # Проверка наличия архива для извлечения приложений
        if not os.path.exists(ARCHIVE_PATH):
            update_status_callback("Ошибка: архив не найден")
            time.sleep(1)
            download_archive(url, save_path, selection,update_status_callback, 0)
        if os.path.exists(ARCHIVE_PATH):
            # Извлечение выбранных приложений из архива
            with zipfile.ZipFile(ARCHIVE_PATH, "r") as archive:
                for app in selection:
                    if app in APPLICATION:
                        app_file = APPLICATION[app]
                        archive.extract(app_file, EXTRACT_PATH)
                        update_status_callback(f"{app} извлечено")
                        print(f"Приложение {app} успешно извлечено!")
                        time.sleep(0.2)
            time.sleep(1)
        install_applications(selection, update_status_callback)
    except Exception as e:
        print(f"Ошибка в extract_applications: {e}")


# Установка приложений
def install_applications(selection, update_status_callback):
    try:
        # Разделение приложений на тихую и обычную установки
        silent_install_apps = [app for app in selection if app in SILENT_INSTALL_APPS]
        regular_install_apps = [app for app in selection if app not in SILENT_INSTALL_APPS]

        # Установка тихих приложений
        for app in silent_install_apps:
            if app in APPLICATION:
                app_file = os.path.join(EXTRACT_PATH, APPLICATION[app])
                if app == "7-Zip":
                    update_status_callback(f"{app} устанавливается.")
                    subprocess.run([app_file, "/S"], check=True, shell=True)
                else:
                    update_status_callback(f"{app} устанавливается.")
                    subprocess.run([app_file, "/S", "/silent", "/verysilent", "/quiet", "/qn"], check=True, shell=True)
                update_status_callback(f"{app} установлен тихо")
                print(f"Приложение {app} установлено тихо.")
                time.sleep(2)

        # Установка обычных приложений
        for app in regular_install_apps:
            if app in APPLICATION:
                app_file = os.path.join(EXTRACT_PATH, APPLICATION[app])
                subprocess.run([app_file], check=True, shell=True)  # Обычная установка
                update_status_callback(f"{app} установлен.")
                print(f"Приложение {app} установлено.")
                time.sleep(2)

        time.sleep(2)
        remove_extracted_applications()

    except Exception as e:
        print(f"Ошибка в install_applications: {e}")
        update_status_callback("Ошибка при установке.\n")


# Функция для отключения автозагрузки приложений
def disable_autostart(update_status_callback):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run",
                             0, winreg.KEY_ALL_ACCESS)
        i = 0
        while True:
            try:
                name, value, type = winreg.EnumValue(key, i)  # Получение имени, значения и типа каждой записи
                winreg.DeleteValue(key, name)  # Удаление
                update_status_callback(f"Автозагрузка отключена:\n{name}")
                print(f"Автозагрузка отключена для: {name}")
                time.sleep(0.5)
            except OSError:
                break
            i += 1
        winreg.CloseKey(key)  # Закрытие ключа реестра
        return True
    except Exception as e:
        print(f"Ошибка при отключении автозагрузки: {e}")
        update_status_callback("Ошибка при отключении\nавтозагрузки")
        return False


# Функция для удаления извлеченных приложений
def remove_extracted_applications():
    try:
        if os.path.exists(EXTRACT_PATH):
            for file_name in os.listdir(EXTRACT_PATH):
                file_path = os.path.join(EXTRACT_PATH, file_name)
                if os.path.isfile(file_path):  # Проверка, является ли объект файлом
                    os.remove(file_path)
                    print(f"Удален файл: {file_name}")
                    time.sleep(0.5)
        else:
            print("Папка не найдена")
    except Exception as e:
        print(f"Ошибка при удалении файлов: {e}")


if __name__ == "__main__":
    # Создание приложения GUI
    app = QApplication([])
    app.setApplicationName("WinPostInstaller")

    # Загрузка интерфейса приложения
    from interface import WinPostInstaller

    win_post_installer = WinPostInstaller()
    win_post_installer.show()

    app.exec()  # Запуск главного цикла приложения
