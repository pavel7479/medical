
import streamlit as st
from TextRecognizer import TextRecognizer
from TextProcessor import TextProcessor
from FileManager import FileManager

class StreamlitApp:
    def __init__(self, medical_app):
        self.medical_app = medical_app
        self.file_manager = FileManager()

    def run(self):
        st.title("Medical OCR & Keyword Extraction")

        uploaded_file = st.file_uploader("Загрузите изображение", type=["jpg", "png"])

        if uploaded_file:
            # Сохранение файла
            image_path = self.file_manager.save_uploaded_file(uploaded_file)
            st.image(image_path, caption="Загруженное изображение", use_column_width=True)

            # Распознавание текста
            recognizer = TextRecognizer()
            extracted_text = recognizer.recognize_with_easyocr(image_path)
            st.text_area("Распознанный текст", extracted_text, height=200)

            # Обработка текста
            processor = TextProcessor('keywords.txt')
            keywords_data = processor.extract_keywords(extracted_text)

            # Сохранение результатов в JSON
            json_path = self.file_manager.save_json_file(keywords_data)
            st.success(f"Результат сохранён в {json_path}")

            # Вывод ключевых слов
            st.json(keywords_data)
