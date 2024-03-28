import os
import shutil
from pathlib import Path

def clear_temp_folder():
    temp_folder = Path(os.environ.get('TEMP', ''))
    deleted_files = 0
    deleted_dirs = 0
    total_size = 0  # Переменная для подсчета общего размера удаленных файлов

    for item in temp_folder.iterdir():
        try:
            if item.is_file():
                total_size += item.stat().st_size  # Добавляем размер файла к общему размеру
                item.unlink()
                deleted_files += 1
            elif item.is_dir():
                item.rmdir()
                deleted_dirs += 1
        except Exception as e:
            print(f"Ошибка в удалении: {item.name}")

    total_size_mb = total_size / (1024 * 1024)  # Переводим общий размер в мегабайты
    print(f"Удалено файлов: {deleted_files}")
    print(f"Удалено директорий: {deleted_dirs}")
    print(f"Примерный размер удаленных файлов: {total_size_mb:.2f} MB")

if __name__ == "__main__":
    clear_temp_folder()
    message = "Черный закончил работу"
    print(message)
