from symspellpy import SymSpell
import re
import csv
import json
class TextProcessor:
    """Класс для обработки текста и извлечения ключевых слов и их значений. Сохраняет результат в файл .csv"""

    def __init__(self, keywords):
        self.keywords = keywords
        self.sym_spell = SymSpell()
        self._initialize_sym_spell()

    def _initialize_sym_spell(self):
        """Инициализирует SymSpell для исправления ошибок в тексте."""
        for word in self.keywords:
            self.sym_spell.create_dictionary_entry(word, 1)

    def extract_keywords(self, text):
        """Извлекает ключевые слова и их значения из текста."""
        keyword_values = {}
        for line in text.split("\n"):
            cleaned_line = re.sub(r"[+\-—|]", " ", line).strip()

            print("Используемые ключевые слова:", self.keywords) # отладка кода

            for keyword in self.keywords:
                if keyword in cleaned_line:
                    match = re.search(r"\d+\.\d+", cleaned_line)
                    if match:
                        value = float(match.group())
                        keyword_values[keyword] = value
                        print(f"Найдено ключевое слово: {keyword}, значение: {value}")
        return keyword_values

    def save_to_json(self, keyword_values, output_file_path):
        """Сохраняет ключевые слова и их значения в JSON-файл."""
        with open(output_file_path, "w", encoding="utf-8") as file:
            json.dump(keyword_values, file, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в {output_file_path}")

#====================================================================================
    def _load_keywords(self, file_path):
        """Загружает ключевые слова из файла."""
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

