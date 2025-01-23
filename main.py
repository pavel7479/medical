import streamlit as st
from image_processor import ImageProcessor
import cv2
import numpy as np
from PIL import Image

# Инициализация ImageProcessor
processor = ImageProcessor()

# Заголовок приложения
st.title("Выравнивание текста на изображении")

# Загрузка изображения
uploaded_file = st.file_uploader("Загрузите изображение с текстом", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Преобразуем файл в массив numpy
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Отображаем оригинальное изображение
    st.image(image, caption="Оригинальное изображение", use_column_width=True)

    # Выравниваем изображение
    aligned_image = processor.align_image(image)

    # Отображаем выровненное изображение
    st.image(aligned_image, caption="Выровненное изображение", use_column_width=True)

    # Сохраняем выровненное изображение
    output_filename = f"aligned_{uploaded_file.name}"
    output_path = processor.save_image(aligned_image, output_filename)

    # Показываем путь к сохранённому файлу
    st.success(f"Изображение сохранено: {output_path}")