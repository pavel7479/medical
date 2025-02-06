
from FileLoader import FileLoader
from FileManager import FileManager
from FilePaths import FilePaths
from TextRecognizer import TextRecognizer
from TextProcessor import TextProcessor
from OllamaInstaller import OllamaInstaller
from OllamaClient import OllamaClient
from StreamlitAPI import StreamlitApp

class MedicalApp:
    def __init__(self):
        """Инициализация приложения."""
        self.file_paths = None
        self.keywords = None
        self.prompt = None
        self.recognizer = TextRecognizer()
        self.processor = None
        self.ollama_installer = OllamaInstaller()
        self.ollama_client = OllamaClient()
        self.file_manager = FileLoader()  # Добавил file_manager
        self.file_manager = FileManager()

    def load_files(self, image_file, keywords_file, prompt_file):
        """Загружает пути файлов и данные."""
        self.file_paths = FilePaths(
            image_path=image_file,
            easyocr_output_path="recognized_text_easyocr.txt",
            csv_output_path="keyword_values.json",
            keywords_file_path=keywords_file,
            prompt_file_path=prompt_file
        )

        try:
            self.keywords = self.file_manager.load_keywords(self.file_paths.keywords_file_path)
            self.prompt = self.file_manager.load_prompt(self.file_paths.prompt_file_path)
            return "Файлы загружены успешно."
        except FileNotFoundError as e:
            return f"Ошибка загрузки: {e}"

    def recognize_text(self):
        """Распознает текст с изображения."""
        easyocr_text = self.recognizer.recognize_with_easyocr(self.file_paths.image_path)
        with open(self.file_paths.easyocr_output_path, "w", encoding="utf-8") as file:
            file.write(easyocr_text)
        return easyocr_text

    def extract_keywords(self, text):
        """Извлекает ключевые слова."""
        self.processor = TextProcessor(self.keywords)
        keyword_values = self.processor.extract_keywords(text)
        self.processor.save_to_json(keyword_values, self.file_paths.csv_output_path)
        return keyword_values

    def run_ollama(self, text):
        """Устанавливает и запускает Ollama, обрабатывает текст."""
        self.ollama_installer.install_ollama()
        self.ollama_installer.start_ollama()
        self.ollama_installer.pull_model()
        response = self.ollama_client.ask_ollama(self.prompt.format(keywords=self.keywords, easyocr_text=text))
        return response

# def main():
#     """Функция для запуска Streamlit-приложения."""
#     app = MedicalApp()
#     streamlit_app = StreamlitApp(app)  # Передаём file_manager
#     streamlit_app.run()
#
# if __name__ == "__main__":
#     main()


