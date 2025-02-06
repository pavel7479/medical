import cv2
from PIL import Image
import pytesseract
import easyocr
import os
"""
Распознаёт текст используя EasyOCR
"""
class TextRecognizer:
    """Класс для распознавания текста с изображений с использованием Tesseract и EasyOCR."""

    def __init__(self, tesseract_lang='rus', easyocr_lang=['ru']):
        self.tesseract_lang = tesseract_lang
        self.easyocr_lang = easyocr_lang
        self.easyocr_reader = easyocr.Reader(easyocr_lang)

    def recognize_with_easyocr(self, image_path):
        """Распознает текст с изображения с помощью EasyOCR."""

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл {image_path} не найден!")

        # Загрузка изображения с проверкой
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Не удалось загрузить изображение {image_path}. Проверьте формат файла!")

        result = self.easyocr_reader.readtext(image_path)
        recognized_text = "\n".join([detection[1] for detection in result])
        return recognized_text
#======================================================================================================

