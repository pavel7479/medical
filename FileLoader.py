import os

class FileLoader:
    """Класс для загрузки данных из файлов."""

    @staticmethod
    def load_keywords(file_path):
        """Загружает ключевые слова из файла."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден.")

        with open(file_path, "r", encoding="utf-8") as file:
            keywords = [line.strip() for line in file if line.strip()]

        return keywords

    @staticmethod
    def load_prompt(file_path):
        """Загружает промт из файла."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден.")

        with open(file_path, "r", encoding="utf-8") as file:
            prompt = file.read().strip()

        return prompt