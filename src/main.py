import zipfile
import os
import requests
import subprocess
from PyQt6.QtWidgets import QApplication

CURRENT_PATH = os.getcwd()[:-4]
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
    "Epic Games": "EpicInstaller.msi",
    "MSI Afterburner": "MSI-Afterburner.exe",
    "CPU-Z": "cpu-z.exe",
    "LA Pleer": "LA_Setup.exe",
    "GeForce Experience": "GeForce_Experience.exe"
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
        # install_extracted_programs(update_status_callback)
        update_status_callback("Установка завершена")
    else:
        update_status_callback("Ошибка: архив не найден")


# def install_extracted_programs(update_status_callback):
#     files = os.listdir(EXTRACT_PATH)
#
#     exe_files = [file for file in files if file.lower().endswith('.exe')]
#     for exe_file in exe_files:
#         exe_path = os.path.join(EXTRACT_PATH, exe_file)
#
#         install_command = f'"{exe_path}" /S'
#         try:
#             subprocess.run(install_command, shell=True, check=True)
#             update_status_callback(f'{exe_file} успешно установлен.')
#         except subprocess.CalledProcessError as e:
#             update_status_callback(f'Ошибка при установке {exe_file}: {e}')
#
#
# def photo_wiever():
#     extensions = ['.jpg', '.jpeg', '.gif', '.png', '.bmp', '.tiff', '.ico']
#     assoc_value = 'PhotoViewer.FileAssoc.Tiff'
#
#     for extension in extensions:
#         command = f'reg add HKCU\Software\Classes\{extension} /ve /t REG_SZ /d {assoc_value} /f'
#         subprocess.run(command, shell=True)
#
#
# def defender_off():
#     command1 = 'REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d 1 /f'
#
#     command2 = 'REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableBehaviorMonitoring" /t REG_DWORD /d 1 /f'
#     command3 = 'REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableOnAccessProtection" /t REG_DWORD /d 1 /f'
#     command4 = 'REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableScanOnRealtimeEnable" /t REG_DWORD /d 1 /f'
#
#     command5 = 'REG ADD "HKLM\SYSTEM\CurrentControlSet\Services\SecurityHealthService" /v "Start" /t REG_DWORD /d 3 /f'
#
#     subprocess.run(command1, shell=True)
#     subprocess.run(command2, shell=True)
#     subprocess.run(command3, shell=True)
#     subprocess.run(command4, shell=True)
#     subprocess.run(command5, shell=True)
#
#
# def defender_notifications_off():
#     subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "off"])
#     key_path = r"HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows Defender Security Center\\Notifications"
#     # Команда для добавления значения DisableNotifications
#     command_disable_notifications = f'reg add "{key_path}" /v "DisableNotifications" /t REG_DWORD /d 1 /f'
#     # Команда для добавления значения DisableEnhancedNotifications
#     command_disable_enhanced_notifications = f'reg add "{key_path}" /v "DisableEnhancedNotifications" /t REG_DWORD /d 1 /f'
#     # Выполняем команды через subprocess
#     subprocess.run(command_disable_notifications, shell=True)
#     subprocess.run(command_disable_enhanced_notifications, shell=True)


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("WinPostInstaller")

    from interface import WinPostInstaller

    win_post_installer = WinPostInstaller()
    win_post_installer.show()

    app.exec()
