import os
import shutil
import json

class FileManager:
    """Класс для управления загрузкой и сохранением файлов."""

    def __init__(self, upload_dir="uploads"):
        self.upload_dir = upload_dir
        os.makedirs(self.upload_dir, exist_ok=True)  # Создаём папку, если её нет

    def save_uploaded_file(self, uploaded_file):
        """Сохраняет загруженный файл и возвращает его путь."""
        file_path = os.path.join(self.upload_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path

    def save_json_file(self, data, filename="output.json"):
        """Сохраняет данные в JSON-файл."""
        json_path = os.path.join(self.upload_dir, filename)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return json_path

    def delete_file(self, file_path):
        """Удаляет файл, если он существует."""
        if os.path.exists(file_path):
            os.remove(file_path)

    def clear_upload_folder(self):
        """Удаляет все файлы в папке загрузок."""
        if os.path.exists(self.upload_dir):
            shutil.rmtree(self.upload_dir)
            os.makedirs(self.upload_dir, exist_ok=True)
